

from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import pandas as pd
from tqdm import tqdm

def global_tickers():
    '''

    '''
    session = HTMLSession()
    url = 'https://www.gurufocus.com/stock_list.php?p=0&n=100'
    r = session.get(url)
    soup = bs(r.content, 'html5lib')
    max_page = int( [ i.text.split(' ')[-1].replace('(', '').replace(')', '') for i in soup.find('div', class_ = 'page_links').find_all('a') if 'LAST' in i.text ][0] )
    first = True
    for i in tqdm(range(max_page)):
        r = session.get(f'https://www.gurufocus.com/stock_list.php?p={i}&n=100')
        soup = bs(r.content, 'html5lib')
        if first:
            df = pd.read_html( str(soup.find_all('table')[1]) )[0]
            first = False
        else:
            df = df.append( pd.read_html( str(soup.find_all('table')[1]) )[0] )
    df = df.iloc[:,:3]
    return df

def nasdaq_tickers():
    '''

    '''
    df1 = pd.read_csv('ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt', sep = '|', skipfooter = 1)
    df1 = df1[df1['Test Issue'] != 'Y'].iloc[:,:2]
    df2 = pd.read_csv('ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt', sep = '|', skipfooter = 1)
    df2 = df2[df2['Test Issue'] != 'Y'].iloc[:,:2]
    df2.columns = df1.columns
    df1 = df1.append(df2)
    df1.reset_index(inplace = True, drop = True)
    return df1
