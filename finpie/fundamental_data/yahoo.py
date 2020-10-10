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

class YahooData( DataBase ):

    def __init__(self, ticker):
        DataBase.__init__(self)
        self.ticker = ticker

    def key_metrics(self):
        '''

        '''
        url = f'https://finance.yahoo.com/quote/{self.ticker}/key-statistics?p={self.ticker}'
        soup = self._get_session(url)
        df = pd.concat( [ pd.read_html( str(t) )[0].transpose()
                            for t in soup.find_all('table')[1:] ], axis = 1 )
        df.columns = df.iloc[0]
        df = df[1:]
        df.reset_index(inplace = True, drop = True)
        df.columns = [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip() \
                            .replace(' ', '_').replace('/', '')  for c in df.columns ]


        df['ticker'] = self.ticker
        df.replace(',', '', regex = True, inplace = True)
        df = self._col_to_float(df)

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        df.index = [pd.to_datetime(dt.datetime.today().date())]
        df.index.name = 'date'
        return df


    def _download(self, url):
        '''

        '''
        soup = self._get_session(url)
        tempDict = {}
        lineitems = soup.find_all('div', class_ = "D(tbr)")
        for l in lineitems:
            temp = l.find_all('div', class_ = 'Ta(c)')
            tempList = []
            for t in temp:
                tempList.append(t.text)
            tempDict[ l.find('div', class_ = 'Ta(start)').text ] = tempList
        cols = [ c.find('div', class_ = 'Ta(start)').text for c in lineitems ]
        df = pd.DataFrame(tempDict, columns = cols )
        df = df.loc[:,~df.columns.duplicated()]
        df.replace(',','', regex = True, inplace = True)
        df.replace('-', np.nan, inplace = True)

        df['ticker'] = self.ticker

        df.columns = [ col.replace(',','').replace('(','').replace(')','') \
                            .replace('&','and').replace('/','_').replace(' ', '_' )
                                for col in df.columns ]
        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        df.replace(',', '', regex = True, inplace = True)
        df = df[ df.breakdown != 'ttm' ]
        df.index = pd.to_datetime(df.breakdown)
        df.index.name = 'date'
        df.drop('breakdown', axis = 1, inplace = True)
        return self._col_to_float(df)


    def cashflow_statement(self):
        url = "https://finance.yahoo.com/quote/" + self.ticker + "/cash-flow?p=" + self.ticker
        try:
            df = self._download(url)
            return df
        except:
            print(f'Download failed. Ticker {self.ticker} may not be available.')



    def income_statement(self):
        url = "https://finance.yahoo.com/quote/" + self.ticker + "/financials?p=" + self.ticker
        try:
            df = self._download(url)
            return df
        except:
            print(f'Download failed. Ticker {self.ticker} may not be available.')



    def balance_sheet(self):
        url = "https://finance.yahoo.com/quote/" + self.ticker + "/balance-sheet?p=" + self.ticker
        try:
            df = self._download(url)
            return df
        except:
            print(f'Download failed. Ticker {self.ticker} may not be available.')



    def statements(self):
        '''

        '''
        incomeStatement = self.income_statement()
        balanceSheet = self.balance_sheet()
        cashflowStatement = self.cashflow_statement()
        return incomeStatement, balanceSheet, cashflowStatement

    def earnings_estimate(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        soup = self._get_session(url)

        df = pd.read_html( str( soup.find('table') ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['reference_date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]

        df = df[1:]
        df.iloc[:, 1:] = df.iloc[:, 1:]

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        df.replace(',', '', regex = True, inplace = True)
        df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]
        df.index = [pd.to_datetime( dt.datetime.today().date() )] * len(df)
        df.index.name = 'date'

        return self._col_to_float(df)

    def earnings_history(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        soup = self._get_session(url)

        df = pd.read_html( str( soup.find_all('table')[2] ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['reference_date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]
        df = df[1:]

        df.replace(',', '', regex = True, inplace = True)
        df = self._col_to_float(df)

        df.iloc[:, 1:] = df.iloc[:, 1:]

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]
        df.index = [pd.to_datetime( dt.datetime.today().date() )] * len(df)
        df.index.name = 'date'
        return df

    def revenue_estimates(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        soup = self._get_session(url)

        df = pd.read_html( str( soup.find_all('table')[1] ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['reference_date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]
        df = df[1:]

        df.replace(',', '', regex = True, inplace = True)
        df = self._col_to_float(df)

        df.iloc[:, 1:] = df.iloc[:, 1:]

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]
        df.index = [pd.to_datetime( dt.datetime.today().date() )] * len(df)
        df.index.name = 'date'
        return df

    def growth_estimates(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        soup = self._get_session(url)

        df = pd.read_html( str( soup.find_all('table')[-1] ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['reference_date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]

        df = df[1:]
        df = df.astype('str')
        df.replace(',', '', regex = True, inplace = True)

        df = self._col_to_float(df)
        df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')

        df = df.transpose()
        df.columns = df.iloc[0]
        df = df[1:]

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]
        df.index = [pd.to_datetime( dt.datetime.today().date() )] * len(df)
        df.index.name = 'date'
        return df

    def earnings_estimate_trends(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        soup = self._get_session(url)

        df = pd.read_html( str( soup.find_all('table')[3] ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['reference_date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]
        df = df[1:]
        df.replace(',', '', regex = True, inplace = True)
        df = self._col_to_float(df)
        df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]
        df.index = [pd.to_datetime( dt.datetime.today().date() )] * len(df)
        df.index.name = 'date'
        return df


    def esg_score(self):
      '''

      '''
      url = f'https://finance.yahoo.com/quote/{self.ticker}/sustainability?p={self.ticker}'
      soup = self._get_session(url)

      section = soup.find(attrs = {'data-test': 'qsp-sustainability'})
      df = pd.DataFrame( {
        'total_esg_risk_score': np.float(section.find('div', string = 'Total ESG Risk score').find_next('div').find_next('div').text),
        'risk_category': section.find('div', string = 'Total ESG Risk score').find_next('div').find_next('div').find_next('div').find_next('div').text,
        'risk_percentile': section.find('div', string = 'Total ESG Risk score').find_next('div').find_next('div').find_next('span').text.replace(' percentile', ''),
        'environment_risk_score': np.float(section.find('div', string = 'Environment Risk Score').find_next('div').find_next('div').text),
        'social_risk_score': np.float(section.find('div', string = 'Social Risk Score').find_next('div').find_next('div').text),
        'governance_risk_score': np.float(section.find('div', string = 'Governance Risk Score').find_next('div').find_next('div').text),
        #'controversy_level': np.float(section.find('span', string = 'Controversy Level').find_next('div', class_ = 'Mt(15px)').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').text),
        'ticker' : self.ticker }, index = [0] )
      df.index = [pd.to_datetime( dt.datetime.today().date() )]
      df.index.name = 'date'
      return df


    def corporate_governance_score(self):
      '''

      '''
      url = f'https://finance.yahoo.com/quote/{self.ticker}/profile?p={self.ticker}'
      soup = self._get_session(url)

      temp = { i.split(':')[0].replace('The pillar scores are', '').strip(): i.split(':')[1].replace('.', '').strip() for i in soup.find_all('section')[-1].find_all('span')[3].text.split(';')  }
      temp['quality_score'] = soup.find_all('section')[-1].find_all('span')[1].text.replace('.','')[-2:].strip()
      df = pd.DataFrame(temp, index = [0])
      df['ticker'] = self.ticker
      df['date'] = dt.datetime.today().date()
      df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]
      df.replace(',', '', regex = True, inplace = True)
      df = self._col_to_float(df)
      df.index = [pd.to_datetime( dt.datetime.today().date() )]
      df.index.name = 'date'
      return df


    def profile(self):
       url = f'https://finance.yahoo.com/quote/{self.ticker}/profile?p={self.ticker}'
       soup = self._get_session(url)

       try:
           no_of_employees = np.int( soup.find('span', string = 'Full Time Employees').find_next('span').text.replace(',', '') )
       except:
           no_of_employees = np.nan
       df = pd.DataFrame( { 'company_name': soup.find_all('section')[1].find('h3').text,
                            'sector': soup.find('span', string = 'Sector(s)').find_next('span').text,
                            'industry': soup.find('span', string = 'Industry').find_next('span').text,
                            'number_of_employees': no_of_employees,
                            'description': soup.find('h2', string = 'Description').find_next('p').text,
                            'ticker': self.ticker }, index = [0] )
       df.index = [pd.to_datetime( dt.datetime.today().date() )]
       df.index.name = 'date'
       return df


    def executives_info(self):
       '''

       '''
       url = f'https://finance.yahoo.com/quote/{self.ticker}/profile?p={self.ticker}'
       soup = self._get_session(url)

       df = pd.read_html( str( soup.find('table') ) )[0]
       df['Gender'] = [ 'male' if 'Mr.' in n else 'female' for n in df.Name ]
       df['Age_at_end_of_year'] = [ dt.datetime.today().year - np.int(y) for y in df['Year Born'] ]
       col = 'Pay'
       df[col] = df[col].astype('str')
       df.loc[df[col].str.contains('T'), col] = (df[col][df[col].str.contains('T')] \
                                              .replace('T', '', regex = True) \
                                              .astype('float') * 1000000000000).astype('str')
       df.loc[df[col].str.contains('B'), col] = (df[col][df[col].str.contains('B', case=True)] \
                                              .replace('B', '', regex = True) \
                                              .astype('float') * 1000000000).astype('str')
       df.loc[df[col].str.contains('M'), col] = (df[col][df[col].str.contains('M', case=True)] \
                                              .replace('M', '', regex = True) \
                                              .astype('float') * 1000000).astype('str')
       df.loc[df[col].str.contains('k'), col] = (df[col][df[col].str.contains('k', case=True)] \
                                              .replace('k', '', regex = True) \
                                              .astype('float') * 1000).astype('str')
       df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]
       df.index = [pd.to_datetime( dt.datetime.today().date() )] * len(df)
       df.index.name = 'date'
       return df



'''

def valuation_metrics(self):


    url = f'https://finance.yahoo.com/quote/{self.ticker}/key-statistics?p={self.ticker}'
    soup = self._get_session(url)
    df = pd.read_html( str(soup.find('table')) )[0].transpose()
    df.reset_index(inplace = True)
    df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                    if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                        for c in df.iloc[0][1:].values.tolist()]
    df = df[1:]

    df = self._col_to_float(df)

    df.replace(',', '', regex = True, inplace = True)
    df.replace('-', np.nan, regex = True, inplace = True)

    #df[df.columns[1:]] = df[df.columns[1:]].astype('float')
    df.replace('Current', '', regex = True, inplace = True) # replace as of date as well ?
    df.replace(',', '', regex = True, inplace = True)

    df['ticker'] = self.ticker

    df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]

    return self._col_to_float(df)

'''
