
from  bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np
import datetime as dt

'''
    Functions:
        yahoo_valuation_metrics(ticker) ->
        yahoo_ratios(ticker) ->
        yahoo_all_statements(ticker) ->
        yahoo_balance_sheet(ticker) ->
        yahoo_income_statement(ticker) ->
        yahoo_cashflow_statement(ticker) ->

        # To do: add quarterly statements function with selenium
'''

def yahoo_valuation_metrics(ticker):
    '''

    '''
    session = HTMLSession()
    url = f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'
    r = session.get(url)
    soup = bs( r.content, "html.parser" )
    df = pd.read_html( str(soup.find('table')) )[0].transpose()
    df.reset_index(inplace = True)
    df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                    if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                        for c in df.iloc[0][1:].values.tolist()]
    df = df[1:]

    df = col_to_float(df)

    df.replace(',', '', regex = True, inplace = True)
    df.replace('-', np.nan, regex = True, inplace = True)

    df[df.columns[1:]] = df[df.columns[1:]].astype('float')
    df.replace('Current', '', regex = True, inplace = True) # replace as of date as well ?

    df['ticker'] = ticker
    return df


def yahoo_ratios(ticker):
    '''

    '''
    session = HTMLSession()
    url = f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'
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

    df = col_to_float(df)

    df['Date'] = dt.datetime.today().date()
    df['ticker'] = ticker
    return df


def yahoo_statement(ticker, url):
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

    df['ticker'] = ticker

    df.columns = [ col.replace(',','').replace('(','').replace(')','') \
                        .replace('&','and').replace('/','_').replace(' ', '_' )
                            for col in df.columns ]
    df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]

    return df


def yahoo_cashflow_statement(ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + "/cash-flow?p=" + ticker
    try:
        df = yahoo_statement(ticker, url)
    except:
        print(f'Ticker {ticker} may not be available.')
    return df


def yahoo_income_statement(ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + "/financials?p=" + ticker
    try:
        df = yahoo_statement(ticker, url)
    except:
        print(f'Ticker {ticker} may not be available.')
    return df


def yahoo_balance_sheet(ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + "/balance-sheet?p=" + ticker
    try:
        df = yahoo_statement(ticker, url)
    except:
        print(f'Ticker {ticker} may not be available.')
    return df


def yahoo_all_statements(ticker):
    '''

    '''
    incomeStatement = yahoo_income_statement(ticker)
    balanceSheet = yahoo_balance_sheet(ticker)
    cashflowStatement = yahoo_cashflow_statement(ticker)
    return incomeStatement, balanceSheet, cashflowStatement

def yahoo_earnings_estimate(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/analysis'
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

def yahoo_earnings_history(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/analysis'
    session = HTMLSession()
    r = session.get(url)
    soup = bs( r.content, "html.parser" )

    df = pd.read_html( str( soup.find_all('table')[2] ) )[0].transpose()
    df.reset_index(inplace = True)
    df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                    if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                        for c in df.iloc[0][1:].values.tolist()]
    df = df[1:]

    df = col_to_float(df)

    df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')

    df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
    return df

def yahoo_revenue_estimates(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/analysis'
    session = HTMLSession()
    r = session.get(url)
    soup = bs( r.content, "html.parser" )

    df = pd.read_html( str( soup.find_all('table')[1] ) )[0].transpose()
    df.reset_index(inplace = True)
    df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                    if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                        for c in df.iloc[0][1:].values.tolist()]
    df = df[1:]

    df = col_to_float(df)

    df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')

    df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
    return df

def yahoo_growth_estimates(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/analysis'
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
    df = col_to_float(df)
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
    df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
    return df

def yahoo_earnings_estimate_trends(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/analysis'
    session = HTMLSession()
    r = session.get(url)
    soup = bs( r.content, "html.parser" )

    df = pd.read_html( str( soup.find_all('table')[3] ) )[0].transpose()
    df.reset_index(inplace = True)
    df.columns = ['Date'] + [c[:-1].strip().replace(' ', '_').replace('/', '')
                    if c.strip()[-1].isdigit() else c.strip().replace(' ', '_').replace('/', '')
                        for c in df.iloc[0][1:].values.tolist()]
    df = df[1:]
    df = col_to_float(df)
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
    df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
    return df


def col_to_float(df):
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
        except:
            continue
    return df
