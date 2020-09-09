from    bs4                 import BeautifulSoup    as bs
import  pandas              as pd
import  numpy               as np
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from    selenium           import webdriver
import  datetime           as     dt
import  time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import os
import dask.dataframe as dd
from iexfinance.stocks import get_historical_intraday
from   alpha_vantage.timeseries import TimeSeries


def alpha_vantage_prices(ticker, api_token, start_date = None):
    '''

    '''
    ts = TimeSeries(key = api_token, output_format = 'pandas')
    data, meta_data = ts.get_daily_adjusted(symbol = ticker, outputsize = 'full' )
    columns = ['open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient' ]
    data.columns = columns
    data.reset_index(level=0, inplace=True)
    data.iloc[:,1:] = data.iloc[:,1:].astype('float')
    data.date = pd.to_datetime(data.date)
    data.sort_values('date', ascending = True, inplace = True)
    data.index = data.date
    if start_date != None:
        data = data[start_date:]
    data.reset_index(drop = True, inplace = True)
    data.index = data.date
    data.drop('date', axis = 1, inplace = True)
    return data





def tingo_prices( ticker, api_token, start_date = None, end_date = None, freq = '1min'):
    '''

    Example date format = '2017-01-01'

    '''
    if start_date == None:
        start_date = '1980-01-01'
    if end_date == None:
        end_date = dt.datetime.today().date().strftime('%Y-%m-%d')
    headers = {'Content-Type': 'application/json' }
    requestResponse = requests.get(f"https://api.tiingo.com/iex/{ticker}/prices?startDate={start_date}&endDate={end_date}&resampleFreq={freq}&token={api_token}", headers=headers)
    df = pd.DataFrame(requestResponse.json())
    df.date = pd.to_datetime(df.date)

    # iterate through latest dates to get more than the last 10000 rows
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


'''

def tingo_forex_intraday( currency_pair, api_token, start_date, end_date = None, freq = '1min' ):

    if end_date == None:
        end_date = dt.datetime.today().date().strftime('%Y-%m-%d')
    headers = {'Content-Type': 'application/json' }
    requestResponse = requests.get(f'https://api.tiingo.com/tiingo/fx/{currency_pair}/prices?&endDate={end_date}&resampleFreq=1min&token={api_token}', headers = headers)
    df = pd.DataFrame(requestResponse.json())
    df.date = pd.to_datetime(df.date)

    # iterate through latest dates to get more than the last 10000 rows
    last = df.copy()
    df = dd.from_pandas(df, npartitions = 1)
    while last.date.iloc[0].date() > pd.to_datetime(start_date):
        headers = {'Content-Type': 'application/json' }
        requestResponse = requests.get(f"https://api.tiingo.com/tiingo/fx/{currency_pair}/prices?endDate={(last.date.iloc[0]).date().strftime('%Y-%m-%d')}&resampleFreq={freq}&token={api_token}", headers=headers)
        try:
            temp = pd.DataFrame(requestResponse.json())
            temp.date = pd.to_datetime(temp.date)
            if last.iloc[0,0] == temp.iloc[0,0]:
                break
            last = temp.copy()
            df = df.append(dd.from_pandas(temp, npartitions = 1))
        except:
            last.date.iloc[0] -= dt.timedelta(1)
            headers = {'Content-Type': 'application/json' }
            requestResponse = requests.get(f"https://api.tiingo.com/tiingo/fx/{currency_pair}/prices?endDate={(last.date.iloc[0]).date().strftime('%Y-%m-%d')}&resampleFreq={freq}&token={api_token}", headers=headers)
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
'''




def iex_intraday(ticker, api_token, start_date = None, end_date = None):
    '''

    '''
    if end_date == None:
        date = dt.datetime.today()
    else:
        date = pd.to_datetime(end_date)

    if start_date == None:
        start_date = pd.to_datetime('2000-01-01')

    df = dd.from_pandas(get_historical_intraday(ticker, date, token = api_token, output_format = 'pandas'), npartitions = 1)

    e, i = 0, 0
    date = dt.datetime.today() - dt.timedelta(i)
    while e <= 5 and date > start_date:
        date = dt.datetime.today() - dt.timedelta(i)
        df2 = get_historical_intraday(ticker, date, token = api_token, output_format = 'pandas')
        if not df2.empty:
            df = df.append(dd.from_pandas(df2, npartitions = 1))
            time.sleep(.5)
            e = 0
        else:
            e += 1
        i += 1
    return df



