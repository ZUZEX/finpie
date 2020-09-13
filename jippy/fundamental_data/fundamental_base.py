
from selenium import webdriver
import os
import sys

class Fundamental(object):
    def __init__(self):
        pass

    def _col_to_float(self, df):
        '''
        Converts string columns to floats replacing percentage signs and T, B, M, k
        to trillions, billions, millions and thousands.
        '''
        for col in df.columns:
            try:
                df.loc[df[col].str.contains('T'), col] = (df[col][df[col].str.contains('T')] \
                                                        .replace('T', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000000000) #.astype('str')
                df.loc[df[col].str.contains('B'), col] = (df[col][df[col].str.contains('B', case=True)] \
                                                        .replace('B', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000000) #.astype('str')
                df.loc[df[col].str.contains('M'), col] = (df[col][df[col].str.contains('M', case=True)] \
                                                        .replace('M', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000) #.astype('str')
                df.loc[df[col].str.contains('k'), col] = (df[col][df[col].str.contains('k', case=True)] \
                                                        .replace('k', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000) #.astype('str')
                df.loc[df[col].str.contains('%'), col] = (df[col][df[col].str.contains('%', case=True)] \
                                                        .replace('%', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') / 100) #.astype('str')
                df.loc[df[col].str.contains('K'), col] = (df[col][df[col].str.contains('K', case=True)] \
                                                     .replace('K', '', regex = True) \
                                                     .astype('float') * 1000) #.astype('str')
            except:
                continue
        return df


    def _get_chromedriver(self):

        filepath = os.path.dirname(__file__)
        if '/' in filepath:
            filepath = '/'.join( filepath.split('/')[:-1]) + '/webdrivers/'
        elif '\\' in filepath:
            filepath = '\\'.join( filepath.split('\\')[:-1]) + '\\webdrivers\\'

        if sys.platform == 'darwin':
            return  filepath + 'chromedriver_mac'
        elif 'win' in sys.platform:
            return filepath + 'chromedriver_windows'


    def _load_driver(self, caps = None):
        options = webdriver.ChromeOptions()
        if not self.head:
            options.add_argument('--headless')

        print(self._get_chromedriver())

        if caps != None:
            driver = webdriver.Chrome( executable_path=self._get_chromedriver(), options = options, desired_capabilities=caps ) # chromedriver
        else:
            driver = webdriver.Chrome( executable_path=self._get_chromedriver(), options = options ) # chromedriver
        driver.set_window_size(1400,1000)
        driver.set_page_load_timeout(1800)
        driver.delete_all_cookies()

        return driver
