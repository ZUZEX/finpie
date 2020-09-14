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


import pandas as pd


class oecdData(object):

    def __init__(self, country_code = 'all', freq = 'Q', currency_code = 'CXCU'):

        '''currency_code options:
            'CXCU', dollar converted (default)
            'CXCUSA', dollar converted seasonally adjusted
            'NCCU': national currency
            'NCCUSA': national currency seasonally adjusted

            freq options:
                'M', monthly
                'Q', quarterly (default)
                'A', annually


            Only for trade indicators:
                'NCML', national currency monthly level
                'NCMLSA', national currency monthly level seasonally adjusted
                'CXML', dollar converted monthly level
                'CXMLSA', dollar converted monthly level seasonally adjusted

            other codes...
            IXOB, index
            IXOBSA, index seasonally adjusted
            IXNSA, normalised index seasonally adjusted
            ST, rate or level
            STSA, rate or level seasonally adjusted
            GY, growth rate
            GYSA, growth rate seasonally adjusted
            ML, monthly level
            QL, quarterly level
            BLSA, balanced level seasonally adjusted
        '''

        self.country_code = country_code
        self.freq = freq
        self.currency_code = currency_code

        # seasnonally adjusted or not..
        # index levels or rates...
        # monthly or quarterly levels

    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - oced current account  - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

    def current_account(self, percent_of_gdp = False):
        if percent_of_gdp:
            code1 = 'B6BLTT02'
            code2 = f'.STSA.{self.freq}'
        else:
            code1 = 'B6BLTT01'
            code2 = f'.{self.currency_code}.{self.freq}'
        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_BOP6/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}')
        else:
            df = self._get_oecd(f'MEI_BOP6/{code1}.{self.country_code.upper()}{code2}')
        return df

    def goods_balance(self, xm = 'balance'):
        if xm.lower() == 'exports':
            code1 = 'B6CRTD01'
        elif xm.lower() == 'imports':
            code1 = 'B6DBTD01'
        else:
            code1 = 'B6BLTD01'
        code2 = f'.{self.currency_code}.{self.freq}'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_BOP6/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}')
        else:
            df = self._get_oecd(f'MEI_BOP6/{code1}.{self.country_code.upper()}{code2}')
        return df

    def services_balance(self, xm = 'balance'):
        if xm.lower() == 'exports':
            code1 = 'B6CRSE01'
        elif xm.lower() == 'imports':
            code1 = 'B6DBSE01'
        else:
            code1 = 'B6BLSE01'
        code2 = f'.{self.currency_code}.{self.freq}'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_BOP6/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}')
        else:
            df = self._get_oecd(f'MEI_BOP6/{code1}.{self.country_code.upper()}{code2}')
        return df


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - oced financial account  - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

    def financial_account(self, assets_or_liabs = None):
        '''

        '''
        codes = [ 'B6FATC01', 'B6FATD01', 'B6FATT01' ]
        return self._fa_helper(codes, assets_or_liabs)

    def direct_investment(self, assets_or_liabs = None):
        '''

        '''
        codes = [ 'B6FADI02', 'B6FADI03', 'B6FADI01' ]
        return self._fa_helper(codes, assets_or_liabs)

    def portfolio_investment(self, assets_or_liabs = None):
        '''

        '''
        codes = [ 'B6FAPI02', 'B6FAPI03', 'B6FAPI10' ]
        return self._fa_helper(codes, assets_or_liabs)


    def other_investment(self, assets_or_liabs = None):
        '''

        '''
        codes = [ 'B6FAOI02', 'B6FAOI03', 'B6FAOI01' ]
        return self._fa_helper(codes, assets_or_liabs)

    def financial_derivatives(self):
        '''

        '''
        assets_or_liabs = None
        codes = ['B6FAFD01', 'B6FAFD01', 'B6FAFD01']
        return self._fa_helper(codes, assets_or_liabs)

    def reserve_assets(self):
        '''

        '''
        assets_or_liabs = None
        codes = ['B6FARA01', 'B6FARA01', 'B6FARA01']
        return self._fa_helper(codes, assets_or_liabs)


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - -  oecd composite leading indicators - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


    def cli(self, subject = 'amplitude'):
        '''
        url: https://stats.oecd.org/Index.aspx?DataSetCode=MEI_CLI

        options:
            default: amplitude adjusted (cli) - LOLITOAA
            normalised (cli) - LOLITONO
            trend restored (cli) - LOLITOTR_STSA
            12-month rate of change of the trend restored (CLI) - LOLITOTR_GYSA
            OECD standardised BCI, amplitude adjusted - BSCICP03
            OECD standardised CCI, amplitude adjusted - CSCICP03
            ratio to trend (gdp) - LORSGPRT
            normalised ( gdp ) - LORSGPNO
            trend ( gdp ) - LORSGPTD
            original seasonally adjusted (gdp) - LORSGPOR_IXOBSA
        '''
        if subject == 'amplitude':
            code1 = 'LOLITOAA'
        else:
            code1 = subject
        code2 = f'.{self.freq}'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_CLI/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                            measure = False)
        else:
            df = self._get_oecd(f'MEI_CLI/{code1}.{self.country_code.upper()}{code2}',
                            measure = False)
        return df



    def cci(self):
        code1 = 'CSCICP03'
        code2 = f'.{self.freq}'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_CLI/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                            measure = False)
        else:
            df = self._get_oecd(f'MEI_CLI/{code1}.{self.country_code.upper()}{code2}',
                            measure = False)
        return df



    def bci(self):
        code1 = 'BSCICP03'
        code2 = f'.{self.freq}'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_CLI/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                            measure = False)
        else:
            df = self._get_oecd(f'MEI_CLI/{code1}.{self.country_code.upper()}{code2}',
                            measure = False)
        return df


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - -oecd business tendency survey - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -



    def economic_situation_survey( self ):

        code1 = 'CSESFT'
        code2 = f'.BLSA.{self.freq.upper()}'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_BTS_COS/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                            measure = False)
        else:
            df = self._get_oecd(f'MEI_BTS_COS/{code1}.{self.country_code.upper()}{code2}',
                            measure = False)
        return df


    def consumer_confidence_survey( self ):

        code1 = 'CSCICP02'
        code2 = f'.BLSA.{self.freq.upper()}'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_BTS_COS/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                            measure = False)
        else:
            df = self._get_oecd(f'MEI_BTS_COS/{code1}.{self.country_code.upper()}{code2}',
                            measure = False)
        return df


    def consumer_price_inflation_survey( self ):
        code1 = 'CSINFT'
        code2 = f'.BLSA.{self.freq.upper()}'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_BTS_COS/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                            measure = False)
        else:
            df = self._get_oecd(f'MEI_BTS_COS/{code1}.{self.country_code.upper()}{code2}',
                            measure = False)
        return df


    # TO DO:
    # BUSINESS TENDENCY SURVEYS
    # # https://stats.oecd.org/restsdmx/sdmx.ashx/GetData/MEI_BTS_COS/BS+BSPR+BSPRTE+BSPRFT+BSFG+BSFGLV+BSOB+BSOBLV+BSOI+BSOITE+BSXR+BSXRLV+BSSP+BSSPFT+BSEM+BSEMFT+BSCU+BSCURT+BSBU+BSBUCT+BSCI+BC+BCBU+BCBUTE+BCCI+BCOB+BCOBLV+BCEM+BCEMFT+BCSP+BCSPFT+BR+BRBU+BRBUTE+BRBUFT+BRCI+BRVS+BRVSLV+BREM+BREMFT+BROD+BRODFT+BV+BVBU+BVBUTE+BVCI+BVDE+BVDETE+BVDEFT+BVEM+BVEMTE+BVEMFT+BN+BNBU+BNBUCT+BNBUFT+BNRM+BNRMTE+BNEM+BNEMTE+BNEMFT+BNOD+BNODTE.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ISR+ITA+JPN+KOR+LVA+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+NMEC+BRA+CHN+IND+IDN+RUS+ZAF.BLSA.{self.freq}+M/all?startTime=2019-Q1&endTime=2020-Q3


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - oecd main economic indicators - - - - - - - - - - - - -
    #          https://stats.oecd.org/Index.aspx?DataSetCode=MEI_CLI#
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # business tendency and consumer opinion
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

    def business_tendency_survey(self, sector):
        '''

        '''
        if sector == 'retail':
            code1 = 'BRCICP02'
        elif sector == 'construction':
            code1 = 'BCCICP02'
        elif sector == 'services':
            code1 = 'BVCICP02'
        elif sector == 'manufacturing':
            code1 = 'BSCICP02'
            # can add oecd indicator
        code2 = f'.STSA+IXNSA.{self.freq}' # normalised or rate/level

        return self._main_indicator_helper(code1, code2)


    def consumer_opinion_survey( self, measure = 'national'):
        '''

        '''
        if measure == 'oecd':
            code1 = 'CSCICP03'
        else:
            code1 = 'CSCICP02'
        code2 = f'.STSA+IXNSA.{self.freq}'

        return self._main_indicator_helper(code1, code2)


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # financial indicator
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


    def monetary_aggregates_m1(self):
        '''
        Check national currency or non national currency
        '''
        code1 = 'MANMM101'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def monetary_aggregates_m3(self):
        '''
        Check national currency or non national currency
        '''
        code1 = 'MABMM301'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def interbank_rates(self):
        '''
        Check national currency or non national currency
        '''
        code1 = 'IRSTCI01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def short_term_rates(self):
        '''
        Check national currency or non national currency
        '''
        code1 = 'IR3TBB01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def long_term_rates(self):
        '''
        Check national currency or non national currency
        '''
        code1 = 'IRLTLT01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def all_share_prices(self):
        code1 = 'SPASTT01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def share_prices_industrials(self):
        code1 = 'SPINTT01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def usd_exchange_rates_spot(self):
        code1 = 'CCUSSP01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def usd_exchange_rates_average(self):
        code1 = 'CCUSMA02'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def rer_overall(self):
        code1 = 'CCRETT01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+{self.currency_code}.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # trade
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

    def exports_value(self):
        code1 = 'XTEXVA01'
        code2 = f'.NCML+NCMLSA+CXML+CXMLSA+GYSA.{self.freq}' # other currency codes
        return self._main_indicator_helper(code1, code2)

    def imports_value(self):
        code1 = 'XTIMVA01'
        code2 = f'.NCML+NCMLSA+CXML+CXMLSA+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # labour indicators
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

    def unemployment_rate(self):
        code1 = 'LRHUTTTT'
        code2 = f'.STSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # price indices
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


    def cpi_total(self):
        code1 = 'CPALTT01'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def cpi_city_total(self):
        code1 = 'CPALCY01'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def cpi_non_food_non_energy(self):
        code1 = 'CPGRLE01'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def cpi_energy(self):
        code1 = 'CPGREN01'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # national accounts
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


    def gdp_deflator(self):
        code1 = 'NAGIGP01'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def gdp_total(self):
        code1 = 'NAEXKP01'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def gdp_final_consumption(self):
        code1 = 'NAEXKP02'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def gdp_government_consumption(self):
        code1 = 'NAEXKP03'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    def gdp_fixed_capital_formation(self):
        code1 = 'NAEXKP04'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def gdp_exports(self):
        code1 = 'NAEXKP06'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def gdp_imports(self):
        code1 = 'NAEXKP07'
        code2 = f'.IXOB+IXOBSA+GY+GYSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # production and sales
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


    def total_manufacturing_index(self):
        '''

        '''
        code1 = 'PRMNTO01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)

    def total_industry_production_ex_construction(self):
        '''

        '''
        code1 = 'PRINTO01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    def total_construction(self):
        '''

        '''
        code1 = 'PRCNTO01'
        code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    def total_retail_trade(self, measure = 'value'):
        '''

        '''
        if measure != 'value':
            code1 = 'SLRTTO01' # volume instead of value
        else:
            code1 = 'SLRTTO02' # default value measure
        code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    def passenger_car_registration(self):
        '''

        '''
        code1 = 'SLRTCR03'
        code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)


    def construction_permits_issued(self):
        '''

        '''
        code1 = 'ODCNPI03'
        code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.{self.freq}'
        return self._main_indicator_helper(code1, code2)




    ################################################################################
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    # - - - - - - -  - - - - - helper functions  - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
    ################################################################################

    def _get_oecd(self, code, measure = True):
        '''

        '''
        code = f'https://stats.oecd.org/SDMX-JSON/data/{code}/all/OECD?contentType=csv'
        df = pd.read_csv(code)
        if measure == True:
            columns = ['SUBJECT', 'Subject', 'Country', 'MEASURE', 'Measure', 'FREQUENCY', 'TIME', 'Unit Code', 'PowerCode Code', 'Value' ]
        else:
            columns = ['SUBJECT', 'Subject', 'Country', 'FREQUENCY', 'TIME', 'Unit Code', 'PowerCode Code', 'Value' ]
        df = df[columns]
        df.index = pd.to_datetime(df.TIME)
        return df


    def _fa_helper(self, codes, assets_or_liabs):
        '''

        '''

        code2 = f'.{self.currency_code}.{self.freq}'

        if assets_or_liabs == 'assets':
            code1 = codes[0]#'B6FATC01'
        elif assets_or_liabs == 'liabs':
            code1 = codes[1]# 'B6FATD01'
        else:
            code1 = codes[2] #'B6FATT01'

        if self.country_code == 'all':
            df = self._get_oecd(f'MEI_BOP6/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}')
        else:
            df = self._get_oecd(f'MEI_BOP6/{code1}.{self.country_code.upper()}{code2}')
        return df


    def _main_indicator_helper(self, code1, code2):
        if self.country_code == 'all':
            df = self._get_oecd(f'MEI/AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF.{code1}{code2}',
                            measure = False)
        else:
            df = self._get_oecd(f'MEI/{code1}.{self.country_code.upper()}{code2}',
                            measure = False)
        return df


        '''
        main economic indicators
        'https://stats.oecd.org/restsdmx/sdmx.ashx/GetData/MEI/AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU28+G4E+G-7+NAFTA+OECDE+G-20+OECD+SDR+ONM+A5M+NMEC+ARG+BRA+BGR+CHN+CRI+CYP+IND+IDN+MLT+ROU+RUS+SAU+ZAF.LO+LORS+LORSGP+LORSGPRT+LORSGPNO+LORSGPTD+LORSGPOR+LOLI+LOLITO+LOLITOAA+LOLITONO+LOLITOTR+LOCO+LOCOPA+LOCOPANO+LOCOPAOR+LOCOAB+LOCOABNO+LOCOABOR+LOCOBS+LOCOBSNO+LOCOBSOR+LOCOBU+LOCOBUNO+LOCOBUOR+LOCOBD+LOCOBDNO+LOCOBDOR+LOCOBE+LOCOBENO+LOCOBEOR+LOCOBX+LOCOBXNO+LOCOBXOR+LOCOBF+LOCOBFNO+LOCOBFOR+LOCOBO+LOCOBONO+LOCOBOOR+LOCOBI+LOCOBINO+LOCOBIOR+LOCOBP+LOCOBPNO+LOCOBPOR+LOCOBC+LOCOBCNO+LOCOBCOR+LOCOBK+LOCOBKNO+LOCOBKOR+LOCOVR+LOCOVRNO+LOCOVROR+LOCODW+LOCODWNO+LOCODWOR+LOCOPC+LOCOPCNO+LOCOPCOR+LOCOCI+LOCOCINO+LOCOCIOR+LOCOCE+LOCOCENO+LOCOCEOR+LOCOEX+LOCOEXNO+LOCOEXOR+LOCOEM+LOCOEMNO+LOCOEMOR+LOCOTX+LOCOTXNO+LOCOTXOR+LOCOXG+LOCOXGNO+LOCOXGOR+LOCOHS+LOCOHSNO+LOCOHSOR+LOCOTM+LOCOTMNO+LOCOTMOR+LOCOMG+LOCOMGNO+LOCOMGOR+LOCOIS+LOCOISNO+LOCOISOR+LOCOLT+LOCOLTNO+LOCOLTOR+LOCOMA+LOCOMANO+LOCOMAOR+LOCONT+LOCONTNO+LOCONTOR+LOCOOD+LOCOODNO+LOCOODOR+LOCOPP+LOCOPPNO+LOCOPPOR+LOCOPB+LOCOPBNO+LOCOPBOR+LOCOPE+LOCOPENO+LOCOPEOR+LOCOPG+LOCOPGNO+LOCOPGOR+LOCOPQ+LOCOPQNO+LOCOPQOR+LOCOPM+LOCOPMNO+LOCOSL+LOCOSLNO+LOCOSLOR+LOCOSP+LOCOSPNO+LOCOSPOR+LOCOST+LOCOSTNO+LOCOSTOR+LOCOSI+LOCOSINO+LOCOSIOR+LOCOSK+LOCOSKNO+LOCOSKOR+LOCOTT+LOCOTTNO+LOCOTTOR+LOCOTA+LOCOTANO+LOCOTAOR.ST+STSA+IXOB+IXOBSA+GY+GYSA.{self.freq}+M'

        '''
