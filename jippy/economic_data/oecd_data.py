
import pandas as pd

# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - oced current account  - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


def oecd_current_account(country_code = 'all', percent_of_gdp = False):
    if percent_of_gdp:
        code1 = 'B6BLTT02'
        code2 = '.STSA.Q'
    else:
        code1 = 'B6BLTT01'
        code2 = '.NCCU+CXCU+NCCUSA+CXCUSA.Q'
    if country_code == 'all':
        df = get_oecd(f'MEI_BOP6/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}')
    else:
        df = get_oecd(f'MEI_BOP6/{code1}.{country_code.upper()}{code2}')
    return df

def oecd_goods_balance(country_code = 'all', xm = 'balance'):
    if xm.lower() == 'exports':
        code1 = 'B6CRTD01'
    elif xm.lower() == 'imports':
        code1 = 'B6DBTD01'
    else:
        code1 = 'B6BLTD01'
    code2 = '.NCCU+CXCU+NCCUSA+CXCUSA.Q'

    if country_code == 'all':
        df = get_oecd(f'MEI_BOP6/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}')
    else:
        df = get_oecd(f'MEI_BOP6/{code1}.{country_code.upper()}{code2}')
    return df

def oecd_services_balance(country_code = 'all', xm = 'balance'):
    if xm.lower() == 'exports':
        code1 = 'B6CRSE01'
    elif xm.lower() == 'imports':
        code1 = 'B6DBSE01'
    else:
        code1 = 'B6BLSE01'
    code2 = '.NCCU+CXCU+NCCUSA+CXCUSA.Q'

    if country_code == 'all':
        df = get_oecd(f'MEI_BOP6/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}')
    else:
        df = get_oecd(f'MEI_BOP6/{code1}.{country_code.upper()}{code2}')
    return df





# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - oced financial account  - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -



def oecd_financial_account(country_code = 'all', currency = 'dollar', assets_or_liabs = None):
    '''

    '''
    codes = [ 'B6FATC01', 'B6FATD01', 'B6FATT01' ]
    return fa_helper(codes, country_code, currency, assets_or_liabs)

def oecd_direct_investment(country_code = 'all', currency = 'dollar', assets_or_liabs = None):
    '''

    '''
    codes = [ 'B6FADI02', 'B6FADI03', 'B6FADI01' ]
    return fa_helper(codes, country_code, currency, assets_or_liabs)

def oecd_portfolio_investment(country_code = 'all', currency = 'dollar', assets_or_liabs = None):
    '''

    '''
    codes = [ 'B6FAPI02', 'B6FAPI03', 'B6FAPI10' ]
    return fa_helper(codes, country_code, currency, assets_or_liabs)


def oecd_other_investment(country_code = 'all', currency = 'dollar', assets_or_liabs = None):
    '''

    '''
    codes = [ 'B6FAOI02', 'B6FAOI03', 'B6FAOI01' ]
    return fa_helper(codes, country_code, currency, assets_or_liabs)

def oecd_financial_derivatives(country_code = 'all', currency = 'dollar' ):
    '''

    '''
    assets_or_liabs = None
    codes = ['B6FAFD01', 'B6FAFD01', 'B6FAFD01']
    return fa_helper(codes, country_code, currency, assets_or_liabs)

def oecd_reserve_assets(country_code = 'all', currency = 'dollar' ):
    '''

    '''
    assets_or_liabs = None
    codes = ['B6FARA01', 'B6FARA01', 'B6FARA01']
    return fa_helper(codes, country_code, currency, assets_or_liabs)


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - -  oecd composite leading indicators - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