def yahoo_prices(ticker):
    '''

    '''
    def downloads_done():
        '''
        https://stackoverflow.com/questions/48263317/selenium-python-waiting-for-a-download-process-to-complete-using-chrome-web
        '''
        for i in os.listdir():
            if ".crdownload" in i:
                time.sleep(0.5)
                downloads_done()

    filepath = os.getcwd()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    prefs = {'download.default_directory' : filepath}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome( executable_path=r'chromedriver', options=options)
    url = f'https://finance.yahoo.com/quote/{ticker}/history?'
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        driver.find_element_by_xpath('//button[@type="submit"]').click()
    except:
        driver.quit()
        print(f'{ticker} download failed. Ticker may not exist.')
        return None
    try:
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'dateRangeBtn')))
        driver.find_element_by_class_name('dateRangeBtn').click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@data-value="MAX"]')))
        driver.find_element_by_xpath('//button[@data-value="MAX"]').click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//a[@download="{ticker}.csv"]')))
        driver.find_element_by_xpath(f'//a[@download="{ticker}.csv"]').click()
        # waits for all the files to be completed
        #paths = WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
        time.sleep(2)
        downloads_done()
        driver.quit()
    except:
        driver.quit()
        # remove crdownload files
        print(f'{ticker} download failed. Ticker may not exist.')
        return None
    df = pd.read_csv( filepath + f'/{ticker}.csv')
    os.remove( filepath + f'/{ticker}.csv')
    df.index = pd.to_datetime(df.Date)
    df.drop('Date', axis = 1, inplace = True)
    return df


def yahoo_option_chain( ticker):
    '''

    '''
    # Scrape website
    contents = []
    url = 'https://finance.yahoo.com/quote/{}/options'.format(ticker)
    options = Options()
    driver = webdriver.Firefox( executable_path=r'geckodriver', options = options )
    driver.get(url)
    try:
        try:
            driver.find_element_by_xpath('//form/button').click()
        except:
            pass
        scroll_page(driver)
        contents.append(driver.page_source)
        elements = driver.find_elements_by_xpath('//div[@class="Fl(start) Pend(18px) option-contract-control drop-down-selector"]//descendant::option')
        dates = [ ele.get_attribute('value') for ele in elements ]
        for d in dates[1:]:
            driver.get( 'https://finance.yahoo.com/quote/{}/options?date={}'.format(ticker, d) )
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calls')))
            except:
                pass
            scroll_page(driver)
            contents.append(driver.page_source)
        driver.quit()
        # Parse htmls
        calls = []
        puts  = []
        for idx, content in enumerate(contents):
            soup = bs(content, 'lxml')
            try:
                temp = pd.read_html(str(soup.find('table', class_ = 'calls')))[0]
                trs = soup.find('table', class_ = 'calls').find_all('tr')
                temp['ITM'] = [ 1 if 'in-the-money' in t['class'] else 0 for t in trs ][1:]
                calls.append( temp )
            except:
                print( dt.date.fromtimestamp( int(dates[idx]) ) )
            try:
                temp = pd.read_html(str(soup.find('table', class_ = 'puts')))[0]
                trs = soup.find('table', class_ = 'puts').find_all('tr')
                temp['ITM'] = [ 1 if 'in-the-money' in t['class'] else 0 for t in trs ][1:]
                puts.append(temp)
            except:
                print( dt.date.fromtimestamp( int(dates[idx]) ) )
        # Create dataframes
        calls = create_option_df(calls, 'Call')
        puts = create_option_df(puts, 'Put')

        return calls, puts

    except:
            try:
                driver.quit()
                print(ticker, 'failed.')
            except:
                print(ticker, 'failed.')

            return ticker


url = 'https://www.investing.com/indices/us-spx-500-futures-historical-data'

