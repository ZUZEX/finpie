

import pandas as pd
import numpy as np
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import dask.dataframe as dd
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm


def get_futures_prices(date):
    '''
    input: datetime object
    output: pandas dataframe with prices for all available futures for the
            specified date
    '''
    errors = []
    y = str(date.year)
    if len(str(date.month)) == 2:
        m = str(date.month)
    else:
        m = '0' + str(date.month)
    if len(str(date.day)) == 2:
        d = str(date.day)
    else:
        d = '0' + str(date.day)
    try:
        session = HTMLSession()
        url = f'https://www.mrci.com/ohlc/{y}/{y[-2:]+m+d}.php'
        r = session.get(url)
        soup = bs(r.content, 'html5lib')
        df = pd.read_html( str(soup.find('map').find_next('table')) )[0]
        futures_lookup = pd.read_csv('futures_lookup.csv').name.tolist()
        indices = [ i for i, j in enumerate(df.iloc[:,0]) if j in futures_lookup ]
        columns = ['month', 'date', 'open', 'high', 'low', 'close', 'change', 'volume', 'open_interest', 'change_in_oi' ]
        if len(df.columns) == 11:
            df = df.iloc[indices[0]:-2, :len(df.columns)-1]
        else:
            df = df.iloc[indices[0]:-2, :]
    except:
        errors.append(date)
        return errors
    df.columns = columns
    #[ i for i in np.unique(df.month).tolist() if i not in futures_lookup ]

    first = True
    for i in range(1, len(indices)):
        temp = df.loc[indices[i-1]+1:indices[i]-2].copy()
        temp['future'] = df.loc[indices[i-1], 'month']
        if first:
            out = temp.copy()
            first = False
        else:
            out = out.append(temp)
    out = out[ out.iloc[:,1] != 'Total Volume and Open Interest']
    out.to_csv('futures.csv')
    out.index = [date] * len(out) #pd.to_datetime( [ f'{i[-2:]}/{i[2:4]}/{i[:2]}' for i in out.date ] )
    out.replace('\+', '', regex = True, inplace = True)
    out.replace('unch', np.nan, inplace = True)

    return dd.from_pandas(out, npartitions = 1)


def futures_historical_prices(date_range):
    '''
        Function to retrieve historical futures prices of all available futures contracts,
        including currency, interest rate, energy, meat, metals, softs, grains, soybeans,
        fiber and index futures.

        Notice that the download is not very fast and 20 years of data takes around 2 hours
        to download and contains around 2 million rows.

        input: pandas date range, e.g. pd.date_range('2000-01-01', '2020-01-01')
        output: pandas dataframe with prices for all available futures for the
                specified time period
    '''
    with ThreadPoolExecutor(4) as pool:
        res = list( tqdm( pool.map(get_futures_prices, date_range), total = len(date_range) ))
    df_out = dd.concat( [ i for i in res if type(i) != type([0]) ], axis = 0 )
    df_out = df_out.compute()
    return df_out
