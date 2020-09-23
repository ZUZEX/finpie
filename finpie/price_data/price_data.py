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
import re
import time
import requests
import pandas as pd
import datetime as dt
import dask.dataframe as dd
from io import StringIO
from alpha_vantage.timeseries import TimeSeries
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iexfinance.stocks import get_historical_intraday
from finpie.base import DataBase
#from base import DataBase

def alpha_vantage_prices(ticker, api_token, start_date = None):
    '''

    '''
    ts = TimeSeries(key = api_token, output_format = 'pandas')
    data, meta_data = ts.get_daily_adjusted(symbol = ticker, outputsize = 'full' )
    columns = ['open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient' ]
    data.columns = columns
    data.reset_index(level=0, inplace=True)
    data.iloc[:,1:] = data.iloc[:,1:].astype('float')
    data.date = pd.to_datetime(data.date)
    data.sort_values('date', ascending = True, inplace = True)
    data.index = data.date
    if start_date != None:
        data = data[start_date:]
    data.reset_index(drop = True, inplace = True)
    data.index = data.date
    data.drop('date', axis = 1, inplace = True)
    return data


def tingo_prices( ticker, api_token, start_date = None, end_date = None, freq = '1min'):
    '''

    Example date format = '2017-01-01'

    '''
    if start_date == None:
        start_date = '1980-01-01'
    if end_date == None:
        end_date = dt.datetime.today().date().strftime('%Y-%m-%d')
    headers = {'Content-Type': 'application/json' }
    requestResponse = requests.get(f"https://api.tiingo.com/iex/{ticker}/prices?startDate={start_date}&endDate={end_date}&resampleFreq={freq}&token={api_token}", headers=headers)
    df = pd.DataFrame(requestResponse.json())
    df.date = pd.to_datetime(df.date)

    # iterate through latest dates to get more than the last 10000 rows
    last = df.copy()
    df = dd.from_pandas(df, npartitions = 1)
    while last.date.iloc[0].date() > pd.to_datetime(start_date):
        headers = {'Content-Type': 'application/json' }
        requestResponse = requests.get(f"https://api.tiingo.com/iex/{ticker}/prices?startDate={start_date}&endDate={ last.date.iloc[0].date().strftime('%Y-%m-%d')}&resampleFreq={freq}&token={api_token}", headers=headers)
        temp = pd.DataFrame(requestResponse.json())
        temp.date = pd.to_datetime(temp.date)
        if last.iloc[0,0] == temp.iloc[0,0]:
            break
        last = temp.copy()
        df = df.append(dd.from_pandas(temp, npartitions = 1))
    df = df.compute()
    df.sort_values('date', ascending = True, inplace = True)
    df.index = df.date
    df.drop('date', axis = 1, inplace = True)
    return df


'''

def tingo_forex_intraday( currency_pair, api_token, start_date, end_date = None, freq = '1min' ):

    if end_date == None:
        end_date = dt.datetime.today().date().strftime('%Y-%m-%d')
    headers = {'Content-Type': 'application/json' }
    requestResponse = requests.get(f'https://api.tiingo.com/tiingo/fx/{currency_pair}/prices?&endDate={end_date}&resampleFreq=1min&token={api_token}', headers = headers)
    df = pd.DataFrame(requestResponse.json())
    df.date = pd.to_datetime(df.date)

    # iterate through latest dates to get more than the last 10000 rows
    last = df.copy()
    df = dd.from_pandas(df, npartitions = 1)
    while last.date.iloc[0].date() > pd.to_datetime(start_date):
        headers = {'Content-Type': 'application/json' }
        requestResponse = requests.get(f"https://api.tiingo.com/tiingo/fx/{currency_pair}/prices?endDate={(last.date.iloc[0]).date().strftime('%Y-%m-%d')}&resampleFreq={freq}&token={api_token}", headers=headers)
        try:
            temp = pd.DataFrame(requestResponse.json())
            temp.date = pd.to_datetime(temp.date)
            if last.iloc[0,0] == temp.iloc[0,0]:
                break
            last = temp.copy()
            df = df.append(dd.from_pandas(temp, npartitions = 1))
        except:
            last.date.iloc[0] -= dt.timedelta(1)
            headers = {'Content-Type': 'application/json' }
            requestResponse = requests.get(f"https://api.tiingo.com/tiingo/fx/{currency_pair}/prices?endDate={(last.date.iloc[0]).date().strftime('%Y-%m-%d')}&resampleFreq={freq}&token={api_token}", headers=headers)
            temp = pd.DataFrame(requestResponse.json())
            temp.date = pd.to_datetime(temp.date)
            if last.iloc[0,0] == temp.iloc[0,0]:
                break
            last = temp.copy()
            df = df.append(dd.from_pandas(temp, npartitions = 1))

    df = df.compute()
    df.sort_values('date', ascending = True, inplace = True)
    df.index = df.date
    df.drop('date', axis = 1, inplace = True)
    return df
'''

