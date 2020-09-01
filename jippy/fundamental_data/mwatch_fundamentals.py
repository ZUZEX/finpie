

from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np


def mwatch_download(ticker, sheet, freq = 'annual'):
    '''


    '''
    if freq == 'annual':
        url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials/{sheet}'
    elif freq == 'quarterly':
        url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials/{sheet}/quarter'
    else:
        print('Please specify annual or quartlery frequency.')
        return None
    session = HTMLSession()
    r = session.get(url)
    soup = bs(r.content, 'html5lib')
    df = pd.concat( [ pd.read_html(str(s))[0] for s in soup.find('div', class_ = 'financials').find_all('table') ] )
    df = df.astype(str)
    df.iloc[:,0][ df.iloc[:,0] == 'nan' ]= df[ df.iloc[:,0] == 'nan' ].iloc[:,-1]
    df = df.iloc[:,:-2]
    df = df.transpose()
    df.index.name = 'date'
    df.columns = df.iloc[0]
    df = df[1:]
    df.columns.name = ''
    df.replace('-', np.nan, regex = True, inplace = True)
    df.replace('\(', '-', regex = True, inplace = True)
    df.replace('\)', '', regex = True, inplace = True)
    # rename duplicate columns
    columns = pd.io.parsers.ParserBase({'names':df.columns})._maybe_dedup_names(df.columns)
    df.columns = [ str(col).replace('\xa0', ' ') for col in columns ]
    df = df.astype('str')
    for col in df.columns:
        try:
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
            df.loc[df[col].str.contains('%'), col] = (df[col][df[col].str.contains('%', case=True)] \
                                                    .replace('%', '', regex = True) \
                                                    .astype('float') / 100).astype('str')
        except:
            continue
    df.columns = [ col.replace(' ', '_').replace('/','_to_').replace('.', '').replace('&', 'and').lower() for col in df.columns ]
    return df.astype('float')


def mwatch_income_statement(ticker, freq = 'annual'):
    '''

    '''
    return mwatch_download(ticker, 'income', freq)


def mwatch_balance_sheet(ticker, freq = 'annual'):
    '''

    '''
    return mwatch_download(ticker, 'balance-sheet', freq)


def mwatch_cashflow_statement(ticker, freq = 'annual'):
    '''

    '''
    return mwatch_download(ticker, 'cash-flow', freq)

def mwatch_statements(ticker, freq = 'annual'):
    '''

    '''
    income_statement = mwatch_income_statement(ticker, freq)
    balance_sheet = mwatch_balance_sheet(ticker, freq)
    cashflow_statement = mwatch_cashflow_statement(ticker, freq)
    return income_statement, balance_sheet, cashflow_statement
