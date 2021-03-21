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
from finpie.base import DataBase

class MwatchData( DataBase ):

    def __init__(self, ticker, freq = 'A', countryCode = ''):
        DataBase.__init__(self)
        self.ticker = ticker
        self.countryCode = countryCode
        self.freq = freq

    def _download(self, sheet):
        '''

        '''
        if self.freq.lower() == 'annual' or self.freq.lower() == 'a':
            if self.countryCode != '':
                url = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/{sheet}?countrycode={self.countryCode}'
            else:
                url = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/{sheet}'
        elif self.freq.lower() == 'quarterly' or self.freq.lower() == 'q':
            if self.countryCode != '':
                url = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/{sheet}/quarter?countrycode={self.countryCode}'
            else:
                url = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/{sheet}/quarter'

        else:
            print('Please specify annual or quartlery frequency.')
            return None
        soup = self._get_session(url)
        df = pd.concat( [ pd.read_html(str(s.find('table')))[0] for s in soup.find_all('div', class_='financials') ] )
        df = df.astype(str)
        df.iloc[:,0][ df.iloc[:,0] == 'nan' ]= df[ df.iloc[:,0] == 'nan' ].iloc[:,-1]
        df = df.iloc[:,:-1]
        df = df.transpose()
        df.index.name = 'date'
        df.columns = df.iloc[0]
        df = df[1:]
        df.columns.name = ''
        if self.freq.lower() == 'quarterly' or self.freq.lower() == 'q':
            df.index = pd.to_datetime(df.index)
        df.replace('-', np.nan, inplace = True)
        df.replace('\(', '-', regex = True, inplace = True)
        df.replace('\)', '', regex = True, inplace = True)
        # rename duplicate columns
        columns = pd.io.parsers.ParserBase({'names':df.columns})._maybe_dedup_names(df.columns)
        df.columns = [ str(col).replace('\xa0', ' ') for col in columns ]
        df = df.astype('str')

        df.replace(',', '', regex = True, inplace = True)
        df.columns = [ col.split(' ', 1)[0].replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        return self._col_to_float( df )


    def income_statement(self):
        '''

        '''
        return self._download('income')


    def balance_sheet(self):
        '''

        '''
        return self._download('balance-sheet')


    def cashflow_statement(self):
        '''

        '''
        return self._download('cash-flow')

    def statements(self):
        '''

        '''
        income_statement = self.income_statement()
        balance_sheet = self.balance_sheet()
        cashflow_statement = self.cashflow_statement()
        return income_statement, balance_sheet, cashflow_statement
