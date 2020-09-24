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
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession

def global_tickers():
    '''

    '''
    session = HTMLSession()
    url = 'https://www.gurufocus.com/stock_list.php?p=0&n=100'
    r = session.get(url)
    soup = bs(r.content, 'html5lib')
    max_page = int( [ i.text.split(' ')[-1].replace('(', '').replace(')', '') for i in soup.find('div', class_ = 'page_links').find_all('a') if 'LAST' in i.text ][0] )
    first = True
    for i in tqdm(range(max_page)):
        r = session.get(f'https://www.gurufocus.com/stock_list.php?p={i}&n=100')
        soup = bs(r.content, 'html5lib')
        if first:
            df = pd.read_html( str(soup.find_all('table')[1]) )[0]
            first = False
        else:
            df = df.append( pd.read_html( str(soup.find_all('table')[1]) )[0] )
    df = df.iloc[:,:3]
    df.drop('Price', inplace = True, axis = 1)
    df.drop_duplicates('Symbol', inplace = True)
    return df

def nasdaq_tickers():
    '''

    '''
    df1 = pd.read_csv('ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt', sep = '|', skipfooter = 1, engine = 'python')
    df1 = df1[df1['Test Issue'] != 'Y'].iloc[:,:2]
    df2 = pd.read_csv('ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt', sep = '|', skipfooter = 1, engine = 'python')
    df2 = df2[df2['Test Issue'] != 'Y'].iloc[:,:2]
    df2.columns = df1.columns
    df1 = df1.append(df2)
    df1.reset_index(inplace = True, drop = True)
    return df1



'''http://www.eoddata.com/stocklist/AMEX/B.htm
http://www.eoddata.com/stocklist/ASX/2.htm
http://www.eoddata.com/stocklist/CBOT/B.htm
http://www.eoddata.com/stocklist/CFE.htm
http://www.eoddata.com/stocklist/COMEX/G.htm
http://www.eoddata.com/stocklist/EUREX/D.htm
http://www.eoddata.com/stocklist/FOREX/C.htm
http://www.eoddata.com/stocklist/HKEX.htm
http://www.eoddata.com/stocklist/INDEX/B.htm
http://www.eoddata.com/stocklist/kcbt.htm
http://www.eoddata.com/stocklist/LIFFE/C.htm
http://www.eoddata.com/stocklist/LSE.htm
http://www.eoddata.com/stocklist/MGEX/I.htm
http://www.eoddata.com/stocklist/NASDAQ/B.htm
http://www.eoddata.com/stocklist/NYBOT/C.htm
http://www.eoddata.com/stocklist/NYSE/E.htm
http://www.eoddata.com/stocklist/OTCBB/D.htm
http://www.eoddata.com/stocklist/SGX/B.htm
http://www.eoddata.com/stocklist/TSX/G.htm
http://www.eoddata.com/stocklist/TSXV/G.htm
http://www.eoddata.com/stocklist/USMF/H.htm
http://www.eoddata.com/stocklist/WCE.htm


import string

dfs = []
chars = string.ascii_lowercase + ''.join( [ str(i) for i in range(0,10) ] )
for i in chars:
    url = f'http://www.eoddata.com/stocklist/AMEX/{i.upper()}.htm'
    session = HTMLSession()
    url = 'https://www.gurufocus.com/stock_list.php?p=0&n=100'
    r = session.get(url)
    soup = bs(r.content, 'html5lib')
    dfs.append( pd.read_html( str( soup.find('table', class_ = 'quotes') ) )



def exchange_symbols(exchange):
    pass'''
