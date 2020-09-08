#!/bin/python3

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Project:      Sentiment
## Title:        Tweets Retrieval
## Author:       Peter la Cour
## Email:        peter.lacour@student.unisg.ch
## Place, Time:  St. Gallen, 05.05.19

## Description:
##
##

## Improvements:
## Last changes:

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
################################################################################

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                                 Setup
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
################################################################################

# Import files

# Load packages
import random
import numpy                    as np
import pandas                   as pd
import datetime                 as dt
from    bs4                                import  BeautifulSoup        as bs
from pyspark.sql import SparkSession
from    selenium           import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.options import Options

import dask.dataframe as dd

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                               Functions
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
################################################################################

# None

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                            Start of Script
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
################################################################################

class CleanText():
    def __init__(self):
        self.months = { 'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', \
                       'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12' }
        self.filterz = [ ' ' ]

    def _format_date( self, date ):
        y = str(date.year)
        if len(str(date.month) ) < 2:
            m = '0' + str(date.month)
        else:
            m = str(date.month)
        if len(str(date.day) ) < 2:
            d = '0' + str(date.day)
        else:
            d =  str(date.day)
        return y, m, d


    def _clean_dates(self, data):

        months = { 'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', \
                       'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12' }
        week_days = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ]

        dayz = [ 'Today', 'Yesterday' ]

        data['Datetime'] = np.nan
        hour = [ (idx, hour.split(' ')[0]) for idx, hour in enumerate(data.Date) if 'hour' in hour.lower() ]
        for i, h in hour:
            data.Datetime.iloc[i] = data.Date_Retrieved.iloc[i] - dt.timedelta( hours = int(h) )

        week = [ (idx, w.split(' ')[1:]) for idx, w in enumerate(data.Date) if any(wd in w.split(' ')[0] for wd in week_days) ]
        for i, w in week:
            if len(w) == 2:
                data.loc[i, 'Datetime'] = pd.to_datetime( w[1].replace(',', '')  + '/' + months[w[0][:3].lower()] + '/' + str(dt.datetime.today().year), format = '%d/%m/%Y' )
            else:
                data.loc[i, 'Datetime'] = pd.to_datetime( w[1].replace(',', '')  + '/' + months[w[0][:3].lower()] + '/' + str(w[2]), format = '%d/%m/%Y' )

        day = [ (idx, w.split(' ')[0].replace(',', '')) for idx, w in enumerate(data.Date) if any(wd in w.split(' ')[0].replace(',', '') for wd in dayz) ]
        for i, w in day:
            if w == 'Today':
                data.Datetime.iloc[i] = pd.to_datetime( dt.datetime.strftime(dt.datetime.today(),  format = '%d/%m/%Y'), format = '%d/%m/%Y' )
            elif w == 'Yesterday':
                data.Datetime.iloc[i] = pd.to_datetime( dt.datetime.strftime(dt.datetime.today() - dt.timedelta(days = 1),  format = '%d/%m/%Y'), format = '%d/%m/%Y' )

        hes = [ (idx, hour.split(' ')[0]) for idx, hour in enumerate(data.Date) if 'h ago' in hour.lower() ]
        for i, h in hes:
            data.Datetime.iloc[i] = data.Date_Retrieved.iloc[i] - dt.timedelta( hours = int(h.replace('h', '')) )


        for source in np.unique(data.Source):
            if source == 'sa':
                pass
            elif source == 'nyt':
                yes = [ (idx, d.split(' ')[:2]) for idx, d in enumerate(data.Date) if len(d.split(' ')[-1]) < 3 ]
                for i, y in yes:
                    data.Datetime.iloc[i] = pd.to_datetime( y[1] + '/' + months[y[0][:3].lower()] + '/' + str(dt.datetime.today().year), format = '%d/%m/%Y')
            elif source in ['ft', 'bloomberg']:
                data['Datetime'][ data.Source == source ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[-1] \
                                                                                             for d in data[ data.Source == source ].Date ], format = '%d/%m/%Y' ))
            elif source in ['barrons', 'wsj']:
                data['Datetime'][ data.Source == source ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[2] \
                                                                                                     for d in data[ data.Source == source ].Date ], format = '%d/%m/%Y' ))
            elif source == 'reuters':
                data['Datetime'][ data.Source == source ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[2] \
                                                                                                     for d in data[ data.Source == source ].Date ], format = '%d/%m/%Y' ))
            elif source == 'cnbc':
                data['Datetime'][ data.Source == source ] = list(pd.to_datetime( [ d.split(' ')[0].split('/')[1] + '/' + d.split(' ')[0].split('/')[0] + '/' + d.split(' ')[0].split('/')[2] \
                                                                                                     for d in data[ data.Source == source ].Date ], format = '%d/%m/%Y' ))
        data.Datetime = data.Datetime.dt.strftime('%d/%m/%Y')
        return data



    def _clean_duplicates(self, data):

        columns = [ col for col in data.columns if col != 'Date_Retrieved' ]
        data.drop_duplicates(columns, inplace = True)
        data.reset_index(drop = True, inplace = True)

        return data


    def filter_data(self, data):

        filtered = []
        for i, n in enumerate(data.Headline):
            for f in self.filterz:
                if f in n.lower():
                    filtered.append( data.ID.iloc[i] )
                elif f in data.Description.iloc[i].lower():
                    filtered.append( data.ID.iloc[i] )
                else:
                    continue

        data = data[ data.ID.isin(filtered) ]
        data.reset_index(drop = True, inplace = True)

        return data



