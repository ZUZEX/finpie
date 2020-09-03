from  bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np
import datetime as dt


def yahoo_esg_data(ticker):
  '''

  '''
  session = HTMLSession()
  url = f'https://finance.yahoo.com/quote/{ticker}/sustainability?p={ticker}'
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
    'ticker' : ticker }, index = [0] )
  return df


def yahoo_corporate_governance_score(ticker):
  '''

  '''
  session = HTMLSession()
  url = f'https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}'
  r = session.get(url)
  soup = bs( r.content, "html.parser" )


  temp = { i.split(':')[0].replace('The pillar scores are', '').strip(): i.split(':')[1].replace('.', '').strip() for i in soup.find_all('section')[-1].find_all('span')[3].text.split(';')  }
  temp['quality_score'] = soup.find_all('section')[-1].find_all('span')[1].text.replace('.','')[-2:].strip()
  df = pd.DataFrame(temp, index = [0])
  df['ticker'] = ticker
  df['date'] = dt.datetime.today().date()
  df.columns = [ col.lower().replace(' ', '_') for col in df.columns ]

  return df
