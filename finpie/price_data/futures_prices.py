#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# finpie - a simple library to download some financial data
# https://github.com/peterlacour/finpie
#
# Copyright (c) 2020 Peter la Cour
#
# Licensed under the MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os
import numpy as np
import pandas as pd
import dask.dataframe as dd
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from concurrent.futures import ThreadPoolExecutor


def historical_futures_contracts(date_range):
    '''
        Function to retrieve historical futures prices of all available futures contracts,
        including currency, interest rate, energy, meat, metals, softs, grains, soybeans,
        fiber and index futures.

        Notice that the download is not very fast and 20 years of data takes around 2 hours
        to download and contains around 2 million rows.

        input: pandas date range, e.g. pd.date_range('2000-01-01', '2020-01-01')
        output: pandas dataframe with prices for all available futures for the
                specified time period
    '''
    with ThreadPoolExecutor(4) as pool:
        res = list( tqdm( pool.map(_download_prices, date_range), total = len(date_range) ))
    df_out = dd.concat( [ i for i in res if type(i) != type([0]) ], axis = 0 )
    df_out = df_out.compute()
    return df_out


def futures_contracts(date):
    return _download_prices(date).compute()


def _download_prices(date):
    '''
    input: datetime object
    output: pandas dataframe with prices for all available futures for the
            specified date
    '''
    errors = []
    if type(date) == type('str'):
        date = pd.to_datetime(date, format = '%Y-%m-%d')
    y = str(date.year)
    if len(str(date.month)) == 2:
        m = str(date.month)
    else:
        m = '0' + str(date.month)
    if len(str(date.day)) == 2:
        d = str(date.day)
    else:
        d = '0' + str(date.day)
    try:
        session = HTMLSession()
        url = f'https://www.mrci.com/ohlc/{y}/{y[-2:]+m+d}.php'
        r = session.get(url)
        soup = bs(r.content, 'html5lib')
        df = pd.read_html( str(soup.find('map').find_next('table')) )[0]
        try:
            futures_lookup = pd.read_csv( os.path.dirname(__file__) + '/futures_lookup.csv').name.tolist()
        except:
            futures_lookup = pd.read_csv( os.path.dirname(__file__) + '\\futures_lookup.csv').name.tolist()
        indices = [ i for i, j in enumerate(df.iloc[:,0]) if j in futures_lookup ]
        columns = ['month', 'date', 'open', 'high', 'low', 'close', 'change', 'volume', 'open_interest', 'change_in_oi' ]
        if len(df.columns) == 11:
            df = df.iloc[indices[0]:-2, :len(df.columns)-1]
        else:
            df = df.iloc[indices[0]:-2, :]
    except:
        errors.append(date)
        return errors
    df.columns = columns
    #[ i for i in np.unique(df.month).tolist() if i not in futures_lookup ]

    first = True
    for i in range(1, len(indices)):
        temp = df.loc[indices[i-1]+1:indices[i]-2].copy()
        temp['future'] = df.loc[indices[i-1], 'month']
        if first:
            out = temp.copy()
            first = False
        else:
            out = out.append(temp)
    out = out[ out.iloc[:,1] != 'Total Volume and Open Interest']
    out.to_csv('futures.csv')
    out.index = [date] * len(out) #pd.to_datetime( [ f'{i[-2:]}/{i[2:4]}/{i[:2]}' for i in out.date ] )
    out.replace('\+', '', regex = True, inplace = True)
    out.replace('unch', np.nan, inplace = True)

    return dd.from_pandas(out, npartitions = 1)