def iex_intraday(ticker, api_token, start_date = None, end_date = None):
    '''

    '''
    if end_date == None:
        date = dt.datetime.today()
    else:
        date = pd.to_datetime(end_date)

    if start_date == None:
        start_date = pd.to_datetime('2000-01-01')

    df = dd.from_pandas(get_historical_intraday(ticker, date, token = api_token, output_format = 'pandas'), npartitions = 1)

    e, i = 0, 0
    date = dt.datetime.today() - dt.timedelta(i)
    while e <= 5 and date > start_date:
        date = dt.datetime.today() - dt.timedelta(i)
        df2 = get_historical_intraday(ticker, date, token = api_token, output_format = 'pandas')
        if not df2.empty:
            df = df.append(dd.from_pandas(df2, npartitions = 1))
            time.sleep(.5)
            e = 0
        else:
            e += 1
        i += 1
    df.sort_index(ascending = True, inplace = True)
    return df


def yahoo_prices(ticker, start = None, end = None):
    '''

    '''
    if start == None:
        start = -2208988800

    if end == None:
        last_close = (dt.datetime.today() ).strftime("%Y-%m-%d")
        end = int(time.mktime(time.strptime(f'{last_close} 00:00:00', '%Y-%m-%d %H:%M:%S')))

    url = f'https://query2.finance.yahoo.com/v7/finance/download/{ticker}?period1={start}&period2={end}&interval=1d'
    r = requests.get(url).text
    df = pd.read_csv(StringIO(r))
    df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]
    df.index = pd.to_datetime(df.date, format = '%Y-%m-%d')
    df.drop('date', inplace = True, axis = 1)

    return df


def yahoo_option_chain( ticker ):
    '''

    '''
    url = f'https://query2.finance.yahoo.com/v7/finance/options/{ticker}?getAllData=True'
    r = requests.get(url).json()
    calls = []
    puts = []
    for o in r['optionChain']['result'][0]['options']:
        calls.append( pd.DataFrame( o['calls'] ) )
        puts.append( pd.DataFrame( o['puts'] ) )
    calls = pd.concat(calls)
    puts = pd.concat(puts)

    calls.columns = [ re.sub( r"([A-Z])", r"_\1", col).lower() for col in calls.columns ]
    puts.columns = [ re.sub( r"([A-Z])", r"_\1", col).lower() for col in puts.columns ]

    calls.expiration = pd.to_datetime( [ dt.datetime.fromtimestamp( x ).date() for x in calls.expiration ] )
    calls.last_trade_date = pd.to_datetime( [ dt.datetime.fromtimestamp( x ) for x in calls.last_trade_date ] )

    puts.expiration = pd.to_datetime( [ dt.datetime.fromtimestamp( x ).date() for x in puts.expiration ] )
    puts.last_trade_date = pd.to_datetime( [ dt.datetime.fromtimestamp( x ) for x in puts.last_trade_date ] )

    calls.reset_index(drop = True, inplace = True)
    puts.reset_index(drop = True, inplace = True)

    return calls, puts


def cboe_option_chain(ticker, head = False):

    db = DataBase()
    db.head = head
    url = 'http://www.cboe.com/delayedquote/quote-table-download'
    try:
        driver = db._load_driver(caps = 'none')
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="txtTicker"]')))
        driver.find_element_by_xpath('//input[@id="txtTicker"]').send_keys(ticker)
        driver.find_element_by_xpath('//input[@id="txtTicker"]').send_keys(Keys.ENTER)
        db.downloads_done('quotedata.dat')
        driver.quit()
    except:
        print('Failed to load data...')
        driver.quit()
        return None

    df = pd.read_csv(db.download_path + '/quotedata.dat', error_bad_lines=False, warn_bad_lines=False)
    underlying_price = float( df.columns[-2] )
    df = pd.read_csv(db.download_path + '/quotedata.dat', skiprows = [0,1,3], error_bad_lines=False, warn_bad_lines=False)
    df['underlying'] = underlying_price
    os.remove(db.download_path + '/quotedata.dat')

    df.columns = [ col.replace(' ', '_').lower().replace('_date', '') for col in df.columns ]
    puts = df.loc[:, ['expiration', 'puts' ] + [ col for col in df.columns if '.1' in col ] + [ 'strike', 'underlying' ] ]
    puts.columns = [ col.replace('.1', '') for col in puts.columns ]
    calls = df.loc[:, [ col for col in df.columns if '.1' not in col ] ]
    calls.drop('puts', inplace = True, axis = 1)

    return calls, puts
