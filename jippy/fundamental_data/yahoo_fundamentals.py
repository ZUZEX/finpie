
from  bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np
import datetime as dt

'''
    Functions:
        get_valuation_metrics(ticker) ->
        get_ratios(ticker) ->
        get_all_statements(ticker) ->
        get_balance_sheet(ticker) ->
        get_income_statement(ticker) ->
        get_cashflow_statement(ticker) ->

        # To do: add quarterly statements function with selenium
'''

def get_valuation_metrics(ticker):
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
    for col in df.columns:
        df[col][df[col].str.contains('T')] = (df[col][df[col].str.contains('T')] \
                                                .replace('T', '', regex = True) \
                                                .astype('float') * 1000000000000).astype('str')
        df[col][df[col].str.contains('B')] = (df[col][df[col].str.contains('B', case=True)] \
                                                .replace('B', '', regex = True) \
                                                .astype('float') * 1000000000).astype('str')
        df[col][df[col].str.contains('M')] = (df[col][df[col].str.contains('T', case=True)] \
                                                .replace('T', '', regex = True) \
                                                .astype('float') * 1000000).astype('str')
        df[col][df[col].str.contains('K')] = (df[col][df[col].str.contains('T', case=True)] \
                                                .replace('T', '', regex = True) \
                                                .astype('float') * 1000).astype('str')
    df.replace(',', '', regex = True, inplace = True)
    df.replace('-', np.nan, regex = True, inplace = True)

    df[df.columns[1:]] = df[df.columns[1:]].astype('float')
    df.replace('Current', '', regex = True, inplace = True) # replace as of date as well ?

    df['Ticker'] = ticker
    return df


def get_ratios(ticker):
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

    for col in df.columns:
        try:
            df[col][df[col].str.contains('T')] = (df[col][df[col].str.contains('T')] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000000000).astype('str')
            df[col][df[col].str.contains('B')] = (df[col][df[col].str.contains('B', case=True)] \
                                                    .replace('B', '', regex = True) \
                                                    .astype('float') * 1000000000).astype('str')
            df[col][df[col].str.contains('M')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000).astype('str')
            df[col][df[col].str.contains('K')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000).astype('str')
            df[col][df[col].str.contains('%')] = (df[col][df[col].str.contains('%', case=True)] \
                                                    .replace('%', '', regex = True) \
                                                    .astype('float') / 100).astype('str')
        except:
            continue
    df['Date'] = dt.datetime.today().date()
    df['Ticker'] = ticker
    return df


def get_statement(ticker, url):
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
    df.columns = [ col.replace(',','').replace('(','').replace(')','') \
                    .replace('&','and').replace('/','_').replace(' ', '_' )
                        for col in df.columns ]
    df['Ticker'] = ticker

    return df


def get_cashflow_statement(ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + "/cash-flow?p=" + ticker
    try:
        df = get_statement(ticker, url)
    except:
        print(f'Ticker {ticker} may not be available.')
    return df


def get_income_statement(ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + "/financials?p=" + ticker
    try:
        df = get_statement(ticker, url)
    except:
        print(f'Ticker {ticker} may not be available.')
    return df


def get_balance_sheet(ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + "/balance-sheet?p=" + ticker
    try:
        df = get_statement(ticker, url)
    except:
        print(f'Ticker {ticker} may not be available.')
    return df


def get_all_statements(ticker):
    '''

    '''
    incomeStatement = get_income_statement(ticker)
    balanceSheet = get_balance_sheet(ticker)
    cashflowStatement = get_cashflow_statement(ticker)
    return incomeStatement, balanceSheet, cashflowStatement

def get_earnings_estimate(ticker):
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

    return df

def get_earnings_history(ticker):
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
    for col in df.columns:
        try:
            df[col][df[col].str.contains('T')] = (df[col][df[col].str.contains('T')] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000000000).astype('str')
            df[col][df[col].str.contains('B')] = (df[col][df[col].str.contains('B', case=True)] \
                                                    .replace('B', '', regex = True) \
                                                    .astype('float') * 1000000000).astype('str')
            df[col][df[col].str.contains('M')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000).astype('str')
            df[col][df[col].str.contains('K')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000).astype('str')
            df[col][df[col].str.contains('%')] = (df[col][df[col].str.contains('%', case=True)] \
                                                    .replace('%', '', regex = True) \
                                                    .astype('float') / 100).astype('str')
        except:
            continue
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
    return df

def get_revenue_estimates(ticker):
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

    for col in df.columns:
        try:
            df[col][df[col].str.contains('T')] = (df[col][df[col].str.contains('T')] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000000000).astype('str')
            df[col][df[col].str.contains('B')] = (df[col][df[col].str.contains('B', case=True)] \
                                                    .replace('B', '', regex = True) \
                                                    .astype('float') * 1000000000).astype('str')
            df[col][df[col].str.contains('M')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000).astype('str')
            df[col][df[col].str.contains('K')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000).astype('str')
            df[col][df[col].str.contains('%')] = (df[col][df[col].str.contains('%', case=True)] \
                                                    .replace('%', '', regex = True) \
                                                    .astype('float') / 100).astype('str')
        except:
            continue
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
    return df

def get_growth_estimates(ticker):
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
    for col in df.columns:
        try:
            df[col][df[col].str.contains('T')] = (df[col][df[col].str.contains('T')] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000000000).astype('str')
            df[col][df[col].str.contains('B')] = (df[col][df[col].str.contains('B', case=True)] \
                                                    .replace('B', '', regex = True) \
                                                    .astype('float') * 1000000000).astype('str')
            df[col][df[col].str.contains('M')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000).astype('str')
            df[col][df[col].str.contains('K')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000).astype('str')
            df[col][df[col].str.contains('%')] = (df[col][df[col].str.contains('%', case=True)] \
                                                    .replace('%', '', regex = True) \
                                                    .astype('float') / 100).astype('str')
        except:
            continue
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
    return df

def get_earnings_estimate_trends(ticker):
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
    for col in df.columns:
        try:
            df[col][df[col].str.contains('T')] = (df[col][df[col].str.contains('T')] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000000000).astype('str')
            df[col][df[col].str.contains('B')] = (df[col][df[col].str.contains('B', case=True)] \
                                                    .replace('B', '', regex = True) \
                                                    .astype('float') * 1000000000).astype('str')
            df[col][df[col].str.contains('M')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000000).astype('str')
            df[col][df[col].str.contains('K')] = (df[col][df[col].str.contains('T', case=True)] \
                                                    .replace('T', '', regex = True) \
                                                    .astype('float') * 1000).astype('str')
            df[col][df[col].str.contains('%')] = (df[col][df[col].str.contains('%', case=True)] \
                                                    .replace('%', '', regex = True) \
                                                    .astype('float') / 100).astype('str')
        except:
            continue
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
    return df
