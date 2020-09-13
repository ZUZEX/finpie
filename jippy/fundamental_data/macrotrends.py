# Load packages
import pandas as pd
from bs4 import  BeautifulSoup as bs
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

from jippy.fundamental_data.fundamental_base import Fundamental


class macrotrendsData( Fundamental ):

    def __init__( self, ticker ):
        self.ticker = ticker
        self.head = False

    def income_statement(self, freq = 'A'):
        return self._download('income-statement', freq)


    def balance_sheet(self, freq = 'A'):
        return self._download('balance-sheet', freq)


    def cashflow_statement(self, freq = 'A'):
        return self._download('cash-flow-statement', freq)


    def ratios(self, freq = 'A'):
        return self._download('financial-ratios', freq)


    def _get_table(self, page_source):
        soup = bs(page_source, 'html5lib')
        rows = soup.find_all('div', attrs = { 'role': 'row' } )
        temp = []
        for row in rows:
            temp.append( [ cell.text for cell in row.find_all('div', attrs = { 'role': 'gridcell' } ) ] )
        df = pd.DataFrame( temp, columns = [ col.text for col in soup.find_all('div', attrs = { 'role': 'columnheader' } ) ] )
        df.drop('', axis = 1, inplace = True)
        df.columns = ['Item'] + df.columns[1:].to_list()
        df.index = df.Item
        df.drop('Item', axis = 1, inplace = True)
        return df


    def _download(self, sheet, freq):

        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        driver = self._load_driver(caps = caps)
        if self.head == True:
            driver.minimize_window()
        url = f'https://www.macrotrends.net/stocks/charts/{self.ticker}'

        try:
            driver.get(url)
            time.sleep(2)
            url = driver.current_url + f'{sheet}?freq={freq.upper()}'
            driver.get(url)
            #print(driver.find_elements_by_xpath( '//div[@role="columnheader"]')[2].text)
            element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="jqx-reset jqx-icon-arrow-right"]')))
        except:
            print('Failed to load page...')
            driver.quit()
            return None

        dfs = [ self._get_table(driver.page_source) ]
        bool, check, double_check = True, '', 0
        first = driver.find_elements_by_xpath( '//div[@role="columnheader"]')[2].text

        while bool:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="jqx-reset jqx-icon-arrow-right"]')))
            element = driver.find_element_by_xpath('//div[@class="jqx-reset jqx-icon-arrow-right"]')
            ActionChains(driver).click_and_hold(element).perform()
            time.sleep(2)
            first = driver.find_elements_by_xpath( '//div[@role="columnheader"]')[2].text
            ActionChains(driver).release(element).move_by_offset(-50, -50).perform()

            dfs.append( self._get_table(driver.page_source) )

            if check == first: #driver.find_elements_by_xpath( '//div[@role="columnheader"]')[-1].text:
                if double_check == 3:
                    bool = False
                double_check += 1

            check = first #driver.find_elements_by_xpath( '//div[@role="columnheader"]')[-1].text

        df = pd.concat(dfs, axis = 1)
        df = df.loc[:,~df.columns.duplicated()]
        driver.quit()

        df.replace('\$', '', regex = True, inplace = True)
        df.replace(',', '', regex = True, inplace = True)
        df.replace('-', '', regex = True, inplace = True)
        df = df.transpose()
        df.columns = [ col.replace(' ', '_').replace('/','_to_').replace('.', '').replace('__', '_').replace('-', '').replace('&', 'and').lower() for col in df.columns ]
        df.replace('', 'nan', inplace = True)
        df.index = pd.to_datetime(df.index, format = '%Y-%m-%d')
        df.sort_index(inplace = True)
        return self._col_to_float(df).astype('float')
