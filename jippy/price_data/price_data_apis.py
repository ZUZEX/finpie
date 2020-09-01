
import pandas as pd
import numpy as np
import quandl
from alpha_vantage.timeseries import TimeSeries
import quandl

def get_alpha_vantage_ts(ticker, api_key):
      # load data
      try:
            ts               =  TimeSeries(key = api_key, output_format = 'pandas')
      except:
            print('Please specify your API key.')
      data, meta_data  =  ts.get_daily_adjusted(symbol = ticker, outputsize = 'full' )
      columns          =  ['Open', 'High', 'Low', 'Close', 'Adjusted_Close', 'Volume', 'Dividend_Amount', 'Split_Coefficient' ]
      data.columns     =  columns
      data.reset_index(level=0, inplace=True)
      data['Close']       = pd.to_numeric( data.Close )
      data['Open']        = pd.to_numeric( data.Open )
      data['High']        = pd.to_numeric( data.High )
      data['Low']         = pd.to_numeric( data.Low )
      data['Date']        = pd.to_datetime(data.date)
      data.sort_values('date', ascending = True, inplace = True)
      data.reset_index(drop = True, inplace = True)

      for col in ['Open', 'High', 'Low', 'Close']:
          data[col] = data[col] * data['Adjusted_Close'] / data['Close']
      data.index = pd.to_datetime( data.date )

      return data

def get_quandl(self):
  pass
