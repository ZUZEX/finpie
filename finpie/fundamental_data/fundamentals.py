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

from .finviz import FinvizData
from .macrotrends import MacrotrendsData
from .mwatch import MwatchData
from .yahoo import YahooData
from .fool import Earnings

class FundamentalsClassA(FinvizData, MacrotrendsData, YahooData, Earnings):

    def __init__(self, ticker, freq = 'A', source = 'macrotrends'):
        self.ticker = ticker
        self.freq = freq
        FinvizData.__init__(self, self.ticker)
        YahooData.__init__(self, self.ticker)
        Earnings.__init__(self, self.ticker)
        MacrotrendsData.__init__(self, self.ticker, self.freq)

class FundamentalsClassB(YahooData, FinvizData, Earnings):

    def __init__(self, ticker, freq = 'A'):
        self.ticker = ticker
        self.freq = freq
        FinvizData.__init__(self, self.ticker)
        YahooData.__init__(self, self.ticker)
        Earnings.__init__(self, self.ticker)
        MacrotrendsData.__init__(self, self.ticker, self.freq)

class FundamentalsClassC(FinvizData, MwatchData, YahooData, Earnings):

    def __init__(self, ticker, freq = 'A', source = 'macrotrends'):
        self.ticker = ticker
        self.freq = freq
        FinvizData.__init__(self, self.ticker)
        YahooData.__init__(self, self.ticker)
        Earnings.__init__(self, self.ticker)
        MwatchData.__init__(self, self.ticker, self.freq)


def Fundamentals( ticker, source = 'macrotrends', freq = 'A' ):
    if source == 'macrotrends':
        return FundamentalsClassA(ticker, freq)
    elif source == 'yahoo':
        return FundamentalsClassB(ticker, freq)
    elif source == 'marketwatch':
        return FundamentalsClassC(ticker, freq)
