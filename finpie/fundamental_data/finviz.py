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

import numpy as np
import pandas as pd
import datetime as dt
from finpie.base import DataBase

class FinvizData(DataBase):

    def __init__( self, ticker ):
        self.ticker = ticker

    def insider_transactions( self ):
        '''

        '''
        # to do: format date
        url = f'https://finviz.com/quote.ashx?t={self.ticker}&ty=c&ta=1&p=d'
        soup = self._get_session(url)
        df = pd.read_html( str( soup.find_all('table')[-2] ) )[0]
        df.columns = df.iloc[0]
        df = df[1:]
        df.reset_index(inplace = True, drop = True)
        df.columns = [ col.replace(' ', '_').replace('/','_to_').replace('.', '').replace('&', 'and').lower() for col in df.columns ]
        df.index = [pd.to_datetime( dt.datetime.today().date() )] * len(df)
        df.index.name = 'date'
        return df


    def analyst_ratings( self ):
        '''

        '''
        url = f'https://finviz.com/quote.ashx?t={self.ticker}&ty=c&ta=1&p=d'
        soup = self._get_session(url)
        df = pd.read_html( str( soup.find('table', class_ = 'fullview-ratings-outer') )) [0]
        df.dropna(inplace = True)
        df.columns = ['date', 'action', 'rating_institution', 'rating', 'price_target']
        df.index = pd.to_datetime(df.date)
        df.drop('date', inplace = True, axis = 1)
        df.columns = [ col.replace(' ', '_').replace('/','_to_').replace('.', '').replace('&', 'and').lower() for col in df.columns ]
        df.index = [pd.to_datetime( dt.datetime.today().date() )] * len(df)
        df.index.name = 'date'
        return df


    def key_metrics( self ):
        '''

        '''
        url = f'https://finviz.com/quote.ashx?t={self.ticker}'
        soup = self._get_session(url)
        df = pd.read_html( str( soup.find('table', class_ = 'snapshot-table2') ) )[0]
        columns = list( range(0,len(df.columns), 2) )
        values = list( range(1,len(df.columns), 2) )
        columns = np.array( [ df[i].values for i in columns ] ).flatten().tolist()
        values = np.array( [ df[i].values for i in values ] ).flatten()
        df = pd.DataFrame( values.reshape(1,-1), columns = columns, index = [0])
        df.columns = [ col.replace(' ', '_').replace('/','_to_').replace('.', '').replace('&', 'and').lower() for col in df.columns ]
        df.index = [ pd.to_datetime(dt.datetime.today().date()) ]
        df.index.name = 'date'
        return self._col_to_float(df)

    
