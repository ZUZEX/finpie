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
import random
import numpy as np
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from finpie.news_data.clean_news import CleanNews

class NewsData(CleanNews):
    def __init__(self, ticker, keywords, head = False, verbose = False):
        CleanNews.__init__(self)
        self.ticker = ticker
        self.keywords = keywords
        self.verbose = verbose
        # self.datestop = False

    #########################################################################
    # initial news scrapes
    #########################################################################

    def ft( self, datestop = False ):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                            Financial Times
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def _delete_elements(driver):
            element = driver.find_element_by_tag_name('head')
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)

            element = driver.find_element_by_xpath('//div[@class="n-layout__row n-layout__row--header"]')
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)

            elements = driver.find_elements_by_class_name('o-teaser__image-placeholder')
            for element in elements:
                driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, element)

            element = driver.find_element_by_tag_name('nav')
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)

            element = driver.find_element_by_id('o-header-drawer')
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)

            element = driver.find_element_by_tag_name('footer')
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)

        def _get_articles(contents, headline, link, date, description, author, tag):
            for articles in contents:
                #soup  = bs( content, "lxml" )
                #articles  = soup.find_all('div', class_ = 'o-teaser__content' )
                for article in articles:
                    tag.append( article.find('a').text )
                    headline.append( article.find('div', class_ = 'o-teaser__heading' ).text.replace('\t', ' ').replace('\n', ' ').strip() )
                    link.append( article.find('div', class_ = 'o-teaser__heading' ).find('a').get('href') )
                    try:
                        description.append( article.find('p', class_ = 'o-teaser__standfirst' ).text.replace('\t', ' ').replace('\n', ' ').strip() )
                    except:
                        description.append( 'nan' )
                    date.append( article.find('div', class_ = 'o-teaser__timestamp' ).text )
            return headline, link, date, description, author, tag

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        source = 'ft'

        y = str(dt.datetime.today().year)
        if len(str(dt.datetime.today().month) ) < 2:
            m = '0' + str(dt.datetime.today().month)
        else:
            m = str(dt.datetime.today().month)
        if len(str(dt.datetime.today().day) ) < 2:
            d = '0' + str(dt.datetime.today().day)
        else:
            d =  str(dt.datetime.today().day)

        url = 'https://www.ft.com/search?q=' + self.keywords.replace(' ', '%20') + '&dateTo=' + y + '-' + m + '-' + d + '&sort=date&expandRefinements=true'


        driver = self._load_driver(caps = 'normal')

        try:
            # Set and retrive url
            driver.get(url)
            time.sleep(10) # make implicit wait
            co = 0
            # _delete_elements(driver)

            #driver.find_elements_by_xpath('//a[@data-trackable="sort-item"]')[1].click()
            # Cant get more than 1000 results and need to change date filter when it gives an error
            contents = []
            contents.append( bs( driver.page_source, "lxml" ).find_all('div', class_ = 'o-teaser__content' ) )
            co += 1
            max_articles = np.floor( int( driver.find_element_by_xpath('//h2[@class="o-teaser-collection__heading o-teaser-collection__heading--half-width"]').text.split('of ')[-1].strip() ) / 25 )
            while co < int(max_articles):
                try:
                    max = int( driver.find_element_by_xpath('//span[@class="search-pagination__page"]').text.replace('Page 1 of ', '') )
                    for i in range(max):
                        driver.find_element_by_xpath('//a[@class="search-pagination__next-page o-buttons o-buttons--secondary o-buttons-icon o-buttons-icon--arrow-right o-buttons--big o-buttons-icon--icon-only"]').click()
                        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//head')))
                        _delete_elements(driver)
                        contents.append( bs( driver.page_source, "lxml" ).find_all('div', class_ = 'o-teaser__content' ) )
                        co += 1

                        dte = driver.find_elements_by_xpath('//div[@class="o-teaser__timestamp"]')[-1].text

                        if datestop:
                            if pd.to_datetime( dte ) < pd.to_datetime(datestop):
                                co = int(max_articles) + 10
                                break

                except:
                    try:
                        m = self.months[driver.find_elements_by_xpath('//time[@class="o-teaser__timestamp-date"]')[-1].text.lower()[:3]]
                        d = driver.find_elements_by_xpath('//time[@class="o-teaser__timestamp-date"]')[-1].text.split(' ')[1].replace(',', '')
                        y =  driver.find_elements_by_xpath('//time[@class="o-teaser__timestamp-date"]')[-1].text.split(',')[-1].strip()
                        if len(str(m)) < 2:
                            m = '0' + str(m)
                        else:
                            m = str(m)
                        if len(str(d) ) < 2:
                            d = '0' + str(d)
                        else:
                            d =  str(d)

                        dte = pd.to_datetime(y + m + d, format = '%Y%m%d') + dt.timedelta(1)

                        if datestop:
                            if dte < pd.to_datetime(datestop):
                                co = int(max_articles) + 10

                        y, m, d = self._format_date(dte)
                        url = 'https://www.ft.com/search?q=' + self.keywords.replace(' ', '%20') + '&dateTo=' + y + '-' + m + '-' + d + '&sort=date&expandRefinements=true'
                        driver.get( url )
                        #driver.find_elements_by_xpath('//a[@data-trackable="sort-item"]')[1].click()
                        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//head')))
                        _delete_elements(driver)
                        contents.append( bs( driver.page_source, "lxml" ).find_all('div', class_ = 'o-teaser__content' ) )
                        co += 1
                    except:
                        break
            driver.close()
            driver.quit()
        except:
            print('Failed to load data...\n')
            driver.quit()
            return None

        headline, link, date, description, author, tag = [], [], [], [], [], []
        headline, link, date, description, author, tag = _get_articles(contents, headline, link, date, description, author, tag)

        contents = None

        data = pd.DataFrame(
                {
                    'link': link,
                    'headline': headline,
                    'date': date,
                    'description': description,
                    'tag': tag
                }
            )
        data['date_retrieved'] = dt.datetime.today()
        data['ticker'] = self.ticker
        data['comments'] = 'nan'
        data['author'] = 'nan'
        data['newspaper'] = 'FT'
        data['search_term'] = self.keywords
        data['id'] = data['newspaper'] +  data['headline'] + data['link']
        columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'

        headline, link, date, description, author, tag  = [], [], [], [], [], []
        #soup = None

        data['source'] = source

        data.drop_duplicates(inplace = True)

        data = self._clean_dates(data)
        # write to parquet file with ticker as partition

        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)
        return data



    def wsj( self, datestop = False ):

        source = 'wsj'

        # change to date today
        td_1 = dt.datetime.today() - dt.timedelta(days = 320)
        y, m, d = self._format_date(td_1)
        start_date = y + '/' + m + '/' + d
        td_2 = dt.datetime.today()
        y, m, d = self._format_date(td_2)
        end_date = y + '/' + m + '/' + d

        url = 'https://www.wsj.com/search?&query=' + self.keywords.replace(' ', '%20')  + '&min-date=' + start_date + '&max-date=' + end_date + '&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,press,newswire,wsjpro'

        driver = self._load_driver(caps = 'none')

        try:
            # Set and retrive url
            driver.get(url)
            time.sleep(3)
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
            bool2 = True
            contents = []
            #max = int( driver.find_element_by_xpath('//div[@class="results-menu-wrapper bottom"]//li[@class="results-count"]').text.replace('of ', '') )
            max = int(driver.find_element_by_xpath('//div[@class="WSJTheme--dropdown--3cxtZgDl "]/following::span[contains(text(), "of")]').text.replace('of ', ''))
            contents.append(driver.page_source)
            for i in range(max-1):
                try:
                    time.sleep(random.randint(0,2))
                    driver.get(url + f'&page={i+2}')
                    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                    driver.find_element_by_xpath('//a[contains(text(), "next")]').click()
                    contents.append(driver.page_source)
                except:
                    try:
                        #driver.get(url)
                        driver.get(url + f'&page={i+2}')
                        #driver.find_element_by_xpath('//a[contains(text(), "next")]').click()
                        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                        contents.append(driver.page_source)
                    except:
                        driver.get(url + f'&page={i+2}')
                        #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                        time.sleep(5)
                        contents.append(driver.page_source)

                if datestop:
                    try:
                        #d = driver.find_elements_by_xpath('//time[@class="date-stamp-container"]')[-1].text
                        d = driver.find_elements_by_xpath('//p[contains(@class, "WSJTheme--timestamp")]')[-1].text
                        d = pd.to_datetime(' '.join( d.split(' ')[:3] ))
                        if d < pd.to_datetime(datestop):
                            bool2 = False
                            break
                    except:
                        #d = driver.find_elements_by_xpath('//time[@class="date-stamp-container highlight"]')[-1].text
                        d = driver.find_elements_by_xpath('//p[contains(@class, "WSJTheme--timestamp")]')[-1].text

                        pass


            if bool2:
                bool = True
            else:
                bool = False
                # Record progress
                #_print_progress(i, max-1)
            contents.append(driver.page_source)

            while bool:
                try:
                    td_2 = td_1
                    y, m, d = self._format_date(td_2)
                    start_date = y + '/' + m + '/' + d
                    td_1 = td_1 - dt.timedelta(days = 320)
                    y, m, d = self._format_date(td_1)
                    end_date = y + '/' + m + '/' + d

                    url = 'https://www.wsj.com/search?&query=' + self.keywords.replace(' ', '%20')  + '&min-date=' + start_date + '&max-date=' + end_date + '&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,press,newswire,wsjpro'

                    driver.get(url)

                    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))

                    #driver.switch_to.frame(0)
                    #driver.find_elements_by_xpath('//article')


                    #max = int( driver.find_element_by_xpath('//div[@class="results-menu-wrapper bottom"]//li[@class="results-count"]').text.replace('of ', '') )
                    max = int(driver.find_element_by_xpath('//div[@class="WSJTheme--dropdown--3cxtZgDl "]/following::span[contains(text(), "of")]').text.replace('of ', ''))
                    contents.append(driver.page_source)

                    for i in range(max-1):
                        try:
                            time.sleep(random.randint(0,2))
                            driver.get(url + f'&page={i+2}')
                            #driver.find_element_by_xpath('//a[contains(text(), "next")]').click()
                            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                            contents.append(driver.page_source)
                        except:
                            try:
                                driver.get(url + f'&page={i+2}')
                                #driver.get(url)
                                #driver.find_element_by_xpath('//a[contains(text(), "next")]').click()
                                element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                                contents.append(driver.page_source)
                            except:
                                driver.get(url + f'&page={i+2}')
                                contents.append(driver.page_source)

                        if datestop:
                            #d = driver.find_elements_by_xpath('//time[@class="date-stamp-container"]')[-1].text
                            d = driver.find_elements_by_xpath('//p[contains(@class, "WSJTheme--timestamp")]')[-1].text
                            d = pd.to_datetime(' '.join( d.split(' ')[:3] ))
                            if d > pd.to_datetime(datestop):
                                bool = False
                except:
                    bool = False

            driver.close()
            driver.quit()
        except:
            print('Failed to load data...\n')
            driver.quit()
            return None

        headline, link, date, description, author, tag = [], [], [], [], [], []



        for content in contents:
            soup  = bs( content, "lxml" )
            #articles  = soup.find_all('div', class_ = 'headline-item' )
            articles  = soup.find_all('article')

            for article in articles:

                try:
                    date.append( article.find('p', class_ = re.compile('^WSJTheme--timestamp') ).text )
                except:
                    continue

                headline.append( article.find('h3').text.strip() )
                link.append( article.find('h3').find('a').get('href') )
                try:
                    tag.append( article.find('li', class_ = re.compile('^WSJTheme--type') ).text )
                except:
                    tag.append( 'nan' )
                #date.append( article.find('time').text )

                try:
                    #author.append( article.find('li', class_ = 'byline').text.replace('By', '').strip() )
                    author.append( article.find('p', class_ = re.compile('^WSJTheme--byline') ).text.strip() )
                except:
                    author.append( 'nan' )
                try:
                    description.append( article.find('p', class_ = re.compile('^WSJTheme--summary') ).text.strip() )
                except:
                    description.append( 'nan' )

        data = pd.DataFrame(
                {
                    'link': link,
                    'headline': headline,
                    'date': date,
                    'description': description,
                    'author': author,
                    'tag': tag
                }
            )

        data['date_retrieved'] = dt.datetime.today()
        data['ticker'] = self.ticker
        data['newspaper'] = 'WSJ'
        data['search_term'] = self.keywords

        data['id'] = data['newspaper'] +  data['headline'] + data['link']
        columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'

        data['source'] = source

        data = self._clean_dates(data)
        # write to parquet file with ticker as partition

        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


    def seeking_alpha(self, datestop = False, press_releases = False):
        # Note: might be stopping scrape too early

        def _get_date(d):
            w = d.split(' ')[1:]
            if len(w) == 2:
                d = pd.to_datetime( w[1].replace(',', '')  + '/' + self.months[w[0][:3].lower()] + '/' + str(dt.datetime.today().year), format = '%d/%m/%Y' )
            else:
                d = pd.to_datetime( w[1].replace(',', '')  + '/' + self.months[w[0][:3].lower()] + '/' + str(w[2]), format = '%d/%m/%Y' )
            return d

        source = 'sa'

        if press_releases:
            url =  f'https://seekingalpha.com/symbol/{self.ticker}/press-releases'
        else:
            url = f'https://seekingalpha.com/symbol/{self.ticker}/news'
        driver = self._load_driver(caps = 'none')
        try:
            # Set and retrive url
            driver.get(url)

            time.sleep(5)


            passed = False
            try:
                xpath = '//div[@id="px-captcha"]'
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                element = driver.find_element_by_tag_name('iframe')
                ActionChains(driver).click_and_hold(element).perform()
                time.sleep(5)
                ActionChains(driver).release(element).perform()
                passed = True
            except:
                pass

            try:
                xpath = '//div[@id="px-captcha"]'
                element = driver.find_element_by_xpath(xpath)
                ActionChains(driver).click_and_hold(element).perform()
                time.sleep(7)
                ActionChains(driver).release(element).perform()
                passed = True
            except:
                pass

            time.sleep(10)
            driver.switch_to.window(driver.window_handles[0])

            element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//article')))
            k = 0
            t = 20
            SCROLL_PAUSE_TIME = 0.9

            while k < t:
                k = 0

                if not passed:
                    try:
                        xpath = '//div[@id="px-captcha"]'
                        if len(driver.find_elements_by_xpath(xpath)) > 0:
                            element = driver.find_element_by_tag_name('iframe')
                            ActionChains(driver).click_and_hold(element).perform()
                            time.sleep(5)
                            ActionChains(driver).release(element).perform()
                            passed = False
                    except:
                        pass
                #last_height       = driver.execute_script( 'return document.documentElement.scrollHeight' )
                #last_number = len(driver.find_elements_by_class_name('symbol_item'))
                last_number =  len(driver.find_elements_by_xpath('//article'))
                # Scroll down to bottom
                driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                #new_height = driver.execute_script( 'return document.documentElement.scrollHeight;' )
                #new_number = len(driver.find_elements_by_class_name('symbol_item'))
                new_number = len(driver.find_elements_by_xpath('//article'))

                if datestop:
                    d = _get_date(driver.find_elements_by_xpath('//span[@data-test-id="post-list-date"]')[-1].text)
                    if d < pd.to_datetime(datestop):
                        k = t + 10

                while new_number == last_number:

                    # need to verify this
                    if not passed:
                        try:
                            xpath = '//div[@id="px-captcha"]'
                            if len(driver.find_elements_by_xpath(xpath)) > 0:
                                element = driver.find_element_by_tag_name('iframe')
                                ActionChains(driver).click_and_hold(element).perform()
                                time.sleep(5)
                                ActionChains(driver).release(element).perform()
                                passed = False
                        except:
                            pass

                    driver.execute_script("window.scrollTo(0, -document.documentElement.scrollHeight);")
                    time.sleep(SCROLL_PAUSE_TIME/3)

                    driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
                    time.sleep(SCROLL_PAUSE_TIME/3)

                    # Wait to load page
                    #new_height = driver.execute_script( 'return document.documentElement.scrollHeight;' )
                    #new_number = len(driver.find_elements_by_class_name('symbol_item'))
                    new_number = len(driver.find_elements_by_xpath('//article'))
                    time.sleep(SCROLL_PAUSE_TIME/3)

                    k +=1
                    if k == t:
                        break
                    time.sleep(0.5)

            soup  = bs( driver.page_source, "lxml" )

            driver.close()
            driver.quit()
        except:
            print('Failed to load data...\n')
            driver.quit()
            return None

        headline, link, date, author, comments = [], [], [], [], []

        # news
        headline, link, date, author, comments = [], [], [], [], []
        articles  = soup.find('div', attrs = {'data-test-id': 'post-list'} ).find_all('article' )
        for article in articles:
            try:
                headline.append( article.find('h3').text )
                link.append( article.find('a').get('href') )
                author.append( article.find('span', attrs = {'data-test-id': 'post-list-author'} ).text )
                date.append( article.find('span', attrs = {'data-test-id': 'post-list-date'} ).text )
                try:
                    comments.append( article.find('span', attrs = {'data-test-id': 'post-list-comments'} ).text )
                except:
                    comments.append( '0 comments' )
            except:
                continue


        df_news = pd.DataFrame(
                {
                    'link': link,
                    'headline': headline,
                    'date': date,
                    'author': author,
                    'comments': comments
                }
            )

        df_news['date_retrieved'] = dt.datetime.today()
        df_news['ticker'] = self.ticker
        df_news['description'] = 'nan'
        df_news['tag'] = 'nan'
        df_news['newspaper'] = 'SA - News'


        data = df_news.copy()
        data['search_term'] = self.keywords

        data['id'] = data['newspaper'] +  data['headline'] + data['link']
        columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'

        headline, link, date, author, comments = [], [], [], [], []
        df_news = None
        articles = None
        soup = None

        data['source'] = source

        data = self._clean_dates(data)


        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


    def barrons(self, datestop = False, companyNews = False):

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #                            Barrons
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # problem with older data having concatenated strings in their headlines
        driver = self._load_driver(caps = 'normal')
        source = 'barrons'

        if companyNews:

            url = f'https://www.barrons.com/quote/stock/{self.ticker}'


            try:
                # Set and retrive url
                driver.get(url)

                xpath = '//div[@class="news bgNews more-news-capable"]'
                element = driver.find_element_by_xpath(xpath)

                bool = True
                while bool:
                    driver.execute_script('arguments[0].scrollTop += 1000', element)
                    if datestop:
                        d = driver.find_elements_by_xpath('//span[@class="date"]')[0].text
                        if pd.to_datetime( d ) < pd.to_datetime( datestop ):
                            bool = False
                    try:
                        xpath = '//div[@class="no-more-news"][contains(@style,"display: block")]'
                        driver.find_element_by_xpath(xpath)
                        bool = False
                    except:
                        pass

                articles = bs( driver.page_source, "lxml" ).find('ul', class_ = 'news-columns').find_all('li' )

                driver.close()
                driver.quit()
            except:
                print('Failed to load data...\n')
                driver.quit()
                return None

            headline, link, date, description, author, tag, newspaper = [], [], [], [], [], [], []
            for article in articles:
                link.append( article.find('a').get('href') )
                headline.append( article.find('a').text )
                date.append( article.find('span', class_ = 'date' ).text )
                newspaper.append( article.find('span', class_ = 'provider').text )

            data = pd.DataFrame(
                    {
                        'link': link,
                        'headline': headline,
                        'date': date,
                        'newspaper': newspaper,
                    }
                )

            headline, link, date, description, author, tag = [], [], [], [], [], []
            contents = None

            data['date_retrieved'] = dt.datetime.today()
            data['ticker'] = self.ticker
            data['comments'] = 'nan'
            data['tag'] = 'nan'
            data['search_term'] = 'nan'

            data['id'] = data['newspaper'] +  data['headline'] + data['link']
            columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
            for col in columns:
                if col not in data.columns:
                    data[col] = 'nan'
            data['source'] = source
            data = self._clean_dates(data)

            if self.verbose:
                print('-' * 78)
                print(source.upper(), 'done.', len(data), 'articles collected.')
                print('-' * 78)

            return data

        else:
            url = 'https://www.barrons.com/search?keyword=' + self.keywords + '&numResults=75&sort=date-desc&author=&searchWindow=0&minDate=&maxDate=&source=barrons&source=other&source=press'

            try:
                # Set and retrive url
                driver.get(url)

                # close popup
                contents = []
                try:
                    contents.append( bs( driver.page_source, "lxml" ).find('div', class_ = 'section-content').find_all('li' ) )
                except:
                    pass
                bool = True
                while bool:
                    try:
                        driver.get(driver.find_element_by_xpath('//a[@class="pull-right pageLink pageLink--next"]').get_attribute('href'))
                        contents.append( bs( driver.page_source, "lxml" ).find('div', class_ = 'section-content').find_all('li' ) )
                        if len(driver.find_elements_by_class_name('headline')) == 0 :
                            bool = False
                        if datestop:
                            d = driver.find_elements_by_xpath('//span[@class="date"]')[-1].text
                            if pd.to_datetime( d ) < pd.to_datetime( datestop ):
                                bool = False
                    except:
                        bool = False

                driver.close()
                driver.quit()
            except:
                print('Failed to load data...\n')
                driver.quit()
                return None

            headline, link, date, description, author, tag, newspaper = [], [], [], [], [], [], []

            for articles in contents:
                #soup  = bs( content, "lxml" )
                #articles  = soup.find('div', class_ = 'section-content').find_all('li' )
                for article in articles:
                    link.append( article.find('a').get('href') )
                    headline.append( article.find('span', class_ = 'headline' ).text )
                    date.append( article.find('span', class_ = 'date' ).text )
                    author.append( article.find('span', class_ = 'author' ).text )
                    newspaper.append( article.find('span', class_ = 'provider').text )
                    try:
                        description.append( article.find('p').text )
                    except:
                        description.append( 'nan' )


            data = pd.DataFrame(
                    {
                        'link': link,
                        'headline': headline,
                        'date': date,
                        'description': description,
                        'newspaper': newspaper,
                        'author': author
                    }
                )

            headline, link, date, description, author, tag = [], [], [], [], [], []
            contents = None

            data['date_retrieved'] = dt.datetime.today()
            data['ticker'] = self.ticker
            data['comments'] = 'nan'
            data['tag'] = 'nan'

            data['search_term'] = self.keywords


            data['id'] = data['newspaper'] +  data['headline'] + data['link']
            columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
            for col in columns:
                if col not in data.columns:
                    data[col] = 'nan'
            data['source'] = source

            data = self._clean_dates(data)


            if self.verbose:
                print('-' * 78)
                print(source.upper(), 'done.', len(data), 'articles collected.')
                print('-' * 78)

            return data


    def cnbc(self, datestop = False):

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #                            CNBC
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # may want to change keywords

        source = 'cnbc'

        url = 'https://www.cnbc.com/search/?query=' + self.keywords.replace(' ', '%20') + '&qsearchterm=' + self.keywords.replace(' ', '%20')

        driver = self._load_driver(caps = 'none')

        try:
            # Set and retrive url
            driver.get(url)

            try:
                xpath = '//button[@id="onetrust-accept-btn-handler"]'
                element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
                driver.find_element_by_xpath(xpath).click()
            except:
                pass

            #
            try:
                element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//span[@class="SearchResult-publishedDate"]')))
            except:
                element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//button[@class="Search-submitBtn icon-search"]')))
                driver.get(url)
                element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//span[@class="SearchResult-publishedDate"]')))

            #driver.refresh()
            try:
                try:
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="sortdate"]')))
                    element = driver.find_element_by_xpath('//div[@id="sortdate"]')
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
                    ActionChains(driver).move_to_element( element).click().perform()
                    time.sleep(3)
                except:
                    pass
            except:
                pass

            #element = driver.find_element_by_tag_name('head')
            #driver.execute_script("""
            #var element = arguments[0];
            #element.parentNode.removeChild(element);
            #""", element)

            k = 0
            t = 100
            SCROLL_PAUSE_TIME = 0.5
            while k < t:
                k = 0

                if datestop:
                    element = driver.find_elements_by_xpath('//span[@class="SearchResult-publishedDate"]')[-1].text
                    element = pd.to_datetime( element.split(' ')[0], format = '%m/%d/%Y' )
                    if element < pd.to_datetime(datestop):
                        k = 110
                # SearchResult-searchResultImage
                #SearchResult-searchResultCard SearchResult-standardVariant
                try:
                    elements = driver.find_elements_by_xpath('//div[@class="SearchResult-searchResultCard SearchResult-standardVariant"]')
                    for element in elements:
                        driver.execute_script("""
                        var element = arguments[0];
                        element.parentNode.removeChild(element);
                        """, element)
                except:
                    pass

                try:
                    elements = driver.find_elements_by_xpath('//a[@class="Card-mediaContainer resultlink"]')
                    for element in elements:
                        driver.execute_script("""
                        var element = arguments[0];
                        element.parentNode.removeChild(element);
                        """, element)
                except:
                    pass

                last_height       = driver.execute_script( 'return document.documentElement.scrollHeight' )

                # Scroll down to bottom
                driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script( 'return document.documentElement.scrollHeight;' )

                time.sleep(random.randint(0,4) * 0.43)

                while new_height == last_height:

                    driver.execute_script("window.scrollTo(0, -document.documentElement.scrollHeight);")
                    time.sleep(SCROLL_PAUSE_TIME/3)

                    driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
                    time.sleep(SCROLL_PAUSE_TIME/3)

                    # Wait to load page
                    new_height = driver.execute_script( 'return document.documentElement.scrollHeight;' )
                    time.sleep(SCROLL_PAUSE_TIME/3)

                    if datestop:
                        element = driver.find_elements_by_xpath('//span[@class="SearchResult-publishedDate"]')[-1].text
                        element = pd.to_datetime( element.split(' ')[0], format = '%m/%d/%Y' )
                        if element < pd.to_datetime(datestop):
                            k = 110
                    k += 1
                    if k >= t:
                        break
                    time.sleep(random.randint(0,2) * 0.43)
            content = driver.page_source
            driver.close()
            driver.quit()
        except:
            print('Failed to load data...\n')
            driver.quit()
            return None

        headline, link, date, description, author, tag = [], [], [], [], [], []

        soup  = bs( content, "lxml" )
        articles  = soup.find_all('div', class_ = 'SearchResult-searchResult' )
        len(articles)
        for article in articles:
            link.append( article.find('a', class_ = 'resultlink' ).get('href') )
            headline.append( article.find('span', class_ = 'Card-title').text )
            date.append( article.find('span', class_ = 'SearchResult-publishedDate' ).text )
            try:
                tag.append( article.find('div', class_ = 'SearchResult-searchResultEyebrow').text )
            except:
                tag.append( 'nan' )
            try:
                description.append( article.find('p', class_ = 'SearchResult-searchResultPreview' ).text )
            except:
                description.append( 'nan' )
            try:
                author.append( article.find('a', class_ = 'SearchResult-author').text )
            except:
                author.append( 'nan' )


        data = pd.DataFrame(
                {
                    'link': link,
                    'headline': headline,
                    'date': date,
                    'description': description,
                    'tag': tag,
                    'author': author
                }
            )

        data['date_retrieved'] = dt.datetime.today()
        data['ticker'] = self.ticker
        data['comments'] = 'nan'
        data['newspaper'] = 'CNBC'

        data['search_term'] = self.keywords

        data['id'] = data['newspaper'] +  data['headline'] + data['link']
        columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'

        data['source'] = source

        data = self._clean_dates(data)

        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


    def nyt(self, datestop = False):

        source = 'nyt'

        url = 'https://www.nytimes.com/search?dropmab=true&query=' + self.keywords.replace(' ', '%20') + '&sort=newest'

        driver = self._load_driver(caps = 'none')

        try:


            # Set and retrive url
            driver.get(url)
            xpath = '//button[@data-testid="search-show-more-button"]'
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            xpath = '//span[@data-testid="todays-date"]'
            element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
            contents = []
            bool = True
            t = 30
            k = 0
            oldnumber = 0
            time.sleep(3)
            while bool:
                try:
                    newnumber = len( driver.find_elements_by_tag_name('li') )
                    if newnumber != oldnumber:
                        k = 0
                        # do it with xpath
                        oldnumber = len( driver.find_elements_by_tag_name('li') )
                        element = driver.find_element_by_xpath('//button[@data-testid="search-show-more-button"]')
                        driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
                        #driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
                        #driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)

                        ActionChains(driver).move_to_element( element).click().perform()
                        time.sleep(random.randint(1,2))
                        #time.sleep(1)
                        newnumber = len( driver.find_elements_by_tag_name('li') )


                        last_date = driver.find_elements_by_xpath('//span[@data-testid="todays-date"]')[-1].text
                        if ',' in last_date:
                            y = last_date.split(' ')[-1]
                        else:
                            y = str( dt.datetime.today().year )
                        try: #because of minute timestamp
                            m = self.months[last_date.split(' ')[0][:3].replace('.', '').replace(',', '').lower()]
                            if len(last_date.split(' ')[1].replace(',', '')) < 2:
                                d = '0' + last_date.split(' ')[1].replace(',', '')
                            else:
                                d = last_date.split(' ')[1].replace(',', '')
                            if datestop:
                                if pd.to_datetime(f'{y}-{m}-{d}', format = '%Y-%m-%d') < pd.to_datetime(datestop):
                                    content = driver.page_source
                                    contents.append( content )
                                    bool = False
                        except:
                            pass

                    k += 1
                    if k > t:
                        content = driver.page_source
                        contents.append( content )

                        #try:
                        #last_date = driver.find_elements_by_tag_name('time')[-1].text
                        last_date = driver.find_elements_by_xpath('//div[@data-testid="todays-date"]')[-1].text

                        if ',' in last_date:
                            y = last_date.split(' ')[-1]
                        else:
                            y = str( dt.datetime.today().year )
                        try: #because of minute timestamp
                            m = self.months[last_date.split(' ')[0][:3].replace('.', '').replace(',', '').lower()]
                            if len(last_date.split(' ')[1].replace(',', '')) < 2:
                                d = '0' + last_date.split(' ')[1].replace(',', '')
                            else:
                                d = last_date.split(' ')[1].replace(',', '')
                            if datestop:
                                if pd.to_datetime(f'{y}-{m}-{d}', format = '%Y-%m-%d') < pd.to_datetime(datestop):
                                    content = driver.page_source
                                    contents.append( content )
                                    bool = False
                        except:
                            pass

                        url = 'https://www.nytimes.com/search?dropmab=true&endDate=' + y + m + d + '&query=' + self.keywords.replace(' ', '%20') + '&sort=newest&startDate=' + '20000101'
                        driver.get(url)
                        time.sleep(1)
                        newnumber = len( driver.find_elements_by_tag_name('li') )
                        k = 0
                        #t = 25
                        #except:
                        #    bool = False
                except:
                    content = driver.page_source
                    contents.append( content )
                    bool = False
            driver.close()
            driver.quit()
        except:
            print('Failed to load data...\n')
            driver.quit()
            return None

        headline, link, date, description, author, tag, comment = [], [], [], [], [], [], []
        for content in contents:
            soup  = bs( content, "lxml" )
            articles  = soup.find_all('li', attrs = {'data-testid': 'search-bodega-result'} )
            for article in articles:
                link.append( article.find('a').get('href') )
                headline.append( article.find('h4').text )
                try:
                    date.append( article.find('span', attrs = { 'data-testid': 'todays-date'}).text )
                except:
                    time.sleep(0.5)
                    date.append( article.find('div', attrs = { 'data-testid': 'todays-date'}).text )
                try:
                    description.append( article.find('p', class_ = 'css-16nhkrn').text )
                except:
                    description.append('nan')
                tag.append( article.find('p', class_ = 'css-myxawk').text )
                try:
                    author.append( article.find('p', class_ = 'css-15w69y9').text.replace('By ', ''))
                except:
                    author.append('nan')
                try:
                    comment.append(article.find('span', class_= 'css-h4mf4').text )
                except:
                    comment.append('nan')
        # clean dates
        data = pd.DataFrame(
                {
                    'link': link,
                    'headline': headline,
                    'date': date,
                    'description': description,
                    'tag': tag,
                    'author': author,
                    'comments': comment
                }
            )

        data.drop_duplicates(inplace = True)

        data['date_retrieved'] = dt.datetime.today()
        data['ticker'] = self.ticker
        data['newspaper'] = 'NYT'
        data['search_term'] = self.keywords
        data['id'] = data['newspaper'] +  data['headline'] + data['link']
        columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'
        data['source'] = source

        data = self._clean_dates(data)


        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data



