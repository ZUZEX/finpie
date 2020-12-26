
import pandas as pd
import warnings
import unittest
import time
import finpie

class CommonTest(object):

    def __init__(self):
        # test ticker
        self.ticker = 'AAPL'
        self.date = '2020-12-03'
        self.date2 = '2020-12-11'

    def df_helper(self, data):
        # simple test to see if dataframe is returned

        # check output
        self.assertTrue( type(data) == type( pd.DataFrame() ) )
        # check dataframe length
        self.assertTrue( len(data) > 0 )

    # def test_tingo_prices(self)

    # def test_iex_intraday_prices(self)

    # def test_alpha_vantage_prices(self)


class FundamentalDataTest(unittest.TestCase, CommonTest):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        CommonTest.__init__(self)

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def class_test( self, cl, name ):

        for func in dir(cl):
            if callable(getattr(cl, func)) and '_' != func[0]:
                print( f'Testing {name} {func}' )
                data = getattr(cl, func)()
                if type( data ) == type((1,1)):
                    for d in data:
                        self.df_helper(d)
                else:
                    self.df_helper(data)
                print( 'Test passed. \n')
            time.sleep(1)

    def test_finviz(self):

        finviz = finpie.fundamental_data.FinvizData(self.ticker)
        self.class_test(finviz, 'Finviz fundamentals')

    def test_yahoo(self):

        yahoo = finpie.fundamental_data.YahooData(self.ticker)
        self.class_test(yahoo, 'Yahoo fundamentals')

    def test_mwatch(self):

        mwatch = finpie.fundamental_data.MwatchData(self.ticker)
        self.class_test(mwatch, 'Marketwatch fundamentals')

    def test_macrotrends(self):

        mt = finpie.fundamental_data.MacrotrendsData(self.ticker)
        self.class_test(mt, 'Macrotrends fundamentals')


    def test_earnings_call_transcripts(self):

        e = finpie.fundamental_data.Earnings(self.ticker)

        self.class_test(e, 'Motley Fool Earnings Calls')

class PriceDataTest(unittest.TestCase, CommonTest):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        CommonTest.__init__(self)

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_yahoo_prices(self):

        print('Testing Yahoo price data.')

        data = finpie.historical_prices(self.ticker)
        self.df_helper(data)
        # check columns
        self.assertTrue( list(data.columns) == ['open', 'high', 'low', 'close', 'adj_close', 'volume'] )
        # check data type
        self.assertTrue( any(data.dtypes == 'float') )
        print('Test passed. \n')

    def test_yahoo_option_chain(self):

        print('Testing Yahoo option chain.')
        data1, data2 = finpie.yahoo_option_chain(self.ticker)
        self.df_helper(data1)
        self.df_helper(data2)

        # check columns
        self.assertTrue( any( data1.columns.isin(['expiration']) ) )
        self.assertTrue( any( data2.columns.isin(['expiration']) ) )

        # check data type
        self.assertTrue( data1.percent_change.dtypes  == 'float' )
        self.assertTrue( data2.percent_change.dtypes  == 'float' )

        print('Test passed. \n')

    def test_futures_contacts(self):

        print('Testing futures contracts.')
        data = finpie.futures_contracts(self.date)
        self.df_helper(data)

        # check columns
        self.assertTrue( any( data.columns.isin(['open_interest']) ) )

        print('Test passed.\n')

    def test_historical_futures_contacts(self):

        print('Testing historical futures contracts.')
        date_range = pd.date_range(self.date, self.date2)
        data = finpie.historical_futures_contracts(date_range)
        self.df_helper(data)

        # check columns
        self.assertTrue( any( data.columns.isin(['open_interest']) ) )

        print('Test passed.\n')

    '''def test_cboe_option_chain(self):

        print('Testing CBOE option chain.')

        data1, data2 = finpie.cboe_option_chain(self.ticker)
        self.df_helper(data1)
        self.df_helper(data2)

        # check columns
        self.assertTrue( any( data1.columns.isin(['expiration']) ) )
        self.assertTrue( any( data2.columns.isin(['expiration']) ) )

        # check data type
        self.assertTrue( data1.net.dtypes  == 'float' )
        self.assertTrue( data2.net.dtypes  == 'float' )

        print('Test passed.\n')'''

class OtherDataTest(unittest.TestCase, CommonTest):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        CommonTest.__init__(self)

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_nasdaq_tickers(self):
        print('Testing Nasdaq tickers')
        data = finpie.nasdaq_tickers()
        self.df_helper(data)
        print('Test passed.\n')

    def test_cftc(self):
        print('Testing CFTC')
        data = finpie.cftc()
        self.df_helper(data)
        print('Test passed.\n')

    # def test_global_tickers()


