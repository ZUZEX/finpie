from    bs4                 import BeautifulSoup    as bs
import  pandas              as pd
import  numpy               as np
import  requests
import  datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
from pyspark.sql import SparkSession
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from    selenium           import webdriver
import  datetime           as     dt
import  time
import  os
import zipfile
import io
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from    bs4                 import BeautifulSoup    as bs
import  pandas              as pd
import  numpy               as np
import  requests
import  datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
from pyspark.sql import SparkSession
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from    selenium           import webdriver
import  datetime           as     dt
import  time
import  os
import zipfile
import io
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_yahoo_prices(ticker):
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
    driver = webdriver.Chrome( executable_path=r'/Users/PeterlaCour/Documents/Research.nosync//chromedriver', options=options)
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


def get_yahoo_option_chain( ticker):
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