def oecd_cli(country_code = 'all', subject = 'amplitude'):
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
    code2 = '.M'

    if country_code == 'all':
        df = get_oecd(f'MEI_CLI/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                        measure = False)
    else:
        df = get_oecd(f'MEI_CLI/{code1}.{country_code.upper()}{code2}',
                        measure = False)
    return df



def oecd_cci(country_code = 'all'):
    code1 = 'CSCICP03'
    code2 = '.M'

    if country_code == 'all':
        df = get_oecd(f'MEI_CLI/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                        measure = False)
    else:
        df = get_oecd(f'MEI_CLI/{code1}.{country_code.upper()}{code2}',
                        measure = False)
    return df



def oecd_bci(country_code = 'all'):
    code1 = 'BSCICP03'
    code2 = '.M'

    if country_code == 'all':
        df = get_oecd(f'MEI_CLI/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                        measure = False)
    else:
        df = get_oecd(f'MEI_CLI/{code1}.{country_code.upper()}{code2}',
                        measure = False)
    return df


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - -oecd business tendency survey - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -



def oecd_survey_economic_situation( country_code = 'all', freq = 'M' ):

    code1 = code1 = 'CSESFT'
    code2 = f'.BLSA.{freq.upper()}'

    if country_code == 'all':
        df = get_oecd(f'MEI_BTS_COS/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                        measure = False)
    else:
        df = get_oecd(f'MEI_BTS_COS/{code1}.{country_code.upper()}{code2}',
                        measure = False)
    return df


def oecd_survey_consumer_confidence( country_code = 'all', freq = 'M' ):

    code1 = code1 = 'CSCICP02'
    code2 = f'.BLSA.{freq.upper()}'

    if country_code == 'all':
        df = get_oecd(f'MEI_BTS_COS/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                        measure = False)
    else:
        df = get_oecd(f'MEI_BTS_COS/{code1}.{country_code.upper()}{code2}',
                        measure = False)
    return df


def oecd_survey_consumer_price_inflation(country_code = 'all', freq = 'M' ):
    code1 = code1 = 'CSINFT'
    code2 = f'.BLSA.{freq.upper()}'

    if country_code == 'all':
        df = get_oecd(f'MEI_BTS_COS/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}',
                        measure = False)
    else:
        df = get_oecd(f'MEI_BTS_COS/{code1}.{country_code.upper()}{code2}',
                        measure = False)
    return df


# TO DO:
# BUSINESS TENDENCY SURVEYS
# # https://stats.oecd.org/restsdmx/sdmx.ashx/GetData/MEI_BTS_COS/BS+BSPR+BSPRTE+BSPRFT+BSFG+BSFGLV+BSOB+BSOBLV+BSOI+BSOITE+BSXR+BSXRLV+BSSP+BSSPFT+BSEM+BSEMFT+BSCU+BSCURT+BSBU+BSBUCT+BSCI+BC+BCBU+BCBUTE+BCCI+BCOB+BCOBLV+BCEM+BCEMFT+BCSP+BCSPFT+BR+BRBU+BRBUTE+BRBUFT+BRCI+BRVS+BRVSLV+BREM+BREMFT+BROD+BRODFT+BV+BVBU+BVBUTE+BVCI+BVDE+BVDETE+BVDEFT+BVEM+BVEMTE+BVEMFT+BN+BNBU+BNBUCT+BNBUFT+BNRM+BNRMTE+BNEM+BNEMTE+BNEMFT+BNOD+BNODTE.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ISR+ITA+JPN+KOR+LVA+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+NMEC+BRA+CHN+IND+IDN+RUS+ZAF.BLSA.Q+M/all?startTime=2019-Q1&endTime=2020-Q3


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - oecd main economic indicators - - - - - - - - - - - - -
#          https://stats.oecd.org/Index.aspx?DataSetCode=MEI_CLI#
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

def main_indicator_helper(code1, code2, country_code):
    if country_code == 'all':
        df = get_oecd(f'MEI/AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF.{code1}{code2}',
                        measure = False)
    else:
        df = get_oecd(f'MEI/{code1}.{country_code.upper()}{code2}',
                        measure = False)
    return df


'''
main economic indicators
'https://stats.oecd.org/restsdmx/sdmx.ashx/GetData/MEI/AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU28+G4E+G-7+NAFTA+OECDE+G-20+OECD+SDR+ONM+A5M+NMEC+ARG+BRA+BGR+CHN+CRI+CYP+IND+IDN+MLT+ROU+RUS+SAU+ZAF.LO+LORS+LORSGP+LORSGPRT+LORSGPNO+LORSGPTD+LORSGPOR+LOLI+LOLITO+LOLITOAA+LOLITONO+LOLITOTR+LOCO+LOCOPA+LOCOPANO+LOCOPAOR+LOCOAB+LOCOABNO+LOCOABOR+LOCOBS+LOCOBSNO+LOCOBSOR+LOCOBU+LOCOBUNO+LOCOBUOR+LOCOBD+LOCOBDNO+LOCOBDOR+LOCOBE+LOCOBENO+LOCOBEOR+LOCOBX+LOCOBXNO+LOCOBXOR+LOCOBF+LOCOBFNO+LOCOBFOR+LOCOBO+LOCOBONO+LOCOBOOR+LOCOBI+LOCOBINO+LOCOBIOR+LOCOBP+LOCOBPNO+LOCOBPOR+LOCOBC+LOCOBCNO+LOCOBCOR+LOCOBK+LOCOBKNO+LOCOBKOR+LOCOVR+LOCOVRNO+LOCOVROR+LOCODW+LOCODWNO+LOCODWOR+LOCOPC+LOCOPCNO+LOCOPCOR+LOCOCI+LOCOCINO+LOCOCIOR+LOCOCE+LOCOCENO+LOCOCEOR+LOCOEX+LOCOEXNO+LOCOEXOR+LOCOEM+LOCOEMNO+LOCOEMOR+LOCOTX+LOCOTXNO+LOCOTXOR+LOCOXG+LOCOXGNO+LOCOXGOR+LOCOHS+LOCOHSNO+LOCOHSOR+LOCOTM+LOCOTMNO+LOCOTMOR+LOCOMG+LOCOMGNO+LOCOMGOR+LOCOIS+LOCOISNO+LOCOISOR+LOCOLT+LOCOLTNO+LOCOLTOR+LOCOMA+LOCOMANO+LOCOMAOR+LOCONT+LOCONTNO+LOCONTOR+LOCOOD+LOCOODNO+LOCOODOR+LOCOPP+LOCOPPNO+LOCOPPOR+LOCOPB+LOCOPBNO+LOCOPBOR+LOCOPE+LOCOPENO+LOCOPEOR+LOCOPG+LOCOPGNO+LOCOPGOR+LOCOPQ+LOCOPQNO+LOCOPQOR+LOCOPM+LOCOPMNO+LOCOSL+LOCOSLNO+LOCOSLOR+LOCOSP+LOCOSPNO+LOCOSPOR+LOCOST+LOCOSTNO+LOCOSTOR+LOCOSI+LOCOSINO+LOCOSIOR+LOCOSK+LOCOSKNO+LOCOSKOR+LOCOTT+LOCOTTNO+LOCOTTOR+LOCOTA+LOCOTANO+LOCOTAOR.ST+STSA+IXOB+IXOBSA+GY+GYSA.Q+M'

'''

# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# business tendency and consumer opinion
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

def business_tendency_survey(sector, country_code = 'all', freq = 'M'):
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
    code2 = f'.STSA+IXNSA.{freq}'

    return main_indicator_helper(code1, code2, country_code)


def consumer_opinion_survey( country_code = 'all', measure = 'national', freq = 'M'):
    '''

    '''
    if measure == 'oecd':
        code1 = 'CSCICP03'
    else:
        code1 = 'CSCICP02'
    code2 = f'.STSA+IXNSA.{freq}'

    return main_indicator_helper(code1, code2, country_code)


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# financial indicator
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


def monetary_aggregates_m1(country_code = 'all', freq = 'M'):
    '''
    Check national currency or non national currency
    '''
    code1 = 'MANMM101'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def monetary_aggregates_m3(country_code = 'all', freq = 'M'):
    '''
    Check national currency or non national currency
    '''
    code1 = 'MABMM301'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def interbank_rates(country_code = 'all', freq = 'M'):
    '''
    Check national currency or non national currency
    '''
    code1 = 'IRSTCI01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def short_term_rates(country_code = 'all', freq = 'M'):
    '''
    Check national currency or non national currency
    '''
    code1 = 'IR3TBB01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def long_term_rates(country_code = 'all', freq = 'M'):
    '''
    Check national currency or non national currency
    '''
    code1 = 'IRLTLT01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def all_share_prices(country_code = 'all', freq = 'M'):
    code1 = 'SPASTT01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def share_prices_industrials(country_code = 'all', freq = 'M'):
    code1 = 'SPINTT01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def usd_exchange_rates_spot(country_code = 'all', freq = 'M'):
    code1 = ''
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def usd_exchange_rates_average(country_code = 'all', freq = 'M'):
    code1 = 'CCUSMA02'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def rer_overall(country_code = 'all', freq = 'M'):
    code1 = 'CCRETT01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+NCCU+NCCUSA+CXCU+CXCUSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# trade
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

def exports_value(country_code = 'all', freq = 'M'):
    code1 = 'XTEXVA01'
    code2 = f'.NCML+NCMLSA+CXML+CXMLSA+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def imports_value(country_code = 'all', freq = 'M'):
    code1 = 'XTIMVA01'
    code2 = f'.NCML+NCMLSA+CXML+CXMLSA+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# labour indicators
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -

def unemployment_rate(country_code = 'all', freq = 'M'):
    code1 = 'LRHUTTTT'
    code2 = f'.STSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# price indices
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


def cpi_total(country_code = 'all', freq = 'M'):
    code1 = 'CPALTT01'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    main_indicator_helper(code1, code2, country_code)

def cpi_city_total(country_code = 'all', freq = 'M'):
    code1 = 'CPALCY01'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def cpi_non_food_non_energy(country_code = 'all', freq = 'M'):
    code1 = 'CPGRLE01'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def cpi_energy(country_code = 'all', freq = 'M'):
    code1 = 'CPGREN01'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# national accounts
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


df = gdp_deflator( 'all', freq = 'Q')

df.head(5).to_markdown()

df[df.Country == 'Australia'].tail()


def gdp_deflator(country_code = 'all', freq = 'Q'):
    code1 = 'NAGIGP01'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def gdp_total(country_code = 'all', freq = 'Q'):
    code1 = 'NAEXKP01'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def gdp_final_consumption(country_code = 'all', freq = 'Q'):
    code1 = 'NAEXKP02'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def gdp_government_consumption(country_code = 'all', freq = 'Q'):
    code1 = 'NAEXKP03'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)


def gdp_fixed_capital_formation(country_code = 'all', freq = 'Q'):
    code1 = 'NAEXKP04'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def gdp_exports(country_code = 'all', freq = 'Q'):
    code1 = 'NAEXKP06'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)

def gdp_imports(country_code = 'all', freq = 'Q'):
    code1 = 'NAEXKP07'
    code2 = f'.IXOB+IXOBSA+GY+GYSA.{freq}'
    return main_indicator_helper(code1, code2, country_code)


# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# production and sales
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -


def total_manufacturing_index(country_code, freq = 'M'):
    '''

    '''
    code1 = 'PRMNTO01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.Q'
    main_indicator_helper(code1, code2, country_code)

def total_industry_production_ex_construction(country_code, freq = 'M'):
    '''

    '''
    code1 = 'PRINTO01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.Q'
    main_indicator_helper(code1, code2, country_code)


def total_construction(country_code, freq = 'M'):
    '''

    '''
    code1 = 'PRCNTO01'
    code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.Q'
    return main_indicator_helper(code1, code2, country_code)


def total_retail_trade(country_code, freq = 'M', measure = 'value'):
    '''

    '''
    if measure != 'value':
        code1 = 'SLRTTO01' # volume instead of value
    else:
        code1 = 'SLRTTO02' # default value measure
    code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.Q'
    return main_indicator_helper(code1, code2, country_code)


def passenger_car_registration(country_code, freq = 'M'):
    '''

    '''
    code1 = 'SLRTCR03'
    code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.Q'
    return main_indicator_helper(code1, code2, country_code)


def construction_permits_issued(country_code, freq = 'M'):
    '''

    '''
    code1 = 'ODCNPI03'
    code2 = f'.ST+STSA+IXOB+IXOBSA+ML+MLSA+QL+QLSA.Q'
    return main_indicator_helper(code1, code2, country_code)






################################################################################
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
# - - - - - - -  - - - - - helper functions  - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - -
################################################################################

def get_oecd(code, measure = True):
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


def fa_helper(codes, country_code, currency, assets_or_liabs):
    '''

    '''
    if currency == 'national':
        currency = 'NCCU'
        code2 = f'.{currency}.Q'
    else:
        currency = 'CXCU'
        code2 = f'.{currency}.Q'

    if assets_or_liabs == 'assets':
        code1 = codes[0]#'B6FATC01'
    elif assets_or_liabs == 'liabs':
        code1 = codes[1]# 'B6FATD01'
    else:
        code1 = codes[2] #'B6FATT01'

    if country_code == 'all':
        df = get_oecd(f'MEI_BOP6/{code1}.AUS+AUT+BEL+CAN+CHL+COL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+EU27_2020+G-7+OECD+NMEC+ARG+BRA+CHN+CRI+IND+IDN+RUS+SAU+ZAF{code2}')
    else:
        df = get_oecd(f'MEI_BOP6/{code1}.{country_code.upper()}{code2}')
    return df