class EconomicDataTest(unittest.TestCase, CommonTest):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        CommonTest.__init__(self)

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def class_test( self, cl, name ):

        for func in dir(cl):
            if callable(getattr(cl, func)) and '_' != func[0]:
                if func in 'eia_petroleum_series':
                    # requires series_id and is tested in all other functions
                    pass
                else:
                    print( f'Testing {name} {func}' )
                    data = getattr(cl, func)()
                    if type( data ) == type((1,1)):
                        for d in data:
                            self.df_helper(d)
                    else:
                        self.df_helper(data)
                    print( 'Test passed. \n')
                    time.sleep(1)

    def test_oecd(self):

        oecd = finpie.OecdData()
        self.class_test(oecd, 'OECD data')

    def test_eia(self):

        eia = finpie.EiaData()
        self.class_test(eia, 'EIA data')


class NewsDataTest(unittest.TestCase, CommonTest):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        CommonTest.__init__(self)
        #self.news = finpie.NewsData('XOM', 'exxon mobil')
        self.news = finpie.NewsData('XOM', 'exxon oil')
        #self.news.head = True

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        from pandas.core.common import SettingWithCopyWarning
        warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

    def test_nyt(self):
        print('Testing NYT.')
        data = self.news.nyt( datestop = self.date )
        self.df_helper(data)
        self.assertTrue( self.date2 in pd.date_range( data.index[-1].strftime('%Y-%m-%d'), data.index[0].strftime('%Y-%m-%d') ) )
        print('Test passed. \n')

    def test_seeking_alpha(self):
        print('Testing Seeking Alpha.')
        data = self.news.seeking_alpha( datestop = self.date )
        if type(data) != type(None):
            self.df_helper(data)
            self.assertTrue( self.date2 in pd.date_range( data.index[-1].strftime('%Y-%m-%d'), data.index[0].strftime('%Y-%m-%d') ) )
            print('Test passed. \n')
        else:
            print('Retrying.. \n')
            data = self.news.seeking_alpha( datestop = self.date )
            self.df_helper(data)
            self.assertTrue( self.date2 in pd.date_range( data.index[-1].strftime('%Y-%m-%d'), data.index[0].strftime('%Y-%m-%d') ) )
            print('Test passed. \n')


    def test_reuters(self):
        print('Testing Reuters.')
        data = self.news.reuters( datestop = self.date )
        self.df_helper(data)
        self.assertTrue( self.date2 in pd.date_range( data.index[-1].strftime('%Y-%m-%d'), data.index[0].strftime('%Y-%m-%d') ) )
        print('Test passed. \n')


    def test_cnbc(self):
        print('Testing CNBC.')
        data = self.news.cnbc( datestop = self.date )
        self.df_helper(data)
        self.assertTrue( self.date2 in pd.date_range( data.index[-1].strftime('%Y-%m-%d'), data.index[0].strftime('%Y-%m-%d') ) )
        print('Test passed. \n')


    def test_wsj(self):
        print('Testing WSJ.')
        data = self.news.wsj( datestop = self.date )
        if type(data) != type(None):
            self.df_helper(data)
            self.assertTrue( self.date2 in pd.date_range( data.index[-1].strftime('%Y-%m-%d'), data.index[0].strftime('%Y-%m-%d') ) )
            print('Test passed. \n')
        else:
            print('Retrying.. \n')
            data = self.news.seeking_alpha( datestop = self.date )
            self.df_helper(data)
            self.assertTrue( self.date2 in pd.date_range( data.index[-1].strftime('%Y-%m-%d'), data.index[0].strftime('%Y-%m-%d') ) )
            print('Test passed. \n')


    def test_ft(self):
        print('Testing FT.')
        data = self.news.ft( datestop = self.date )
        self.df_helper(data)
        self.assertTrue( self.date2 in pd.date_range( data.index[-1].strftime('%Y-%m-%d'), data.index[0].strftime('%Y-%m-%d') ) )
        print('Test passed. \n')


if __name__ == '__main__':
    unittest.main()

#ticker = 'AAPL'
#name = 'Macrotrends fundamentals'
#cl = finpie.fundamental_data.MacrotrendsData(ticker)
#cl.head = True
#for func in dir(cl):
#    if callable(getattr(cl, func)) and '_' != func[0]:
#        print( f'Testing {name} {func}' )
#        data = getattr(cl, func)()
#        print(data.head())

#date = '2020-11-03'
#n = finpie.NewsData('XOM', 'exxon oil')
#n = finpie.NewsData('NFLX', 'netflix nflx')
#n.cnbc(datestop = date)
