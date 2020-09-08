


import os

os.chdir('/Users/PeterlaCour/Documents/Research.nosync/financial_data_project/jippy/jippy/news_data/')
from NEWS_SCRAPE_CLASS import *

ns = NewsScrape('XOM', 'exxon mobil')
ns.head = True

data = ns.wsj_news(verbose = True)


data.head()


ns.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
data = ns._filter_data(data)


data.head().to_markdown()






_clean_dates(df)


news = 'WSJ'

def _clean_dates(data):

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
            data['Datetime'][ data.Source == news ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[-1] \
                                                                                         for d in data[ data.Source == news ].Date ], format = '%d/%m/%Y' ))
        elif source in ['barrons', 'wsj']:
            data['Datetime'][ data.Source == news ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[2] \
                                                                                                 for d in data[ data.Source == news ].Date ], format = '%d/%m/%Y' ))
        elif source == 'reuters':
            data['Datetime'][ data.Source == news ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[2] \
                                                                                                 for d in data[ data.Source == news ].Date ], format = '%d/%m/%Y' ))
        elif source == 'cnbc'
            data['Datetime'][ data.Source == news ] = list(pd.to_datetime( [ d.split(' ')[0].split('/')[1] + '/' + d.split(' ')[0].split('/')[0] + '/' + d.split(' ')[0].split('/')[2] \
                                                                                                 for d in data[ data.Source == news ].Date ], format = '%d/%m/%Y' ))





        try:
            data['Datetime'][ data.Newspaper == news ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[-1] \
                                                                                         for d in data[ data.Newspaper == news ].Date ], format = '%d/%m/%Y' ))
        except:
            try:
                data['Datetime'][ data.Newspaper == news ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[2] \
                                                                    if type(data[ data.Newspaper == news ].Datetime.iloc[idx]) == type(np.nan) else dt.datetime.strftime(data[ data.Newspaper == news ].Datetime.iloc[idx], format = '%d/%m/%Y') \
                                                                        for idx, d in enumerate(data[ data.Newspaper == news ].Date) ], format = '%d/%m/%Y' ))
            except:
                try:
                    data['Datetime'][ data.Newspaper == news ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0][:3].lower().replace('.', '') ] + '/' + d.split(' ')[2] \
                                                                                                         for d in data[ data.Newspaper == news ].Date ], format = '%d/%m/%Y' ))
                except:
                    try:
                        data['Datetime'][ data.Newspaper == news ] = list(pd.to_datetime( [ d.split(' ')[0].split('/')[1] + '/' + d.split(' ')[0].split('/')[0] + '/' + d.split(' ')[0].split('/')[2] \
                                                                                                             for d in data[ data.Newspaper == news ].Date ], format = '%d/%m/%Y' ))
                    except:
                        try:
                            data['Datetime'][ data.Newspaper == news ] = list(pd.to_datetime( [ d.split(' ')[1][:-1] + '/' +  months[ d.split(' ')[0].lower().replace('.', '') ] + '/' + d.split(' ')[-1] \
                                                                                                                for d in data[ data.Newspaper == news ].Date ], format = '%d/%m/%Y' ))
                        except:
                            print(news)
                            continue
    data.Datetime = data.Datetime.dt.strftime('%d/%m/%Y')
    return data
