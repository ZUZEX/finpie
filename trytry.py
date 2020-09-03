
import pandas as pd
import requests
import dask.dataframe as dd

def tingo_prices( ticker, api_token, start_date, end_date, freq = '5min'):
    '''

    Example date format = '2000-01-01'

    '''
    headers = {'Content-Type': 'application/json' }
    requestResponse = requests.get(f"https://api.tiingo.com/iex/{ticker}/prices?startDate={start_date}&endDate={end_date}&resampleFreq={freq}&token={api_token}", headers=headers)
    df = pd.DataFrame(requestResponse.json())
    df.date = pd.to_datetime(df.date)

    # iterate through dates to get more than the last 10000 rows
    last = df.copy()
    df = dd.from_pandas(df, npartitions = 1)
    while last.date.iloc[0].date() > pd.to_datetime(start_date):
        headers = {'Content-Type': 'application/json' }
        requestResponse = requests.get(f"https://api.tiingo.com/iex/{ticker}/prices?startDate={start_date}&endDate={ last.date.iloc[0].date().strftime('%Y-%m-%d')}&resampleFreq={freq}&token={api_token}", headers=headers)
        temp = pd.DataFrame(requestResponse.json())
        temp.date = pd.to_datetime(temp.date)
        if last.iloc[0,0] == temp.iloc[0,0]:
            break
        last = temp.copy()
        df = df.append(dd.from_pandas(temp, npartitions = 1))
    df = df.compute()
    df.sort_values('date', ascending = True, inplace = True)
    df.index = df.date
    df.drop('date', axis = 1, inplace = True)
    return df


api_token = '35f2f6d0cbe2206fdfaebbc0c8d76dd81ac76f38'


date_range = pd.date_range('2018-01-01', '2020-01-01')

len(date_range)


start_date = '2019-01-01'
ticker = 'aapl'
freq = '1min'

df = tingo_prices(ticker, api_token, start_date = start_date, end_date = '2020-01-01', freq = freq)

df



df = df.compute()
df.sort_values('date', ascending = True, inplace = True)

df
df['dateform'] = [d.date() for d in pd.to_datetime(df.date)]

80 * 5 / 60


'1min' = 400
'5min' = 80
'10min' = 40
'15min' = 30


df.groupby('dateform').count()

headers = {'Content-Type': 'application/json' }
requestResponse = requests.get(f"https://api.tiingo.com/iex/aapl/prices?startDate={start_date}&resampleFreq={freq}&token={api_token}", headers=headers)
df = pd.DataFrame(requestResponse.json())

df


import matplotlib.pyplot as plt

plt.plot( df.close )



requestResponse = requests.get("https://api.tiingo.com/iex/aapl/prices?startDate=2019-01-02&resampleFreq=5min&token={}".format(api_token), headers=headers)
df2 = pd.DataFrame(requestResponse.json())



requestResponse = requests.get("https://api.tiingo.com/iex/aapl/prices?startDate=2010-01-01&resampleFreq=15min&token={}".format(api_token), headers=headers)
df3 = pd.DataFrame(requestResponse.json())


requestResponse = requests.get("https://api.tiingo.com/iex/aapl/prices?startDate=2010-01-01&resampleFreq=30min&token={}".format(api_token), headers=headers)
df4 = pd.DataFrame(requestResponse.json())


df4


requestResponse = requests.get("https://api.tiingo.com/iex/aapl/prices?startDate=2010-01-01&resampleFreq=60min&token={}".format(api_token), headers=headers)
df5 = pd.DataFrame(requestResponse.json())


df5


import pandas as pd
import requests
from pyspark.sql import SparkSession
import findspark
findspark.init('/usr/local/Cellar/apache-spark/2.4.3/libexec')

api_token = '35f2f6d0cbe2206fdfaebbc0c8d76dd81ac76f38'
path = '/Users/PeterlaCour/Documents/Research.nosync/Trading_algorithms/pead/database/tiingo/'

ticker = 'spy'
frequencies = [ '1min', '5min', '10min', '15min', '30min', '60min', 'daily' ]
frequencies = [  '120min' ]
freq = 'Daily'
headers = {'Content-Type': 'application/json' }
#spark = SparkSession.builder.getOrCreate()
for freq in frequencies:
    if freq == 'daily':
        requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/{}/prices?startDate=2000-1-1&token={}".format( ticker, api_token), headers = headers)
        df = pd.DataFrame(requestResponse.json())
    else:
        requestResponse = requests.get("https://api.tiingo.com/iex/{}/prices?startDate=2010-01-01&resampleFreq={}&token={}".format( ticker, freq, api_token), headers = headers)
        df = pd.DataFrame(requestResponse.json())
    #spark.createDataFrame(df).write.mode('append').parquet( path + 'ticker={}/freq={}'.format(ticker, freq), compression = 'gzip')
