

from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np

from jippy.fundamental_data.fundamental_base import Fundamental


class finvizData(Fundamental):

    def __init__(self, ticker):
        self.ticker = ticker

    def insider_transactions(self):
        '''

        '''
        # to do: format date
        url = f'https://finviz.com/quote.ashx?t={self.ticker}&ty=c&ta=1&p=d'
        session = HTMLSession()
        r = session.get(url)
        soup = bs(r.content, 'html5lib')
        df = pd.read_html( str( soup.find_all('table')[-2] ) )[0]
        df.columns = df.iloc[0]
        df = df[1:]
        df.reset_index(inplace = True, drop = True)
        df.columns = [ col.replace(' ', '_').replace('/','_to_').replace('.', '').replace('&', 'and').lower() for col in df.columns ]
        return df


    def analyst_ratings(self):
        '''

        '''
        url = f'https://finviz.com/quote.ashx?t={self.ticker}&ty=c&ta=1&p=d'
        session = HTMLSession()
        r = session.get(url)
        soup = bs(r.content, 'html5lib')
        df = pd.read_html( str( soup.find('table', class_ = 'fullview-ratings-outer') )) [0]
        df.dropna(inplace = True)
        df.columns = ['date', 'action', 'rating_institution', 'rating', 'price_target']
        df.index = pd.to_datetime(df.date)
        df.drop('date', inplace = True, axis = 1)
        df.columns = [ col.replace(' ', '_').replace('/','_to_').replace('.', '').replace('&', 'and').lower() for col in df.columns ]
        return df

    def key_metrics( self ):

        url = f'https://finviz.com/quote.ashx?t={self.ticker}'
        session = HTMLSession()
        r = session.get(url)
        soup = bs(r.content, 'html5lib')
        df = pd.read_html( str( soup.find('table', class_ = 'snapshot-table2') ) )[0]
        columns = list( range(0,len(df.columns), 2) )
        values = list( range(1,len(df.columns), 2) )
        columns = np.array( [ df[i].values for i in columns ] ).flatten().tolist()
        values = np.array( [ df[i].values for i in values ] ).flatten()
        df = pd.DataFrame( values.reshape(1,-1), columns = columns, index = [0])
        df.columns = [ col.replace(' ', '_').replace('/','_to_').replace('.', '').replace('&', 'and').lower() for col in df.columns ]
        return self._col_to_float(df)
