
from  bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np
import datetime as dt

'''
    Functions:
        valuation_metrics(self.ticker) ->
        ratios(self.ticker) ->
        all_statements(self.ticker) ->
        balance_sheet(self.ticker) ->
        income_statement(self.ticker) ->
        cashflow_statement(self.ticker) ->

        # To do: add quarterly statements function with selenium
'''

class yahooData(object):

    def __init__(self, ticker):
        self.ticker = ticker

    def valuation_metrics(self):
        '''

        '''
        session = HTMLSession()
        url = f'https://finance.yahoo.com/quote/{self.ticker}/key-statistics?p={self.ticker}'
        r = session.get(url)
        soup = bs( r.content, "html.parser" )
        df = pd.read_html( str(soup.find('table')) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]
        df = df[1:]

        df = self._col_to_float(df)

        df.replace(',', '', regex = True, inplace = True)
        df.replace('-', np.nan, regex = True, inplace = True)

        df[df.columns[1:]] = df[df.columns[1:]].astype('float')
        df.replace('Current', '', regex = True, inplace = True) # replace as of date as well ?

        df['ticker'] = self.ticker

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]

        return df


    def ratios(self):
        '''

        '''
        session = HTMLSession()
        url = f'https://finance.yahoo.com/quote/{self.ticker}/key-statistics?p={self.ticker}'
        r = session.get(url)
        soup = bs( r.content, "html.parser" )
        df = pd.concat( [ pd.read_html( str(t) )[0].transpose()
                            for t in soup.find_all('table')[1:] ], axis = 1 )
        df.columns = df.iloc[0]
        df = df[1:]
        df.reset_index(inplace = True, drop = True)
        df.columns = [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip() \
                            .replace(' ', '_').replace('/', '')  for c in df.columns ]

        df = self._col_to_float(df)

        df['Date'] = dt.datetime.today().date()
        df['ticker'] = self.ticker

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        return df


    def _download(self, url):
        '''

        '''
        session = HTMLSession()
        r = session.get(url)
        soup = bs( r.content, "html.parser" )
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

        return df


    def cashflow_statement(self):
        url = "https://finance.yahoo.com/quote/" + self.ticker + "/cash-flow?p=" + self.ticker
        try:
            df = self._download(url)
        except:
            print(f'ticker {self.ticker} may not be available.')
        return df


    def income_statement(self):
        url = "https://finance.yahoo.com/quote/" + self.ticker + "/financials?p=" + self.ticker
        try:
            df = self._download(url)
        except:
            print(f'ticker {self.ticker} may not be available.')
        return df


    def balance_sheet(self):
        url = "https://finance.yahoo.com/quote/" + self.ticker + "/balance-sheet?p=" + self.ticker
        try:
            df = self._download(url)
        except:
            print(f'ticker {self.ticker} may not be available.')
        return df


    def statements(self):
        '''

        '''
        incomeStatement = self.income_statement(self.ticker)
        balanceSheet = self.balance_sheet(self.ticker)
        cashflowStatement = self.cashflow_statement(self.ticker)
        return incomeStatement, balanceSheet, cashflowStatement

    def earnings_estimate(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        session = HTMLSession()
        r = session.get(url)
        soup = bs( r.content, "html.parser" )

        df = pd.read_html( str( soup.find('table') ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]

        df = df[1:]
        df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]

        return df

    def earnings_history(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        session = HTMLSession()
        r = session.get(url)
        soup = bs( r.content, "html.parser" )

        df = pd.read_html( str( soup.find_all('table')[2] ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]
        df = df[1:]

        df = self._col_to_float(df)

        df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        return df

    def revenue_estimates(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        session = HTMLSession()
        r = session.get(url)
        soup = bs( r.content, "html.parser" )

        df = pd.read_html( str( soup.find_all('table')[1] ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]
        df = df[1:]

        df = self._col_to_float(df)

        df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        return df

    def growth_estimates(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        session = HTMLSession()
        r = session.get(url)
        soup = bs( r.content, "html.parser" )

        df = pd.read_html( str( soup.find_all('table')[-1] ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]

        df = df[1:]
        df = df.astype('str')
        df = self._col_to_float(df)
        df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')

        df = df.transpose()
        df.columns = df.iloc[0]
        df = df[1:]

        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        return df

    def earnings_estimate_trends(self):
        url = f'https://finance.yahoo.com/quote/{self.ticker}/analysis'
        session = HTMLSession()
        r = session.get(url)
        soup = bs( r.content, "html.parser" )

        df = pd.read_html( str( soup.find_all('table')[3] ) )[0].transpose()
        df.reset_index(inplace = True)
        df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                        if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                            for c in df.iloc[0][1:].values.tolist()]
        df = df[1:]
        df = self._col_to_float(df)
        df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        return df


    def _col_to_float(self, df):
        '''
        Converts string columns to floats replacing percentage signs and T, B, M, k
        to trillions, billions, millions and thousands.
        '''
        for col in df.columns:
            try:
                df.loc[df[col].str.contains('T'), col] = (df[col][df[col].str.contains('T')] \
                                                        .replace('T', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000000000).astype('str')
                df.loc[df[col].str.contains('B'), col] = (df[col][df[col].str.contains('B', case=True)] \
                                                        .replace('B', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000000).astype('str')
                df.loc[df[col].str.contains('M'), col] = (df[col][df[col].str.contains('M', case=True)] \
                                                        .replace('M', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000).astype('str')
                df.loc[df[col].str.contains('k'), col] = (df[col][df[col].str.contains('k', case=True)] \
                                                        .replace('k', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000).astype('str')
                df.loc[df[col].str.contains('%'), col] = (df[col][df[col].str.contains('%', case=True)] \
                                                        .replace('%', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') / 100).astype('str')
                df.loc[df[col].str.contains('K'), col] = (df[col][df[col].str.contains('K', case=True)] \
                                                     .replace('K', '', regex = True) \
                                                     .astype('float') * 1000).astype('str')
            except:
                continue
        return df



    def esg_score(self):
      '''

      '''
      session = HTMLSession()
      url = f'https://finance.yahoo.com/quote/{self.ticker}/sustainability?p={self.ticker}'
      r = session.get(url)
      soup = bs( r.content, "html.parser" )
      section = soup.find(attrs = {'data-test': 'qsp-sustainability'})
      df = pd.DataFrame( { 'date': dt.datetime.today().date(),
        'total_esg_risk_score': np.float(section.find('div', string = 'Total ESG Risk score').find_next('div').find_next('div').text),
        'risk_category': section.find('div', string = 'Total ESG Risk score').find_next('div').find_next('div').find_next('div').find_next('div').text,
        'risk_percentile': section.find('div', string = 'Total ESG Risk score').find_next('div').find_next('div').find_next('span').text.replace(' percentile', ''),
        'environment_risk_score': np.float(section.find('div', string = 'Environment Risk Score').find_next('div').find_next('div').text),
        'social_risk_score': np.float(section.find('div', string = 'Social Risk Score').find_next('div').find_next('div').text),
        'governance_risk_score': np.float(section.find('div', string = 'Governance Risk Score').find_next('div').find_next('div').text),
        'controversy_level': np.float(section.find('span', string = 'Controversy Level').find_next('div', class_ = 'Mt(15px)').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').text),
        'ticker' : self.ticker }, index = [0] )
      return df


    def corporate_governance_score(self):
      '''

      '''
      session = HTMLSession()
      url = f'https://finance.yahoo.com/quote/{self.ticker}/profile?p={self.ticker}'
      r = session.get(url)
      soup = bs( r.content, "html.parser" )

      temp = { i.split(':')[0].replace('The pillar scores are', '').strip(): i.split(':')[1].replace('.', '').strip() for i in soup.find_all('section')[-1].find_all('span')[3].text.split(';')  }
      temp['quality_score'] = soup.find_all('section')[-1].find_all('span')[1].text.replace('.','')[-2:].strip()
      df = pd.DataFrame(temp, index = [0])
      df['ticker'] = self.ticker
      df['date'] = dt.datetime.today().date()
      df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]

      return df


    def profile(self):
       session = HTMLSession()
       url = f'https://finance.yahoo.com/quote/{self.ticker}/profile?p={self.ticker}'
       r = session.get(url)
       soup = bs( r.content, "html.parser" )
       df = pd.DataFrame( { 'company_name': soup.find_all('section')[1].find('h3').text,
                            'sector': soup.find('span', string = 'Sector(s)').find_next('span').text,
                            'industry': soup.find('span', string = 'Industry').find_next('span').text,
                            'number_of_employees': np.int( soup.find('span', string = 'Full Time Employees').find_next('span').text.replace(',', '') ),
                            'description': soup.find('h2', string = 'Description').find_next('p').text,
                            'ticker': self.ticker }, index = [0] )
       return df

    def executives_info(self):
       '''

       '''
       session = HTMLSession()
       url = f'https://finance.yahoo.com/quote/{self.ticker}/profile?p={self.ticker}'
       r = session.get(url)
       soup = bs( r.content, "html.parser" )

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
       return df
