
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
import  time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from requests_html import HTMLSession
import re


def earnings_calls(ticker):
    '''

    '''

    url = 'https://www.fool.com/'
    driver = _load_driver(False)
    try:
        driver.get(url)

        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="gdpr-modal-background"]')))
            element = driver.find_element_by_xpath('//div[@id="gdpr-modal-background"]')
            _delete_element(driver, element)
            element = driver.find_element_by_xpath('//div[@id="gdpr-modal-content"]')
            _delete_element(driver, element)
        except:
            pass

        element = driver.find_element_by_xpath('//input[@class="ticker-input-input"]')
        element.clear()
        element.send_keys(ticker)
        element.send_keys(' ')
        time.sleep(0.4)
        element.send_keys(Keys.RETURN)

        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="gdpr-modal-background"]')))
            element = driver.find_element_by_xpath('//div[@id="gdpr-modal-background"]')
            _delete_element(driver, element)
            element = driver.find_element_by_xpath('//div[@id="gdpr-modal-content"]')
            _delete_element(driver, element)
        except:
            pass

        element = driver.find_element_by_xpath('//a[@id="earnings"]')
        _scroll_to_element(driver, element)
        element.click()

        bool = True
        while bool:
            try:
                element = driver.find_element_by_xpath('//div[@id="quote_page_earnings_listing"]//button[@id="load-more"]')
                _scroll_to_element(driver, element)
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
        temp['ticker'] = ticker

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
        temp['link'] = link
        df.append( pd.DataFrame( temp, index = [date] ) )

    df = pd.concat(df)
    df.index = pd.to_datetime(df.index)

    return df


def _load_driver(head):
    options = webdriver.ChromeOptions()
    if not head:
        options.add_argument('--headless')
    driver = webdriver.Chrome( executable_path=r'/Users/PeterlaCour/Documents/Research.nosync/financial_data_project/jippy/jippy/price_data/chromedriver', options = options ) # chromedriver
    driver.set_window_size(1400,1000)
    driver.set_page_load_timeout(1800)
    return driver


def _delete_element(driver, element):
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)

def _scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)




ticker = 'aapl'

df = earnings_calls(ticker)


df.head(5).to_markdown()
