
from  bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np
import datetime as dt


def get_profile(ticker):
   session = HTMLSession()
   url = f'https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}'
   r = session.get(url)
   soup = bs( r.content, "html.parser" )
   df = pd.DataFrame( { 'company_name': soup.find_all('section')[1].find('h3').text,
                        'sector': soup.find('span', string = 'Sector(s)').find_next('span').text,
                        'industry': soup.find('span', string = 'Industry').find_next('span').text,
                        'number_of_employees': np.int( soup.find('span', string = 'Full Time Employees').find_next('span').text.replace(',', '') ),
                        'description': soup.find('h2', string = 'Description').find_next('p').text,
                        'ticker': ticker }, index = [0] )
   return df


def get_executives_info(ticker):
   '''

   '''
   session = HTMLSession()
   url = f'https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}'
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
