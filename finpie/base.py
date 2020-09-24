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

import os
import sys
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DataBase(object):
	def __init__(self):
		self.head = False
		self.download_path = os.getcwd()
		self.chromedriver_path = os.path.dirname(__file__)


	def _get_chromedriver_path(self):

		filepath = self.chromedriver_path
		if '/' in filepath:
			filepath = '/'.join( filepath.split('/')) + '/webdrivers/'
		elif '\\' in filepath:
			filepath = '\\'.join( filepath.split('\\')) + '\\webdrivers\\'
		return filepath


	def _get_chromedriver(self):

		filepath = self._get_chromedriver_path()
		if sys.platform == 'darwin':
			return filepath + 'chromedriver_mac'
		elif 'win' in sys.platform:
			return filepath + 'chromedriver_windows.exe'


	def _load_driver(self, caps = 'none'):

		options = webdriver.ChromeOptions()
		prefs = {}
		prefs['profile.default_content_settings.popups'] = 0
		prefs['download.default_directory'] = self.download_path
		prefs['profile.default_content_setting_values.automatic_downloads'] =  1
		options.add_experimental_option('prefs', prefs)
		options.add_experimental_option("excludeSwitches", ['enable-automation'])
		options.add_experimental_option('useAutomationExtension', False)

		options.add_argument('--no-sandbox')
		options.add_argument('--disable-setuid-sandbox')
		options.add_argument('--start-maximized')

		user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'
		options.add_argument(f'user-agent={user_agent}')

		if not self.head:
			options.add_argument('--headless')
		try:
			if caps == 'none':
				caps = DesiredCapabilities().CHROME
				caps["pageLoadStrategy"] = "none"
				driver = webdriver.Chrome( executable_path=self._get_chromedriver(), options = options, desired_capabilities=caps ) # chromedriver
			else:
				caps = DesiredCapabilities().CHROME
				caps["pageLoadStrategy"] = "normal"
				driver = webdriver.Chrome( executable_path=self._get_chromedriver(), options = options, desired_capabilities=caps ) # chromedriver

			driver.execute_script(f"var s=window.document.createElement('script'); s.src='{self._get_chromedriver_path}javascriptM.js';window.document.head.appendChild(s);")

			driver.set_window_size(1400,1000)
			driver.set_page_load_timeout(600)
			driver.delete_all_cookies()

		except Exception as e:
			print('Failed to start driver: ' + str(e) )
			if 'chrome not reachable' in str(e):
				print('Try turning off your firewall...')

		return driver

	def _get_session(self, url):
		'''
		...
		'''
		session = HTMLSession()
		r = session.get(url)
		soup = bs(r.content, 'html5lib')
		return soup


	def _downloads_done(self, filename):
		'''
		https://stackoverflow.com/questions/48263317/selenium-python-waiting-for-a-download-process-to-complete-using-chrome-web
		'''

		bool = True
		while bool:
			if filename not in os.listdir(self.download_path):
				time.sleep(0.5)
				#self._downloads_done(filename)
			else:
				bool = False
		return None


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