class newsData(CleanText):
    def __init__(self, ticker, keywords, head = False, verbose = False):
        super().__init__()
        self.ticker = ticker
        self.keywords = keywords
        self.head = head
        self.verbose = verbose
    #########################################################################
    # initial news scrapes
    #########################################################################

    def _load_driver(self):
        options = webdriver.ChromeOptions()
        if not self.head:
            options.add_argument('--headless')
        driver = webdriver.Chrome( executable_path=r'/Users/PeterlaCour/Documents/Research.nosync/financial_data_project/jippy/jippy/price_data/chromedriver', options = options ) # chromedriver
        driver.set_window_size(1400,1000)
        driver.set_page_load_timeout(1800)
        return driver

    def ft( self, ):
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
                    headline.append( article.find('div', class_ = 'o-teaser__heading' ).text )
                    link.append( article.find('div', class_ = 'o-teaser__heading' ).find('a').get('href') )
                    try:
                        description.append( article.find('p', class_ = 'o-teaser__standfirst' ).text )
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


        driver = self._load_driver()


        # Set and retrive url
        driver.get(url)
        co = 0
        _delete_elements(driver)

        driver.find_elements_by_xpath('//a[@data-trackable="sort-item"]')[1].click()
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
                    _delete_elements(driver)
                    contents.append( bs( driver.page_source, "lxml" ).find_all('div', class_ = 'o-teaser__content' ) )
                    co += 1
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
                    y, m, d = self._format_date(dte)
                    url = 'https://www.ft.com/search?q=' + self.keywords.replace(' ', '%20') + '&dateTo=' + y + '-' + m + '-' + d + '&sort=date&expandRefinements=true'
                    driver.get( url )
                    driver.find_elements_by_xpath('//a[@data-trackable="sort-item"]')[1].click()
                    _delete_elements(driver)
                    contents.append( bs( driver.page_source, "lxml" ).find_all('div', class_ = 'o-teaser__content' ) )
                    co += 1
                except:
                    break
        driver.close()
        driver.quit()

        headline, link, date, description, author, tag = [], [], [], [], [], []
        headline, link, date, description, author, tag = _get_articles(contents, headline, link, date, description, author, tag)

        contents = None

        data = pd.DataFrame(
                {
                    'Link': link,
                    'Headline': headline,
                    'Date': date,
                    'Description': description,
                    'Tag': tag
                }
            )
        data['Date_Retrieved'] = dt.datetime.today()
        data['Ticker'] = self.ticker
        data['Comments'] = 'nan'
        data['Author'] = 'nan'
        data['Newspaper'] = 'FT'
        data['Search_term'] = self.keywords
        data['ID'] = data['Newspaper'] +  data['Headline'] + data['Link']
        columns = [ 'Link', 'Headline', 'Date', 'Description', 'Date_Retrieved', 'Author', 'Tag', 'Newspaper', 'Comments', 'Ticker', 'Search_term', 'ID' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'

        headline, link, date, description, author, tag  = [], [], [], [], [], []
        #soup = None

        data['Source'] = source

        data.drop_duplicates(inplace = True)

        data = self._clean_dates(data)
        # write to parquet file with ticker as partition

        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)
        return data



    def wsj( self ):

        source = 'wsj'

        # change to date today
        td_1 = dt.datetime.today() - dt.timedelta(days = 320)
        y, m, d = self._format_date(td_1)
        start_date = y + '/' + m + '/' + d
        td_2 = dt.datetime.today()
        y, m, d = self._format_date(td_2)
        end_date = y + '/' + m + '/' + d

        url = 'https://www.wsj.com/search/term.html?KEYWORDS=' + self.keywords.replace(' ', '%20')  + '&min-date=' + start_date + '&max-date=' + end_date + '&isAdvanced=true&daysback=4y&andor=AND&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,press,newswire,wsjpro'

        driver = self._load_driver()

        # Set and retrive url
        driver.get(url)
        contents = []
        max = int( driver.find_element_by_xpath('//div[@class="results-menu-wrapper bottom"]//li[@class="results-count"]').text.replace('of ', '') )
        contents.append(driver.page_source)
        for i in range(max-1):
            try:
                time.sleep(random.randint(0,2))
                driver.find_element_by_xpath('//li[@class="next-page"]/a').click()
                contents.append(driver.page_source)
            except:
                driver.refresh()
                driver.find_element_by_xpath('//li[@class="next-page"]/a').click()
                contents.append(driver.page_source)
            # Record progress
            #_print_progress(i, max-1)
        contents.append(driver.page_source)

        bool = True
        while bool:
            try:
                td_2 = td_1
                y, m, d = self._format_date(td_2)
                start_date = y + '/' + m + '/' + d
                td_1 = td_1 - dt.timedelta(days = 320)
                y, m, d = self._format_date(td_1)
                end_date = y + '/' + m + '/' + d

                url = 'https://www.wsj.com/search/term.html?KEYWORDS=' + self.keywords.replace(' ', '%20')  + '&min-date=' + end_date + '&max-date=' + start_date + '&isAdvanced=true&daysback=4y&andor=AND&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,press,newswire,wsjpro'
                driver.get(url)
                max = int( driver.find_element_by_xpath('//div[@class="results-menu-wrapper bottom"]//li[@class="results-count"]').text.replace('of ', '') )
                contents.append(driver.page_source)
                for i in range(max-1):
                    try:
                        time.sleep(random.randint(0,2))
                        driver.find_element_by_xpath('//li[@class="next-page"]/a').click()
                        contents.append(driver.page_source)
                    except:
                        driver.refresh()
                        driver.find_element_by_xpath('//li[@class="next-page"]/a').click()
                        contents.append(driver.page_source)
            except:
                bool = False

        driver.close()
        driver.quit()

        headline, link, date, description, author, tag = [], [], [], [], [], []

        for content in contents:
            soup  = bs( content, "lxml" )
            articles  = soup.find_all('div', class_ = 'headline-item' )
            for article in articles:
                headline.append( article.find('h3').text.strip() )
                link.append( article.find('h3').find('a').get('href') )
                tag.append( article.find('a').text )
                date.append( article.find('time').text )
                try:
                    author.append( article.find('li', class_ = 'byline').text.replace('By', '').strip() )
                except:
                    author.append( 'nan' )
                try:
                    description.append( article.find('div', class_ = 'summary-container').text.strip() )
                except:
                    description.append( 'nan' )

        data = pd.DataFrame(
                {
                    'Link': link,
                    'Headline': headline,
                    'Date': date,
                    'Description': description,
                    'Author': author,
                    'Tag': tag
                }
            )

        data['Date_Retrieved'] = dt.datetime.today()
        data['Ticker'] = self.ticker
        data['Newspaper'] = 'WSJ'
        data['Search_term'] = self.keywords

        data['ID'] = data['Newspaper'] +  data['Headline'] + data['Link']
        columns = [ 'Link', 'Headline', 'Date', 'Description', 'Date_Retrieved', 'Author', 'Tag', 'Newspaper', 'Comments', 'Ticker', 'Search_term', 'ID' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'


        data = self._clean_dates(data)
        # write to parquet file with ticker as partition

        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


    def seeking_alpha(self):
        # Note: might be stopping scrape too early

        source = 'sa'
        url = f'https://seekingalpha.com/symbol/{self.ticker}/news'
        driver = self._load_driver()

        # Set and retrive url
        driver.get(url)

        k = 0
        t = 20
        SCROLL_PAUSE_TIME = 0.9

        while k < t:
            k = 0
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

            while new_number == last_number:

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
                    comments.append( '0 Comments' )
            except:
                continue


        df_news = pd.DataFrame(
                {
                    'Link': link,
                    'Headline': headline,
                    'Date': date,
                    'Author': author,
                    'Comments': comments
                }
            )

        df_news['Date_Retrieved'] = dt.datetime.today()
        df_news['Ticker'] = self.ticker
        df_news['Description'] = 'nan'
        df_news['Tag'] = 'nan'
        df_news['Newspaper'] = 'SA - News'


        data = df_news.copy()
        data['Search_term'] = self.keywords

        data['ID'] = data['Newspaper'] +  data['Headline'] + data['Link']
        columns = [ 'Link', 'Headline', 'Date', 'Description', 'Date_Retrieved', 'Author', 'Tag', 'Newspaper', 'Comments', 'Ticker', 'Search_term', 'ID' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'

        headline, link, date, author, comments = [], [], [], [], []
        df_news = None
        articles = None
        soup = None

        data['Source'] = source

        data = self._clean_dates(data)


        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


    def barrons(self):

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #                            Barrons
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # problem with older data having concatenated strings in their headlines
        source = 'barrons'
        url = 'https://www.barrons.com/search?keyword=' + self.keywords + '&numResults=75&sort=date-desc&author=&searchWindow=0&minDate=&maxDate=&source=barrons&source=other&source=press'

        driver = self._load_driver()

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
            except:
                bool = False

        driver.close()
        driver.quit()

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
                    'Link': link,
                    'Headline': headline,
                    'Date': date,
                    'Description': description,
                    'Newspaper': newspaper,
                    'Author': author
                }
            )

        headline, link, date, description, author, tag = [], [], [], [], [], []
        contents = None

        data['Date_Retrieved'] = dt.datetime.today()
        data['Ticker'] = self.ticker
        data['Comments'] = 'nan'
        data['Tag'] = 'nan'

        data['Search_term'] = self.keywords


        data['ID'] = data['Newspaper'] +  data['Headline'] + data['Link']
        columns = [ 'Link', 'Headline', 'Date', 'Description', 'Date_Retrieved', 'Author', 'Tag', 'Newspaper', 'Comments', 'Ticker', 'Search_term', 'ID' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'
        data['Source'] = source

        data = self._clean_dates(data)


        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


    def bloomberg(self):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #                            Bloomberg
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        source = 'bloomberg'
        url = 'https://www.bloomberg.com/search?query='  + self.keywords.replace(' ', '%20')

        driver = self._load_driver()
        # Set and retrive url
        driver.get(url)

        time.sleep(3)

        try:
            driver.execute_script("""
                    var element = arguments[0];
                    element.parentNode.removeChild(element);
                    """, driver.find_element_by_class_name('truste_box_overlay') )
        except:
            pass

        try:
            driver.execute_script("""
                    var element = arguments[0];
                    element.parentNode.removeChild(element);
                    """, driver.find_element_by_class_name('truste_overlay') )
        except:
            pass


        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="truste-consent-track"]')))
        element = driver.find_element_by_xpath('//div[@id="truste-consent-track"]')
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

        # click sorting thing

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #driver.find_elements_by_class_name('link__a4d2830d ')[7].click()

        element = driver.find_element_by_tag_name('head')
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

        k = 0
        while k < 50:
            bool = True
            new_height = 0
            while bool: #newnumber != oldnumber:
                # do it with xpath
                #oldnumber =  len( driver.find_elements_by_xpath('//div[@class="search-result-content"]') )
                try:
                    element = driver.find_element_by_xpath('//button[@title="Load More Results"]')
                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    element.click()
                    #ActionChains(driver).move_to_element( element).click().perform()
                    #time.sleep(random.randint(1,2))
                    time.sleep( 0.25 )
                    k = 0
                except:
                    bool = False

                    elements = driver.find_elements_by_tag_name('img')
                    for element in elements:
                        driver.execute_script("""
                        var element = arguments[0];
                        element.parentNode.removeChild(element);
                        """, element)

                    k += 1
                    time.sleep(0.5)


        content = driver.page_source

        driver.close()
        driver.quit()

        headline, link, date, description, author, tag = [], [], [], [], [], []

        soup  = bs( content, "lxml" )
        articles  = soup.find_all('div', class_ = 'storyItem__192ee8af' )

        for article in articles:
            link.append( article.find('a').get('href') )
            headline.append( article.find('a', class_ = 'headline__55bd5397').text )
            date.append( article.find('div', class_ = 'publishedAt__79f8aaad' ).text )
            tag.append( article.find('div', class_ = 'eyebrow__4b7f0542').text )
            try:
                description.append( article.find('a', class_ = 'summary__bbda15b4' ).text )
            except:
                description.append( 'nan' )
            try:
                author.append( article.find('div', class_ = 'summary__bbda15b4').text.replace('By ', '') )
            except:
                author.append( 'nan' )


        data = pd.DataFrame(
                {
                    'Link': link,
                    'Headline': headline,
                    'Date': date,
                    'Description': description,
                    'Tag': tag,
                    'Author': author
                }
            )

        data['Date_Retrieved'] = dt.datetime.today()
        data['Ticker'] = self.ticker
        data['Comments'] = 'nan'
        data['Newspaper'] = 'Bloomberg'

        data['Search_term'] = self.keywords

        data['ID'] = data['Newspaper'] +  data['Headline'] + data['Link']
        columns = [ 'Link', 'Headline', 'Date', 'Description', 'Date_Retrieved', 'Author', 'Tag', 'Newspaper', 'Comments', 'Ticker', 'Search_term', 'ID' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'

        data['Source'] = source

        data = self._clean_dates(data)


        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


    def reuters(self):

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #                            Reuters
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        source = 'reuters'
        url =  'https://www.reuters.com/search/news?blob=' + self.keywords.replace(' ', '+' ) +  '&sortBy=date&dateRange=all'

        driver = self._load_driver()

        # Set and retrive url
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_xpath('//button[@id="_evidon-banner-acceptbutton"]').click()

        bool = True
        while bool: #newnumber != oldnumber:
            # do it with xpath
            #oldnumber =  len( driver.find_elements_by_xpath('//div[@class="search-result-content"]') )
            try:
                element = driver.find_element_by_xpath('//div[@class="search-result-more-txt"]')
                driver.execute_script("arguments[0].scrollIntoView();", element)
                ActionChains(driver).move_to_element( element).click().perform()
                time.sleep(random.randint(1,2))
                time.sleep(5)
            except:
                bool = False
            #newnumber =  len( driver.find_elements_by_xpath('//div[@class="search-result-content"]') )
        content = driver.page_source
        driver.close()
        driver.quit()
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
                    'Link': link,
                    'Headline': headline,
                    'Date': date,
                    'Description': description,
                }
            )

        data['Date_Retrieved'] = dt.datetime.today()
        data['Ticker'] = self.ticker
        data['Comments'] = 'nan'
        data['Author'] = 'nan'
        data['Tag'] = 'nan'
        data['Comments'] = 'nan'
        data['Newspaper'] = 'Reuters'

        data['Search_term'] = self.keywords

        data['ID'] = data['Newspaper'] +  data['Headline'] + data['Link']
        columns = [ 'Link', 'Headline', 'Date', 'Description', 'Date_Retrieved', 'Author', 'Tag', 'Newspaper', 'Comments', 'Ticker', 'Search_term', 'ID' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'


        data['Source'] = source

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

        driver = self._load_driver()

        # Set and retrive url
        driver.get(url)

        # close popup
        time.sleep(8)

        try:
            element = driver.find_element_by_xpath('//div[@id="sortdate"]')
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
            ActionChains(driver).move_to_element( element).click().perform()
        except:
            pass

        element = driver.find_element_by_tag_name('head')
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

        k = 0
        t = 100
        SCROLL_PAUSE_TIME = 0.5
        while k < t:
            k = 0

            if datestop:
                element = driver.find_elements_by_xpath('//span[@class="SearchResult-publishedDate"]')[-1].text
                element = pd.to_datetime( element.split(' ')[0], format = '%m/%d/%Y' )
                if element < pd.to_datetime(datestop, format = '%d/%m/%Y'):
                    k = 101
                    break
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
                    if element < pd.to_datetime(datestop, format = '%d/%m/%Y'):
                        k = 101
                        break
                k += 1
                if k >= t:
                    break
                time.sleep(random.randint(0,2) * 0.43)
        content = driver.page_source
        driver.close()
        driver.quit()

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
                    'Link': link,
                    'Headline': headline,
                    'Date': date,
                    'Description': description,
                    'Tag': tag,
                    'Author': author
                }
            )

        data['Date_Retrieved'] = dt.datetime.today()
        data['Ticker'] = self.ticker
        data['Comments'] = 'nan'
        data['Newspaper'] = 'CNBC'

        data['Search_term'] = self.keywords

        data['ID'] = data['Newspaper'] +  data['Headline'] + data['Link']
        columns = [ 'Link', 'Headline', 'Date', 'Description', 'Date_Retrieved', 'Author', 'Tag', 'Newspaper', 'Comments', 'Ticker', 'Search_term', 'ID' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'

        data['Source'] = source

        data = self._clean_dates(data)

        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data


    def nyt(self):

        source = 'nyt'

        months = { 'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', \
                       'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12' }

        url = 'https://www.nytimes.com/search?dropmab=true&query=' + self.keywords.replace(' ', '%20') + '&sort=newest'

        driver = self._load_driver()

        # Set and retrive url
        driver.get(url)

        contents = []
        bool = True
        t = 30
        k = 0
        oldnumber = 0

        while bool:
            try:
                newnumber = len( driver.find_elements_by_tag_name('li') )
                if newnumber != oldnumber:
                    k = 0
                    # do it with xpath
                    oldnumber = len( driver.find_elements_by_tag_name('li') )
                    element = driver.find_element_by_xpath('//button[@data-testid="search-show-more-button"]')
                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    ActionChains(driver).move_to_element( element).click().perform()
                    time.sleep(random.randint(1,2))
                    #time.sleep(1)
                    newnumber = len( driver.find_elements_by_tag_name('li') )
                k += 1
                if k > t:
                    content = driver.page_source
                    contents.append( content )

                    try:
                        last_date = driver.find_elements_by_tag_name('time')[-1].text
                        y = last_date.split(' ')[-1]
                        m = months[last_date.split(' ')[0][:3].replace('.', '').replace(',', '').lower()]
                        if len(last_date.split(' ')[1].replace(',', '')) < 2:
                            d = '0' + last_date.split(' ')[1].replace(',', '')
                        else:
                            d = last_date.split(' ')[1].replace(',', '')
                        url = 'https://www.nytimes.com/search?dropmab=true&endDate=' + y + m + d + '&query=' + self.keywords.replace(' ', '%20') + '&sort=newest&startDate=' + '20000101'
                        driver.get(url)
                        time.sleep(1)
                        newnumber = len( driver.find_elements_by_tag_name('li') )
                        k = 0
                        t = 25
                    except:
                        bool = False
            except:
                content = driver.page_source
                contents.append( content )
                bool = False
        driver.close()
        driver.quit()

        headline, link, date, description, author, tag, comment = [], [], [], [], [], [], []

        for content in contents:
            soup  = bs( content, "lxml" )
            articles  = soup.find_all('li', attrs = {'data-testid': 'search-bodega-result'} )
            for article in articles:
                link.append( article.find('a').get('href') )
                headline.append( article.find('h4').text )
                date.append( article.find('time').text )
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
                    'Link': link,
                    'Headline': headline,
                    'Date': date,
                    'Description': description,
                    'Tag': tag,
                    'Author': author,
                    'Comments': comment
                }
            )

        data.drop_duplicates(inplace = True)
        data['Date_Retrieved'] = dt.datetime.today()
        data['Ticker'] = self.ticker
        data['Newspaper'] = 'NYT'
        data['Search_term'] = self.keywords
        data['ID'] = data['Newspaper'] +  data['Headline'] + data['Link']
        columns = [ 'Link', 'Headline', 'Date', 'Description', 'Date_Retrieved', 'Author', 'Tag', 'Newspaper', 'Comments', 'Ticker', 'Search_term', 'ID' ]
        for col in columns:
            if col not in data.columns:
                data[col] = 'nan'
        data['Source'] = source

        data = self._clean_dates(data)


        if self.verbose:
            print('-' * 78)
            print(source.upper(), 'done.', len(data), 'articles collected.')
            print('-' * 78)

        return data
