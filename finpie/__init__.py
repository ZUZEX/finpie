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

# Economic data
from finpie.economic_data.oecd_data import OecdData
from finpie.economic_data.eia_data import EiaData
# Fundamental data
from finpie.fundamental_data.finviz import FinvizData
from finpie.fundamental_data.macrotrends import MacrotrendsData
from finpie.fundamental_data.mwatch import MwatchData
from finpie.fundamental_data.yahoo import YahooData
# News data
from finpie.news_data.news import NewsData
# Other data
from finpie.other_data.stock_symbols import global_tickers
from finpie.other_data.stock_symbols import nasdaq_tickers
# Price data
from finpie.price_data.price_data import alpha_vantage_prices
from finpie.price_data.price_data import tingo_prices
from finpie.price_data.price_data import iex_intraday
from finpie.price_data.price_data import yahoo_prices
from finpie.price_data.price_data import yahoo_option_chain
from finpie.price_data.price_data import cboe_option_chain
from finpie.price_data.futures_prices import historical_futures_contracts
from finpie.price_data.futures_prices import futures_contracts


__all__ = [ 'alpha_vantage_prices', 'tingo_prices', 'iex_intraday',
            'yahoo_prices', 'yahoo_option_chain', 'cboe_option_chain'
            'historical_futures_contracts', 'futures_contracts',
            'nasdaq_tickers', 'global_tickers',
            'YahooData', 'MwatchData', 'FinvizData', 'MacrotrendsData',
            'OecdData', 'EiaData', 'NewsData']
