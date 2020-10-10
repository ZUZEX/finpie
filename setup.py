#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# finpie - a simple library to download some financial data
# https://github.com/peterlacour/finpie
#


from setuptools import setup, find_packages
from os import path

# Readme for PyPi
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Requriments
with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(name = 'finpie',
      version = '0.131',
      description = 'Simple library to download some financial data',
      packages = find_packages(),
      install_requires = requirements,
      include_package_data = True,
      author = 'Peter la Cour',
      author_email = 'pe.lacour@gmail.com',
      url = 'https://github.com/peterlacour/finpie',
      license = 'MIT',
      keywords = ['yahoo finance', 'news data', 'company fundamentals',
                  'economic data', 'eia data', 'stock prices', 'option prices' ],
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      zip_safe = True)