'''news = NewsData('XOM', 'exxon energy')
datestop = '2021-03-09'
news.head = True
#news.wsj(datestop = datestop)
df = news.seeking_alpha(datestop = datestop)'''




'''
    def reuters(self, datestop = False):

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #                            Reuters
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        source = 'reuters'
        url =  'https://www.reuters.com/search/news?blob=' + self.keywords.replace(' ', '+' ) +  '&sortBy=date&dateRange=all'

        driver = self._load_driver(caps = 'normal')


        try:
            # Set and retrive url
            driver.get(url)

            time.sleep(5)
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="_evidon-barrier-wrapper"]')))
                element = driver.find_element_by_xpath('//div[@id="_evidon-barrier-wrapper"]')
                driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, element)
            except:
                pass
            #_evidon-barrier-wrapper
            try:
                xpath = '//div[@id="onetrust-consent-sdk"]'
                element = driver.find_element_by_xpath(xpath)
                driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, element)
            except:
                pass

            bool = True
            while bool: #newnumber != oldnumber:
                # do it with xpath
                #oldnumber =  len( driver.find_elements_by_xpath('//div[@class="search-result-content"]') )
                try:
                    element = driver.find_element_by_xpath('//div[@class="search-result-more-txt"]')
                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    ActionChains(driver).move_to_element( element).click().perform()
                    time.sleep(random.randint(1,2))
                    time.sleep(2)

                    if datestop:
                        d = driver.find_elements_by_xpath('//h5[@class="search-result-timestamp"]')[-1].get_attribute('innerHTML').split(' ')

                        if dt.datetime(int(d[2]), int(self.months[d[0][:3].lower()]),int(d[1].replace(',',''))) < pd.to_datetime(datestop):
                            bool = False
                    # delete late pop up
                    try:
                        element = driver.find_element_by_xpath('//div[@id="_evidon-barrier-wrapper"]')
                        driver.execute_script("""
                        var element = arguments[0];
                        element.parentNode.removeChild(element);
                        """, element)
                    except:
                        pass

                except:
                    bool = False
                #newnumber =  len( driver.find_elements_by_xpath('//div[@class="search-result-content"]') )
            content = driver.page_source
            driver.close()
            driver.quit()
        except:
            print('Failed to load data...\n')
            driver.quit()
            return None

        headline, link, date, description, author, tag = [], [], [], [], [], []

        soup  = bs( content, "lxml" )
        articles  = soup.find_all('div', class_ = 'search-result-content' )

        for article in articles:
            link.append(article.find('h3').find('a').get('href'))
            headline.append(article.find('h3').text)
            description.append( article.find('div', class_ = 'search-result-excerpt').text.replace('...', '').replace('\n', '').replace('  ', '').strip() )
            date.append( article.find('h5', class_ = "search-result-timestamp").text )

        data = pd.DataFrame(
                {
                    'link': link,
                    'headline': headline,
                    'date': date,
                    'description': description,
                }
            )

        data['date_retrieved'] = dt.datetime.today()
        data['ticker'] = self.ticker
        data['comments'] = 'nan'
        data['author'] = 'nan'
        data['tag'] = 'nan'
        data['comments'] = 'nan'
        data['newspaper'] = 'Reuters'

        data['search_term'] = self.keywords

        data['id'] = data['newspaper'] +  data['headline'] + data['link']
        columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'


        data['source'] = source

        data = self._clean_dates(data)

        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


'''
