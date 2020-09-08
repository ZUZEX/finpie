

from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np


class finvizData(object):

    def __init__(self, ticker):
        self.ticker = ticker

    def finviz_insider_transactions(self):
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


    def finviz_analyst_ratings(self):
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
