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

import pandas as pd
import datetime as dt
from finpie.base import DataBase

def cftc( report_type = 'futures_traders', year = 2000 ):

    '''
    # report type options:
    'disaggregated_futures'
    'disaggregated_combined'
    'futures_traders'
    'futures_traders_combined'
    'futures'
    'futures_combined'
    'commodity_index'

    '''
    db = DataBase()

    if report_type == 'disaggregated_futures':
        if year < 2016:
            last_url = ['https://cftc.gov/files/dea/history/fut_disagg_txt_hist_2006_2016.zip']
            url_list = last_url + [ f'https://cftc.gov/files/dea/history/fut_disagg_txt_{i}.zip' for i in range(2016, dt.datetime.today().year + 1) ]
        else:
            url_list = [ f'https://cftc.gov/files/dea/history/fut_disagg_txt_{i}.zip' for i in range(year, dt.datetime.today().year + 1) ]
    elif report_type == 'disaggregated_combined':
        # Disaggregated Futures-and-Options Combined Reports:
        if year < 2016:
            last_url = [ 'https://cftc.gov/files/dea/history/com_disagg_txt_hist_2006_2016.zip' ]
            url_list = last_url + [ f'https://cftc.gov/files/dea/history/com_disagg_txt_{i}.zip' for i in range(2016, dt.datetime.today().year + 1) ]
        else:
            url_list = [ f'https://cftc.gov/files/dea/history/com_disagg_txt_{i}.zip' for i in range(year, dt.datetime.today().year + 1) ]
    elif report_type == 'futures_traders':
        # Disaggregated Futures-and-Options Combined Reports:
        if year < 2016:
            last_url = [ 'https://cftc.gov/files/dea/history/fin_fut_txt_2006_2016.zip' ]
            url_list = last_url + [ f'https://cftc.gov/files/dea/history/fut_fin_txt_{i}.zip' for i in range(2016, dt.datetime.today().year + 1) ]
        else:
            url_list = [ f'https://cftc.gov/files/dea/history/fut_fin_txt_{i}.zip' for i in range(year, dt.datetime.today().year + 1) ]
    elif report_type == 'futures_traders_combined':
        # Disaggregated Futures-and-Options Combined Reports:
        if year < 2016:
            last_url = [ 'https://cftc.gov/files/dea/history/fin_com_txt_2006_2016.zip' ]
            url_list = last_url + [ f'https://cftc.gov/files/dea/history/com_fin_txt_{i}.zip' for i in range(2016, dt.datetime.today().year + 1) ]
        else:
            url_list = [ f'https://cftc.gov/files/dea/history/com_fin_txt_{i}.zip' for i in range(year, dt.datetime.today().year + 1) ]
    elif report_type == 'futures':
        # Disaggregated Futures-and-Options Combined Reports:
        if year < 2016:
            last_url = [ 'https://cftc.gov/files/dea/history/deacot1986_2016.zip' ]
            url_list = last_url + [ f'https://cftc.gov/files/dea/history/deacot{i}.zip' for i in range(2016, dt.datetime.today().year + 1) ]
        else:
            url_list = [ f'https://cftc.gov/files/dea/history/deacot{i}.zip' for i in range(year, dt.datetime.today().year + 1) ]
    elif report_type == 'futures_combined':
        # Disaggregated Futures-and-Options Combined Reports:
        if year < 2016:
            last_url = [ 'https://cftc.gov/files/dea/history/deahistfo_1995_2016.zip' ]
            url_list = last_url + [ f'https://cftc.gov/files/dea/history/deahistfo{i}.zip' for i in range(2016, dt.datetime.today().year + 1) ]
        else:
            url_list = [ f'https://cftc.gov/files/dea/history/deahistfo{i}.zip' for i in range(year, dt.datetime.today().year + 1) ]
    elif report_type == 'commodity_index':
        # Disaggregated Futures-and-Options Combined Reports:
        if year < 2016:
            last_url = [ 'https://cftc.gov/files/dea/history/dea_cit_txt_2006_2016.zip' ]
            url_list = last_url + [ f'https://cftc.gov/files/dea/history/dea_cit_txt_{i}.zip' for i in range(2016, dt.datetime.today().year + 1) ]
        else:
            url_list = [ f'https://cftc.gov/files/dea/history/dea_cit_txt_{i}.zip' for i in range(year, dt.datetime.today().year + 1) ]
    else:
        print('Report type not valied.')
        return None

    df = pd.concat( [ db._load_zip_file(url) for url in url_list ] )
    df.iloc[:,2] = [ i.split(' ')[0] for i in df.iloc[:,2] ]
    try:
        df.index = pd.to_datetime(df.iloc[:,2], format = '%Y-%m-%d')
    except:
        df.index = [ pd.to_datetime(i, format = '%Y-%m-%d') if '/' not in i else pd.to_datetime(i, format = '%m/%d/%Y')  for i in df.iloc[:,2] ]
    df.index.name = 'date'
    df.drop(df.columns[2], axis = 1, inplace = True)
    df.drop(df.columns[1], axis = 1, inplace = True)
    df.columns = [ col.replace(' ', '_').lower() for col in df.columns ]
    df.iloc[1,:] = df.iloc[1,:].astype('str')
    tmp = [ i for i, col in enumerate(df.columns) if col == 'contract_units'][0]
    df.iloc[:,3:tmp] = df.iloc[:,3:tmp].replace('\.', '0', regex = True).astype('float')

    return df


'''
# quick test
prod = 'futures'
year = 2020
df = cftc(prod, year)
df.head()

df = cftc()
'''