def investing_com_prices(url):
    '''
        For popup:
            <i class="popupCloseIcon largeBannerCloser"></i>'
            element = driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]')
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
            ActionChains(driver).move_to_element(element).click().perform()
    '''

    months = { 'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', \
               'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', \
               'Nov': '11', 'Dec': '12' }
    contents = []
    check = None

    today = dt.datetime.today().date()

    last_date = today

    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome( executable_path=r'/Users/PeterlaCour/Documents/Research.nosync/financial_data_project/jippy/jippy/price_data/chromedriver', options=options)
    driver.get(url)
    time.sleep(2)
    try:
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')))
            driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]').click()
        except:
            pass
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//i[@class="popupCloseIcon largeBannerCloser"]')))
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass

        last_date = last_date - dt.timedelta(10 * 360)

        element = driver.find_element_by_xpath( '//div[@class="datePickerWrap calendarDatePicker"]' )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
        ActionChains(driver).move_to_element(element).click().perform()
        time.sleep(3)
        element = driver.find_element_by_xpath('//input[@id="startDate"]')
        element.clear()
        element.send_keys(last_date.strftime('%m/%d/%Y'))

        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass

        driver.find_element_by_xpath('//a[@id="applyBtn"]').click()
        time.sleep(3)
        contents.append(driver.page_source)

        bool = True
        while bool:
            prev_date = last_date
            last_date = prev_date - dt.timedelta(10 * 360)

            try:
                driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
            except:
                pass
            try:
                driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
            except:
                pass

            element = driver.find_element_by_xpath( '//div[@class="datePickerWrap calendarDatePicker"]' )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
            ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(3)
            
            try:
                driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
            except:
                pass
            try:
                driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
            except:
                pass

            element = driver.find_element_by_xpath('//input[@id="startDate"]')
            element.clear()
            element.send_keys(last_date.strftime('%m/%d/%Y'))

            try:
                driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
            except:
                pass
            try:
                driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
            except:
                pass

            element = driver.find_element_by_xpath('//input[@id="endDate"]')
            element.clear()
            element.send_keys(prev_date.strftime('%m/%d/%Y'))

            driver.find_element_by_xpath('//a[@id="applyBtn"]').click()
            time.sleep(3)

            try:
                driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
            except:
                pass
            try:
                driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
            except:
                pass

            if bs(driver.page_source, 'lxml').find('table', class_ = 'historicalTbl') == check:
                bool = False #last_date < pd.to_datetime()
            else:
                contents.append(driver.page_source)
                check = bs(driver.page_source, 'lxml').find('table', class_ = 'historicalTbl')
        driver.quit()
    except:
        print('Failed.')
        driver.quit()
        #return None

    date, price, open, high, low, vol, change = [], [], [], [], [], [], []
    for content in contents:
        soup = bs(content, 'lxml')
        tbody   = soup.find('table', class_ = 'historicalTbl')
        rows    = tbody.find_all('tr')
        if len(rows) > 2:
            for row in rows[1:]:
                cols = row.find_all('td')
                date.append( cols[0].text )
                price.append( cols[1].text )
                open.append( cols[2].text )
                high.append( cols[3].text )
                low.append( cols[4].text )
                vol.append( cols[5].text )
                change.append( cols[6].text )

    for i, d in enumerate( date ):
        d       = d.replace(',', '').split(' ')
        date[i] = d[1] + '/' + months[ d[0] ] + '/' + d[2]

    df = pd.DataFrame( { 'date': date, 'price': price, 'open': open, 'high': high, \
                         'low': low, 'volume': vol
                        } ).drop_duplicates().reset_index(drop = True)

    df.replace('-', str(np.nan), inplace = True)
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
    df.index = pd.to_datetime(df.date, format = '%d/%m/%Y')
    df.sort_index( inplace = True)
    df.drop('date', axis = 1, inplace = True)
    return df.astype('float')



################################################################################
################################################################################
################################################################################

# helper functions

def create_option_df(  data, option_type ):
    '''

    '''
    data = pd.concat(data)
    data['Option'] = option_type
    data.reset_index(inplace = True, drop = True)
    data['Date_Retrieved'] = dt.datetime.today()
    data.replace('-', np.nan, inplace = True)
    for col in list(data.columns):
        data[col] = data[col].astype('str')
    data.columns = [col.replace(' ', '_').replace('%', 'Percentage') for col in data.columns]
    return data

def scroll_page( driver):
    '''

    '''
    old = len(driver.find_elements_by_tag_name('tr'))
    new = 0
    bool = True
    while bool:
        if old != new:
            old = new
            new = 0
        else:
            bool = False
        driver.execute_script('window.scrollTo(0,document.documentElement.scrollHeight);')
        time.sleep(0.25)
        new = len(driver.find_elements_by_tag_name('tr'))






def investing_com_prices(url):
    '''
        For popup:
            <i class="popupCloseIcon largeBannerCloser"></i>'
            element = driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]')
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
            ActionChains(driver).move_to_element(element).click().perform()
    '''

    months = { 'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', \
               'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', \
               'Nov': '11', 'Dec': '12' }
    contents = []

    today = dt.datetime.today().date()

    last_date = today


    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome( executable_path=r'/Users/PeterlaCour/Documents/Research.nosync/financial_data_project/jippy/jippy/price_data/chromedriver', options=options)
    driver.get(url)
    time.sleep(2)
    try:
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')))
            driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]').click()
        except:
            pass
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//i[@class="popupCloseIcon largeBannerCloser"]')))
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        element = driver.find_element_by_xpath( '//div[@class="datePickerWrap calendarDatePicker"]' )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
        ActionChains(driver).move_to_element(element).click().perform()
        time.sleep(3)
        element = driver.find_element_by_xpath('//input[@id="startDate"]')
        element.clear()
        element.send_keys(last_date.strftime('%m/%d/%Y'))
        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        driver.find_element_by_xpath('//a[@id="applyBtn"]').click()
        time.sleep(3)
        contents.append(driver.page_source)
        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        element = driver.find_element_by_xpath( '//div[@class="datePickerWrap calendarDatePicker"]' )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        try:
            driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]').click()
        except:
            pass
        ActionChains(driver).move_to_element(element).click().perform()
        time.sleep(3)
        element = driver.find_element_by_xpath('//input[@id="startDate"]')
        element.clear()

        last_date = last_date - dt.timedelta(10 * 360)
        element.send_keys(last_date.strftime('%m/%d/%Y'))
        driver.find_element_by_xpath('//a[@id="applyBtn"]').click()
        time.sleep(3)
        contents.append(driver.page_source)
        driver.quit()
