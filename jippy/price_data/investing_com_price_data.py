

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


def get_investing_com(url):
    '''
        For popup:
            <i class="popupCloseIcon largeBannerCloser"></i>'
            element = driver.find_element_by_xpath('//i[@class="popupCloseIcon largeBannerCloser"]')
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
            ActionChains(driver).move_to_element(element).click().perform()
    '''
    options = Options()
    options.headless = False
    months = { 'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', \
               'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', \
               'Nov': '11', 'Dec': '12' }
    contents = []

    driver = webdriver.Firefox( executable_path=r'/webdrivers/geckodriver', options = options )
    driver.get(url)
    time.sleep(2)
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
    element.send_keys('01/01/2010')
    driver.find_element_by_xpath('//a[@id="applyBtn"]').click()
    time.sleep(3)
    contents.append(driver.page_source)

    element = driver.find_element_by_xpath( '//div[@class="datePickerWrap calendarDatePicker"]' )
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
    ActionChains(driver).move_to_element(element).click().perform()
    time.sleep(3)
    element = driver.find_element_by_xpath('//input[@id="startDate"]')
    element.clear()
    element.send_keys('01/01/2000')
    driver.find_element_by_xpath('//a[@id="applyBtn"]').click()
    time.sleep(3)
    contents.append(driver.page_source)
    driver.quit()

    date, price, open, high, low, vol, change = [], [], [], [], [], [], []
    for content in contents:
        soup = bs(content, 'lxml')
        tbody   = soup.find('table', class_ = 'historicalTbl')
        rows    = tbody.find_all('tr')
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
                         'low': low, 'volume': vol, 'change': change \
                        } ).drop_duplicates().reset_index(drop = True)

    return df