#spark.stop()

df






# iex cloud
import time
import pandas as pd
import datetime as dt
from pyspark.sql import SparkSession
import findspark
import tqdm as tqdm
findspark.init('/usr/local/Cellar/apache-spark/2.4.3/libexec')
from iexfinance.stocks import get_historical_intraday



In [11]: df = get_historical_data("TSLA", start, end, output_format='pandas')


path = '/Users/PeterlaCour/Documents/Research.nosync/Trading_algorithms/pead/database/iex_cloud_intraday/'
iex_token = 'sk_4ea16e619eec4364bf683c0a6c2aff6e'

date = dt.datetime.today()
df = get_historical_intraday(ticker, date, token = iex_token, output_format = 'pandas')

df


start_date
c = 0
e = 0
i = 0
while e <= 5 and (dt.datetime.today() - dt.timedelta(i)) > start_date:
    date = dt.datetime.today() - dt.timedelta(i)
    df2 = get_historical_intraday(ticker, date, token = iex_token, output_format = 'pandas')
    if not df2.empty:
        df = df.append(df2)
        c = i
        time.sleep(1)
        e = 0
    else:
        e += 1
    i += 1
print(c)

def iex_intraday(ticker, api_token):
    '''

    '''
    date = dt.datetime.today()
    df = dd.from_pandas(get_historical_intraday(ticker, date, token = api_token, output_format = 'pandas'), npartitions = 1)
    start_date = pd.to_datetime('2019-01-01')
    e, i = 0, 0
    date = dt.datetime.today() - dt.timedelta(i)
    while e <= 5 and date > start_date:
        date = dt.datetime.today() - dt.timedelta(i)
        df2 = get_historical_intraday(ticker, date, token = iex_token, output_format = 'pandas')
        if not df2.empty:
            df = df.append(dd.from_pandas(df2, npartitions = 1))
            time.sleep(.5)
            e = 0
        else:
            e += 1
            print(e)
        i += 1
    return df



print(c)
df = df.compute()
df.sort_values('date',inplace = True)
df.head(5).to_markdown()


get_historical_intraday


# 393
# df

spark = SparkSession.builder.getOrCreate()
spark.createDataFrame(df).write.mode('append').parquet( path + 'ticker={}'.format(ticker), compression = 'gzip')
spark.stop()





'''


# options
# List of Expiration Dates
# To obtain a list of all options expiration dates for a symbol, simply call get_eod_options with a symbol only:

from iexfinance.stocks import get_eod_options

get_eod_options( "AAPL", output_format='pandas', token = iex_token ).head()

Out[2]:
        0
0  204588
1  208108
2  205746
3  210357
4  205449
Options For A Single Date
To obtain the end-of-day prices of options contracts for a single expiration date (in the form YYYYMM):

get_eod_options("AAPL", "202010", 'calls', token = iex_token)

Calls/Puts Only
It is possible to limit option results to calls or puts only:

get_eod_options("AAPL", "202010", "calls", token = iex_token)
or:

get_eod_options("AAPL", "201906", "puts")



'https://cloud.iexapis.com/stable/stock/aapl/quote?token=YOUR_TOKEN_HERE'




The /tops/last endpoint without any parameters will return all symbols.

DEEP
DEEP is IEX’s aggregated real-time depth of book quotes. DEEP also provides last trade price and size information.

Access is available through the function get_deep():

iexfinance.iexdata.get_deep(symbols=None, **kwargs)
DEEP data for a symbol or list of symbols

DEEP is used to receive real-time depth of book quotations direct from IEX. The depth of book quotations received via DEEP provide an aggregated size of resting displayed orders at a price and side, and do not indicate the size or number of individual orders at any price level. Non-displayed orders and non-displayed portions of reserve orders are not represented in DEEP.

DEEP also provides last trade price and size information. Trades resulting from either displayed or non-displayed orders matching on IEX will be reported. Routed executions will not be reported.

Reference: https://iexcloud.io/docs/api/#deep Data Weighting: Free

Parameters:
symbols (str or list, default None) – A symbol or list of symbols
kwargs – Additional Request Parameters (see base class)
Notes

Pandas not supported as an output format for the DEEP endpoint.

Note

Per IEX, DEEP only accepts one symbol at this time.

Usage
from iexfinance.iexdata import get_deep

get_deep("AAPL")[:2]



TOPS
TOPS is IEX’s aggregated best quoted bid and offer position in near real time.

Access is available through the function get_tops():

iexfinance.iexdata.get_tops(symbols=None, **kwargs)
TOPS data for a symbol or list of symbols.

TOPS provides IEX’s aggregated best quoted bid and offer position in near real time for all securities on IEX’s displayed limit order book. TOPS is ideal for developers needing both quote and trade data.
