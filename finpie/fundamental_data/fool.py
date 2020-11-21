#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# finpie - a simple library to download some financial data
# https://github.com/peterlacour/finpie
#
# Copyright (c) 2020 Peter la Cour
#
# Licensed under the MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import re
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from finpie.base import DataBase

class Earnings(DataBase):

    def __init__(self, ticker):
        DataBase.__init__(self)
        self.ticker = ticker

    def transcripts(self, html = True):
        '''
        ....
        '''

        url = 'https://www.fool.com/'
        driver = self._load_driver('none')

        try:
            driver.get(url)

            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="gdpr-modal-background"]')))
                element = driver.find_element_by_xpath('//div[@id="gdpr-modal-background"]')
                self._delete_element(driver, element)
                element = driver.find_element_by_xpath('//div[@id="gdpr-modal-content"]')
                self._delete_element(driver, element)
            except:
                pass

            element = driver.find_element_by_xpath('//input[@class="ticker-input-input"]')
            element.clear()
            element.send_keys(self.ticker)
            time.sleep(0.2)
            element.send_keys(' ')
            time.sleep(1)
            element.send_keys(Keys.RETURN)

            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="gdpr-modal-background"]')))
                element = driver.find_element_by_xpath('//div[@id="gdpr-modal-background"]')
                self._delete_element(driver, element)
                element = driver.find_element_by_xpath('//div[@id="gdpr-modal-content"]')
                self._delete_element(driver, element)
            except:
                pass

            element = driver.find_element_by_xpath('//a[@id="earnings"]')
            self._scroll_to_element(driver, element)
            element.click()

            bool = True
            while bool:
                try:
                    element = driver.find_element_by_xpath('//div[@id="quote_page_earnings_listing"]//button[@id="load-more"]')
                    self._scroll_to_element(driver, element)
                    element.click()
                except:
                    bool = False

            links = [ l.get_attribute('href') for l in driver.find_elements_by_xpath('//div[@id="quote_page_earnings_listing"]//a[@data-id="article-list-hl"]') ]
            driver.quit()
        except:
            print('Failed..')
            driver.quit()
            return None

        session = HTMLSession()
        df = []
        for link in links:
            r = session.get(link)
            soup = bs(r.content, 'html5lib')

            #date = soup.find('span', class_ = 'article-content').find('span', id = 'date').text
            text = soup.find('span', class_ = 'article-content').find_all(['h2', 'p'])[3:]

            headings = [ i for i, h in enumerate(text) if '<h2>' in str(h) ]

            temp = []

            for i in range(1,len(headings)):
                temp.append( ' \n '.join([ t.text for t in text[headings[i-1]:headings[i]] ]) )
            temp.append( ' \n '.join([ t.text for t in text[headings[-1]:]] ) )

            temp = { t.split(':')[0].lower().replace(' ', '_').replace('&', 'and'): ' \n '.join(t.split(' \n ')[1:]) for t in temp if t.split(':')[0].lower() != 'contents'}
            temp['ticker'] = self.ticker
            if html:
                temp['html'] = ' '.join([ str(t) for t in text ])

            pattern = re.compile('([12]\d{3}/(0[0-9]|1[0-9])/(0[0-9]|[12]\d|3[01]))')
            date = pattern.search( link )[0]
            temp['date'] = date

            text =  soup.find('span', class_ = 'article-content').find_all('p')[1].text
            if text == 'Image source: The Motley Fool.':
                text =  soup.find('span', class_ = 'article-content').find_all('p')[2].find('em').text
                temp['time'] = text
            else:
                try:
                    text =  soup.find('span', class_ = 'article-content').find_all('p')[1].find('em').text
                    temp['time'] = text
                except:
                    temp['time'] = soup.find('span', class_ = 'article-content').find_all('p')[1].text.split(',')[-1].strip()
            #soup.find('span', class_ = 'article-content').find('em', id = 'time').text

            text = soup.find('span', class_ = 'article-content').find_all(['h2', 'p'])[1].text
            if text == 'Image source: The Motley Fool.':
                text = soup.find('span', class_ = 'article-content').find_all(['h2', 'p'])[2].text
            try:
                pattern = re.compile('(Q\d\ \d{4})')
                temp['quarter'] = pattern.search(text)[0]
            except:
                pattern = re.compile('(Q\d\\xa0\d{4})')
                temp['quarter'] = pattern.search(text)[0].replace(u'\xa0', u' ')
            temp['link'] = link  # need to add this to access in browser?

            df.append( pd.DataFrame( temp, index = [date] ) )

        df = pd.concat(df)
        df.index = pd.to_datetime(df.index)
        df.index.name = 'date'

        return df

    def _delete_element(self, driver, element):
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

    def _scroll_to_element(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)

# quick test
# e = Earnings('AAPL')
#e.head = True
# e.transcripts()
