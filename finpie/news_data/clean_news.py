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



import numpy as np
import pandas as pd
import datetime as dt
from finpie.base import DataBase

class CleanNews(DataBase):

    def __init__(self):
        DataBase.__init__(self)
        self.months = { 'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', \
                       'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12' }
        self.weekdays = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ]
        self.dayz = [ 'Today', 'Yesterday' ]
        self.filterz = [ ' ' ]

    def _format_date( self, date ):
        '''

        '''
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
        '''

        '''
        data['temp_date'] = np.nan
        hour = [ (idx, hour.split(' ')[0]) for idx, hour in enumerate(data['date']) if 'hour' in hour.lower() or ('h' in hour.lower() and ('march' not in hour.lower() and 'thu' not in hour.lower() ) ) ]
        for i, h in hour:
            data.temp_date.iloc[i] = pd.to_datetime( (data['date_retrieved'].iloc[i] - dt.timedelta( hours = int(h.replace('h', '')) )).strftime(format = '%d-%m-%Y' ), format = '%d-%m-%Y' )

        mins = [ (idx, m.split(' ')[0].replace('m', '')) for idx, m in enumerate(data['date']) if 'm' in m and len(m.split(' ')) <= 2 or 'min' in m ]
        for i, m in mins:
            data.temp_date.iloc[i] = pd.to_datetime( (data['date_retrieved'].iloc[i] - dt.timedelta( minutes = int(m) )).strftime(format = '%d-%m-%Y' ), format = '%d-%m-%Y' )

        week = [ (idx, w.split(' ')[1:]) for idx, w in enumerate(data['date']) if any(wd in w.split(' ')[0] for wd in self.weekdays) ]
        for i, w in week:
            if len(w) == 2:
                data.loc[i, 'temp_date'] = pd.to_datetime( w[1].replace(',', '')  + '-' + self.months[w[0][:3].lower()] + '-' + str(dt.datetime.today().year), format = '%d-%m-%Y' )
            else:
                data.loc[i, 'temp_date'] = pd.to_datetime( w[1].replace(',', '')  + '-' + self.months[w[0][:3].lower()] + '-' + str(w[2]), format = '%d-%m-%Y' )

        day = [ (idx, w.split(' ')[0].replace(',', '')) for idx, w in enumerate(data['date']) if any(wd in w.split(' ')[0].replace(',', '') for wd in self.dayz) ]
        for i, w in day:
            if w == 'Today':
                data.temp_date.iloc[i] = pd.to_datetime( dt.datetime.today().date().strftime(format = '%d-%m-%Y' ), format = '%d-%m-%Y' )

            elif w == 'Yesterday':
                data.temp_date.iloc[i] = pd.to_datetime( (dt.datetime.today().date() - dt.timedelta(days = 1)).strftime(format = '%d-%m-%Y' ),  format = '%d-%m-%Y' )

        hes = [ (idx, hour.split(' ')[0]) for idx, hour in enumerate(data['date']) if 'h ago' in hour.lower() ]
        for i, h in hes:
            data.temp_date.iloc[i] = data['date_retrieved'].iloc[i] - dt.timedelta( hours = int(h.replace('h', '')) )


        for source in np.unique(data['source']):
            if source == 'sa':
                data.temp_date = pd.to_datetime(data.temp_date,  format = '%d-%m-%Y')
            elif source == 'nyt':
                temp = []
                for i, j in enumerate(data.date):
                    if type(data.temp_date.iloc[i]) != type(pd.to_datetime('2000-01-01')):
                        if ',' in j:
                            y = j.split(' ')[-1]
                        else:
                            y = str( dt.datetime.today().year )
                        m = self.months[j.split(' ')[0][:3].replace('.', '').replace(',', '').lower()]
                        if len(j.split(' ')[1].replace(',', '')) < 2:
                            d = '0' + j.split(' ')[1].replace(',', '')
                        else:
                            d = j.split(' ')[1].replace(',', '')
                        temp.append(f'{y}-{m}-{d}')
                    else:
                        temp.append(data.temp_date.iloc[i].strftime('%Y-%m-%d'))

                data.temp_date = pd.to_datetime(temp, format = '%Y-%m-%d')

            elif source in ['ft', 'bloomberg']:
                data['temp_date'][ data['source'] == source ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '-' +  self.months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '-' + d.split(' ')[-1] \
                                                                                             for d in data[ data['source'] == source ]['date'] ], format = '%d-%m-%Y' ))
            elif source in ['barrons', 'wsj']:
                data['temp_date'][ data['source'] == source ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '-' +  self.months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '-' + d.split(' ')[2] \
                                                                        if type(data['temp_date'].iloc[i]) != type(pd.to_datetime('2000-01-01')) else data['temp_date'].iloc[i].strftime( format = '%d-%m-%Y' )
                                                                            for i, d in enumerate( data[ data['source'] == source ]['date'] ) ], format = '%d-%m-%Y' ))
                #data['temp_date'][ data['source'] == source ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '-' +  self.months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '-' + d.split(' ')[2] \
                #                                                                                     for d in data[ data['source'] == source ]['date'] ], format = '%d-%m-%Y' ))
            elif source == 'reuters':
                data['temp_date'][ data['source'] == source ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '-' +  self.months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '-' + d.split(' ')[2] \
                                                                                                     for d in data[ data['source'] == source ]['date'] ], format = '%d-%m-%Y' ))
            elif source == 'cnbc':
                data['temp_date'][ data['source'] == source ] = list(pd.to_datetime( [ d.split(' ')[0].split('/')[1] + '-' + d.split(' ')[0].split('/')[0] + '-' + d.split(' ')[0].split('/')[2] \
                                                                                                     for d in data[ data['source'] == source ]['date'] ], format = '%d-%m-%Y' ))
        data.index = data.temp_date
        data.drop('temp_date', inplace = True, axis = 1)
        data.index.name = 'date'
        data.drop('date', axis = 1, inplace = True)
        return data


    def _clean_duplicates(self, data):
        '''

        '''
        columns = [ col for col in data.columns if col != 'date_retrieved' ]
        data.drop_duplicates(columns, inplace = True)
        data.reset_index(drop = True, inplace = True)
        return data

    def filter_data(self, data):
        '''

        '''
        filtered = []
        for i, n in enumerate(data.headline):
            for f in self.filterz:
                if f in n.lower():
                    filtered.append( data.id.iloc[i] )
                elif f in data.description.iloc[i].lower():
                    filtered.append( data.id.iloc[i] )
                else:
                    continue

        data = data[ data.id.isin(filtered) ]
        #data.reset_index(drop = True, inplace = True)
        return data
