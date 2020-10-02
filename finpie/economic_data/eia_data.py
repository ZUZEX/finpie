#!/usr/bin/env python3
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
import pandas as pd
from collections import OrderedDict

class EiaData(object):

    def __init__(self, freq = 'm', barrels = 'mbblpd', id = False):
        self.freq = freq
        self.barrels = barrels
        self.id = id

    # general
    def eia_petroleum_series(self, series_id, sheet_name = 'all'):

        if sheet_name.lower() == 'all':
            df = pd.read_excel( f'https://www.eia.gov/dnav/pet/xls/{series_id}.xls', sheet_name = None )
            df = pd.concat( [ pd.read_excel( f'https://www.eia.gov/dnav/pet/xls/{series_id}.xls', sheet_name = sheet, index_col = 0 ) for sheet in list(df.keys())[1:] ], axis = 1, sort = False )
        else:
            df = pd.read_excel( f'https://www.eia.gov/dnav/pet/xls/{series_id}.xls', sheet_name = sheet_name, index_col = 0 )
        if self.id:
            df.columns = df.iloc[0,:]
        else:
            df.columns = df.iloc[1,:]
        df = df[2:]
        df.index = pd.to_datetime( df.index )
        df.index.name = 'date'
        df.columns.name = ''
        return df.astype('float')

    def latest_weekly_balance(self, breakdown = False):

        df = pd.read_csv('http://ir.eia.gov/wpsr/table1.csv', encoding='cp1252', error_bad_lines = False, warn_bad_lines = False)
        df.dropna(inplace = True)
        columns_dict = OrderedDict( {'STUB_1': 'supply',
                        'Difference': 'difference_week_ago',
                        'Difference.1': 'difference_year_ago',
                        f'Percent Change': 'percent_change_week_ago',
                        f'Percent Change.1': 'percent_change_year_ago' } )
        if not breakdown:
            df.columns = [ columns_dict[col] if col in columns_dict.keys() else col for col in df.columns ]
            df.replace(',', '', regex = True, inplace = True)
            df.iloc[:, 1:] = df.iloc[:, 1:].astype('float')
            return df
        else:
            df2 = pd.read_csv('http://ir.eia.gov/wpsr/table1.csv', skiprows = len(df)+1, encoding='cp1252', error_bad_lines = False, warn_bad_lines = False)
            df2.dropna(inplace = True)
            df2.iloc[:,1] = [ ' '.join( [re.sub(r'\(.*\)', '', i.split(' ')[0] ).strip()] + i.split(' ')[1:] ) for i in df2.iloc[:,1].values ]
            columns_dict['STUB_2'] = 'breakdown'
            columns_dict[f'{df2.columns.tolist()[2]}.1'] = '4_week_average_week_ago'
            columns_dict[f'{df2.columns.tolist()[5]}.1'] = '4_week_average_year_ago'
            columns_dict[f'{df2.columns.tolist()[2]}.2'] = 'cumulative_daily_average_week_ago'
            columns_dict[f'{df2.columns.tolist()[5]}.2'] = 'cumulative_daily_average_year_ago'
            df2.columns = [ columns_dict[col] if col in columns_dict.keys() else col for col in df2.columns ]
            df2.replace(',', '', regex = True, inplace = True)
            df2.replace('– –', 'NaN', regex = True, inplace = True)
            df2.iloc[:, 2:] = df2.iloc[:, 2:].astype('float')
            return df2



    def weekly_balance(self, series = 'all', sma = False):
        temp_dict = OrderedDict( { 'crude oil production': 'Data 1',
                                    'refiner inputs and utilisation': 'Data 2',
                                    'refiner and blender net inputs': 'Data 3',
                                    'refiner and blender net production': 'Data 4',
                                    'ethanol plant production': 'Data 5',
                                    'stocks': 'Data 6',
                                    'days of supply': 'Data 7',
                                    'imports': 'Data 8',
                                    'exports': 'Data 9',
                                    'net imports incl spr': 'Data 10',
                                    'product supplied': 'Data 11' } )
        if sma:
            f = '4'
        else:
            f = 'W'
        if series == 'all':
            dfs = []
            for key in temp_dict.keys():
                temp = self.eia_petroleum_series(f'PET_SUM_SNDW_DCUS_NUS_{f}', temp_dict[key])
                temp.columns = pd.MultiIndex.from_product([[key], temp.columns])
                dfs.append(temp)
            return pd.concat( dfs, sort = False, axis = 1 )
        elif type(series) == type([]):
            dfs = []
            for key in series:
                temp = self.eia_petroleum_series(f'PET_SUM_SNDW_DCUS_NUS_{f}', temp_dict[key])
                temp.columns = pd.MultiIndex.from_product([[key], temp.columns])
                dfs.append(temp)
                return pd.concat( dfs, sort = False, axis = 1 )
        elif series:
            return self.eia_petroleum_series(f'PET_SUM_SNDW_DCUS_NUS_{f}', temp_dict[series])

    # crude supply
    def crude_supply_and_disposition( self, series = 'all' ):
        if series == 'all':
            return self.eia_petroleum_series('pet_sum_crdsnd_k_m')
        elif series == 'supply':
            return self.eia_petroleum_series('pet_sum_crdsnd_k_m', 'Data 1' )
        elif series == 'disposition':
            return self.eia_petroleum_series('pet_sum_crdsnd_k_m', 'Data 2' )
        elif series == 'ending stocks':
            return self.eia_petroleum_series('pet_sum_crdsnd_k_m', 'Data 3' )
        elif series == 'spr stocks':
            return self.eia_petroleum_series('pet_sum_crdsnd_k_m', 'Data 4' )
        elif series == 'spr imports':
            return self.eia_petroleum_series('pet_sum_crdsnd_k_m', 'Data 5' )

    def crude_production( self ):
        freq = 'm'
        barrels = 'mbblpd' # or mbbl
        return self.eia_petroleum_series(f'pet_crd_crpdn_adc_{barrels}_{freq}')

    def rig_count( self ):
        return self.eia_petroleum_series(f'pet_crd_drill_s1_{self.freq}')

    def crude_reserves( self ):
        return self.eia_petroleum_series('pet_crd_pres_dcu_NUS_a')

    # import and exports
    def weekly_xm( self, padds = False, sma = False):
        # by padds
        # 4 week average
        if padds:
            if sma:
                return self.eia_petroleum_series(f'pet_move_wkly_a_ep00_IM0_{self.barrels}_4')
            else:
                return self.eia_petroleum_series(f'pet_move_wkly_a_EP00_IM0_{self.barrels}_w')
        else:
            if sma:
                return self.eia_petroleum_series(f'pet_move_wkly_dc_NUS-Z00_{self.barrels}_4')
            else:
                return self.eia_petroleum_series(f'pet_move_wkly_dc_NUS-Z00_{self.barrels}_w')


    def monthly_xm( self, net = False, xm = 'both', by = False ):
        # imports and exports by padds..
        if net:
            return self.eia_petroleum_series(f'pet_move_neti_a_EP00_IMN_{self.barrels}_{self.freq}')
        else:
            m = self.eia_petroleum_series(f'pet_move_imp_dc_NUS-Z00_{self.barrels}_{self.freq}')
            m.columns = pd.MultiIndex.from_product([['imports'], m.columns])
            x = self.eia_petroleum_series(f'pet_move_exp_dc_NUS-Z00_{self.barrels}_{self.freq}')
            x.columns = pd.MultiIndex.from_product([['exports'], x.columns])
            if xm == 'both' or xm == 'xm':
                return pd.concat([m,x], axis = 1, sort = False)
            elif xm.lower() == 'm' or xm.lower() == 'imports':
                if by:
                    return self.eia_petroleum_series(f'pet_move_impcus_a2_nus_ep00_im0_{self.barrels}_{self.freq}')
                else:
                    return m
            elif xm.lower() == 'x' or xm.lower() == 'exports':
                if by:
                    return self.eia_petroleum_series(f'pet_move_expc_a_EP00_EEX_{self.barrels}_{self.freq}')
                else:
                    return x

    def weekly_imports_by_country( self, sma = False):
        if sma:
            f = '4'
        else:
            f = 'w'
        return self.eia_petroleum_series(f'pet_move_wimpc_s1_{f}')


    def crude_imports_quality(self):
        return self.eia_petroleum_series(f'pet_move_ipct_k_{self.freq}')


    # Refinery info
    def weekly_refinery_inputs( self, series = 'all', sma = False ):
        if sma:
            freq = '4'
        else:
            freq = 'w'
        if series == 'all':
            return self.eia_petroleum_series(f'pet_pnp_wiup_dcu_nus_{freq}')
        elif series == 'inputs':
            return self.eia_petroleum_series(f'pet_pnp_wiup_dcu_nus_{freq}', 'Data 1')
        elif series == 'net':
            return self.eia_petroleum_series(f'pet_pnp_wiup_dcu_nus_{freq}', 'Data 2')

    def refinery_utilisation( self ):
        return self.eia_petroleum_series('pet_pnp_unc_dcu_nus_m')

    def refinery_yield( self ):
        return self.eia_petroleum_series('pet_pnp_pct_dc_nus_pct_m')

    def refineries( self ):
        return self.eia_petroleum_series('pet_pnp_cap1_dcu_nus_a')

    def crude_acquisition_costs( self ):
        return self.eia_petroleum_series(f'pet_pri_rac2_dcu_nus_{self.freq}')

    def crude_inputs_quality(self):
        return self.eia_petroleum_series(f'pet_pnp_crq_dcu_nus_{self.freq}')

    # stocks
    def weekly_stocks(self, padds = False):

        if padds:
            stocks = OrderedDict( {  'commercial_crude': 'pet_stoc_wstk_a_EPC0_SAX_mbbl_w',
                        'total_gasoline': 'pet_stoc_wstk_a_epm0_sae_mbbl_w',
                        'ethanol': 'pet_stoc_wstk_a_EPOOXE_sae_mbbl_w',
                        'kerosene': 'pet_stoc_wstk_a_EPJK_sae_mbbl_w',
                        'distillates': 'pet_stoc_wstk_a_epd0_sae_mbbl_w',
                        'fuel_oil': 'pet_stoc_wstk_a_eppr_sae_mbbl_w',
                         'propane_propylene': 'pet_stoc_wstk_a_EPLLPZ_sae_mbbl_w' } )

            dfs = []
            for key in stocks.keys():
                temp = self.eia_petroleum_series(stocks[key])
                temp.columns = pd.MultiIndex.from_product([[key], temp.columns])
                dfs.append(temp)
            return pd.concat( dfs, axis = 1, sort = False )
        else:
            return self.eia_petroleum_series('pet_stoc_wstk_dcu_nus_w')

    def monthly_product_stocks(self, padds = False):

        if padds:
            stocks = OrderedDict( {
                        'total_gasoline': 'pet_stoc_ts_a_EPM0_SAE_Mbbl_m',
                        'ethanol': 'pet_stoc_wstk_a_EPOOXE_sae_mbbl_w',
                        'kerosene': 'pet_stoc_wstk_a_EPJK_sae_mbbl_w',
                        'distillates': 'pet_stoc_ts_a_epd0_sae_mbbl_m',
                        'fuel_oil': 'pet_stoc_ts_a_eppr_sae_mbbl_m',
                        'propane_propylene': 'pet_stoc_ts_a_EPLLPZ_sae_mbbl_m' } )
            dfs = []
            for key in stocks.keys():
                temp = self.eia_petroleum_series(stocks[key])
                temp.columns = pd.MultiIndex.from_product([[key], temp.columns])
                dfs.append(temp)
            return pd.concat( dfs, axis = 1, sort = False )
        else:
            return self.eia_petroleum_series('pet_stoc_ts_dcu_nus_m')


    def monthly_refinery_stocks(self):
        '''if padds:
            stocks = {  'commercial_crude': 'pet_stoc_ref_a_EPC0_SKR_mbbl_m',
                        'total_gasoline': 'pet_stoc_wstk_a_epm0_sae_mbbl_w',
                        'ethanol': 'pet_stoc_wstk_a_EPOOXE_sae_mbbl_w',
                        'kerosene': 'pet_stoc_wstk_a_EPJK_sae_mbbl_w',
                        'distillates': 'pet_stoc_wstk_a_epd0_sae_mbbl_w',
                        'fuel_oil': 'pet_stoc_wstk_a_eppr_sae_mbbl_w',
                         'propane_propylene': 'pet_stoc_wstk_a_EPLLPZ_sae_mbbl_w' }
        else:'''
        return self.eia_petroleum_series('pet_stoc_ref_dc_nus_mbbl_m')


    def monthly_tank_and_pipeline_stocks(self):
        return self.eia_petroleum_series('pet_stoc_cu_s1_m')

    # consumption and sales

    def weekly_product_supplied(self, sma = False):
        if sma:
            return self.eia_petroleum_series('pet_cons_wpsup_k_4')
        else:
            return self.eia_petroleum_series('pet_cons_wpsup_k_w')

    def monthly_product_supplied(self):
        #if padds:
        return self.eia_petroleum_series(f'pet_cons_psup_dc_nus_{self.barrels}_{self.freq}')

    def product_prices_sales_and_stock( self, series = 'all' ):
        if series.lower() == 'all':
            return self.eia_petroleum_series('pet_sum_mkt_dcu_nus_m')
        elif series.lower() == 'retail':
            return self.eia_petroleum_series('pet_sum_mkt_dcu_nus_m', 'Data 1')
        elif series.lower() == 'volume':
            return self.eia_petroleum_series('pet_sum_mkt_dcu_nus_m', 'Data 2')
        elif series.lower() == 'stocks':
            return self.eia_petroleum_series('pet_sum_mkt_dcu_nus_m', 'Data 3')
