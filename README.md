
[![Build Status](https://travis-ci.org/peterlacour/finpie.svg?branch=master)](https://travis-ci.org/peterlacour/finpie) [![PyPi](https://img.shields.io/pypi/v/finpie)](https://pypi.org/project/finpie/) [![Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)]()


# finpie - a simple library to download some financial data

<p><b>For recreational and educational purposes. Creating easier access to some financial and news data.</b></p>

<p>This library is an ongoing project designed to facilitate access to financial and economic data. It tries to cover potentially useful or interesting data points but unfortunately some functions will only return single point data which however could be aggregated over time to construct a limited time series. On the other hand, some functions that retrieve large amounts of data or depending on the data source will take some time to run. See the <a href="#A3">function index </a> for more information on issues of data availability and relative run time.</p>

<p>The company fundamentals module includes functions to retrive data from <code>Yahoo Finance</code>, <code>MarketWatch</code>, <code>The Motley Fool</code>, <code>Finviz</code> and <code>Macrotrends</code>. The price data module retrieves data from <code>Yahoo Finance</code> and <code>CBOE</code>. The news module enables historical news headline collection from the <code>FT</code>, <code>NYT</code>, <code>WSJ</code>, <code>Barrons</code> and <code>Seeking Alpha</code> based on keyword searches. The library also provides a function to get all Nasdaq-listed stock tickers as well as worldwide stock symbols (these need some cleaning still once retrieved).</p>

<p>If there are any issues, ideas or recommendations please feel free to reach out.</p>

<br>

<p>
<i>Changes for v0.1362</i>
<li> Fixed macrotrends </li>

<p>

<p>
<i>Changes for v0.1361</i>
<li> Added chromedriver versions 89.0.4389.23</li>
<li> Added a linux driver </li>
<li> Added a country code option for market watch tickers </li>
<li> Removed Reuters news as they started limiting their search results. </li>

<p>

<p>
<i>Changes for v0.136</i>
<li> Updated NewsData.barrons() to enable article collection from Barrons' company site</li>
<li> Added an option to NewsData.filter() function to choose between filtering on headlines, descriptions or both </li>
<li> Removed the economic data module for now </li>
<p>

<p>
<i>Changes for v0.133</i>
<li> Updated the Windows and Mac Chromedrivers to <code>86.\*.\*\*\*\*.\*\*\*</code> </li>
<li> Updated code for data from Macrotrends </li>
<li> Added function to retrive CFTC data to other data section</li>
<p>

<p>
<i>Changes for v0.13</i>
<li> Restructured the fundamental data module to reduce clutter and simplify the repository </li>
<li> Excluded Bloomberg news headline scrape because of the automation detection  </li>
<li> Debugged news headline scrape </li>
<li> Removed third party price data API wrappers </li>
<li> v0.1312: added option to get press releases from Seeking Alpha, updated WSJ script and Yahoo executive info </li>
<p>


<p>
<i>Changes for v0.12</i>
<li> Added a section to download earnings call transcripts</li>
<li> Added a test file and Travis CI </li>
<li> Debugged failing tests </li>
<p>


<p>
<i>Changes for v0.11</i>
<li> Added function to get option prices from CBOE to the <code>price_data</code> module</li>
<li> Added EIA Petroleum data section to the <code>economic_data</code> module</li>
<li> Updated the Windows and Mac Chromedrivers to <code>85.\*.\*\*\*\*.\*\*\*</code> (had included an older Windows Chromedriver before)</li>
<p>




<br>

<p>
<i>To do list:</i>
<ul>
<li> Refactor the news scrape..</li>
<li> Rework economic data module</li>
<li> Add USDA data </li>
<li> Add social media data (Twitter, Stocktwits, Weibo, Reddit WSB?) </li>
<li> Add async requests, multiple/batch download options, proxies.. </li>
</ul>
</p>

<br>

## <div id="0">Documentation</div>

<ol>
<li>
<a href = "#A2">Installation</a>
</li>
<li><a href = "#A3">Function index</a></li>
<li>
<a href = "#A4">Company fundamental data</a><ul>
	<li><a href = "#A42">Financial statements</a></li>
	<li><a href = "#A41">Financial ratios and key metrics</a></li>
	<li><a href = "#A43">Earnings and revenue estimates</a></li>
	<li><a href = "#A48">Earnings call transcripts</a></li>
	<li><a href = "#A44">Insider transactions and analyst ratings</a></li>
	<li><a href = "#A46">ESG scores</a></li>
	<li><a href = "#A47">Company profile</a></li>
	</ul>
</li>
<li>
<a href = "#A5">Price data</a><ul>
	<li><a href = "#A51">Stock prices</a></li>
	<li><a href = "#A52">Option prices</a></li>
	<li><a href = "#A53">Futures prices</a></li>
	</ul>

</li>
<li><a href = "#A7">News data</a></li>
<li><a href = "#A8">Other data</a></li>
<li><a href = "#A9">Sources</a></li>
<li><a href = "#A10">License</a></li>
</ol>

## <div id="A2">Installation</div>

Python3 is required. Google Chrome version <code>89.\*.\*\*\*\*.\*\*\*</code> or higher is required for some functions involving Selenium (can be found <a href="https://chromereleases.googleblog.com/">here</a>).

Note that Selenium may not be able to use Chrome in combination with Firewalls and the functions may fail to execute..

```python
$ pip install finpie
```

### Requirements

```
beautifulsoup4>=4.9.1
dask>=2.11.0
numpy>=1.18.2
pandas>=1.0.1
requests>=2.22.0
requests_html>=0.10.0
selenium>=3.141.0
tqdm>=4.32.1
```

<div align="right"><a href="#0">Back to top</a> </div>



## <div id="A3"> Index </div>

|Output|Data Output|Runtime|
|:-----|:-----|:-----:|
|<b>Company Fundamentals</b>|||
|<b>fd = Fundamentals( ticker, source, freq )</b>|||
|<u>Financial statements</u>|||
|<li> <a id='i7' href='#f7'>fd.income\_statement()</a> </li>|up to 2005|Slow, depends on source|
|<li> <a id='i8' href='#f8'>fd.balance\_sheet()</a> </li>|up to 2005|Slow, depends on source|
|<li> <a id='i9' href='#f9'>fd.cashflow\_statement()</a> </li>|up to 2005|Slow, depends on source|
|<u>Financial ratios and key metrics</u>|||
|<li> <a id='i102' href='#f102'>fd.ratios()</a> </li>|up to 2005|Slow|
|<li> <a id='i2' href='#f2'>fd.key_metrics()</a> </li>|Most recent data|Fast|
|<u>Earnings and revenue estimates</u>|||
|<li> <a id='i11' href='#f11'>fd.earnings\_estimates()</a> </li>|Most recent data|Fast|
|<li> <a id='i12' href='#f12'>fd.earnings\_estimates\_trends()</a> </li>|Recent trend|Fast|
|<li> <a id='i13' href='#f13'>fd.earnings\_history()</a> </li>|4 quarters|Fast|
|<li> <a id='i14' href='#f14'>fd.revenue\_estimates()</a> </li>|Most recent data|Fast|
|<li> <a id='i15' href='#f15'>fd.growth\_estimates()</a> </li>|Most recent data|Fast|
|<u>Earnings call transcripts</u>|||
|<li> <a id='i131' href='#f131'>fd.transcripts()</a> </li>|up to 2018|Slow|
|<u>Insider transactions and analyst ratings</u>|||
|<li> <a id='i16' href='#f16'>fd.insider\_transactions()</a> </li>|Most recent data|Fast|
|<li> <a id='i17' href='#f17'>fd.analyst\_ratings()</a> </li>|Most recent data|Fast|
|<u>ESG data</u>|||
|<li> <a id='i18' href='#f18'>fd.esg\_score()</a> </li>|Most recent data|Fast|
|<li> <a id='i19' href='#f19'>fd.corporate\_governance\_score()</a> </li>|Most recent data|Fast|
|<u>Company profile</u>|||
|<li> <a id='i20' href='#f20'>fd.profile()</a> </li>|Most recent data|Fast|
|<li> <a id='i21' href='#f21'>fd.executives\_info()</a> </li>|Most recent data|Fast|
|<b>Price data</b>|||
|<li> <a id='i22' href='#f22'>historical\_prices(ticker)</a> </li>|Timeseries|Fast|
|<li> <a id='i27' href='#f27'>yahoo\_option\_chain(ticker)</a> </li>|Most recent data|Fast|
|<li> <a id='i106' href='#f106'>cboe\_option\_chain(ticker)</a> </li>|Most recent data|Fast|
|<li> <a id='i28' href='#f28'>historical\_futures\_contracts(date\_range)</a> </li>|Timeseries|Very slow|
|<li> <a id='i29' href='#f29'>futures\_contracts(date)</a> </li>|Any date|Fast|
|<b>News data</b>|||
|<b>news = NewsData( ticker, keyword_string )</b>|||
|<li> <a id='i78' href='#f78'>news.barrons()</a> </li>|Timeseries|Slow|
|<li> <a id='i80' href='#f80'>news.cnbc()</a> </li>|Timeseries|Very slow|
|<li> <a id='i81' href='#f81'>news.ft()</a> </li>|Timeseries|Very slow|
|<li> <a id='i82' href='#f82'>news.nyt()</a> </li>|Timeseries|Very slow|
|<li> <a id='i84' href='#f84'>news.seeking\_alpha()</a> </li>|Timeseries|Slow|
|<li> <a id='i85' href='#f85'>news.wsj()</a> </li>|Timeseries|Very slow|
|<b>Other data</b>|||
|<li> <a id='i86' href='#f86'>nasdaq\_tickers()</a> </li>|List of stock tickers|Fast|
|<li> <a id='i87' href='#f87'>global\_tickers()</a> </li>|List of stock tickers|Slow|
|<li> <a id='i132' href='#f132'>cftc()</a> </li>|Timeseries|Not that slow|


-----

<br>

## <div id="A4"> Company Fundamental data</a>

<div align="right"><a href="#0">Back to top</a> </div>

The functions below enable you to download financial statements, valuation ratios and key financial statistics as well as analyst ratings, insider transactions, ESG scores and company profiles.

The data is pulled from <code>Yahoo Finance</code>, <code>Marketwatch.com</code> , <code>Finviz.com</code> and <code>Macrotrends.com</code>. The macrotrends scrape runs on Selenium and the website might sometimes fail to load. The function may just need to be re-run to work (assuming the ticker is available on the website). As a remedy it might sometimes help to set <code>macrotrends().head = True</code> which will then open a browser window while scraping the data.


```python
import finpie # or import finpie.fundamental_data

# default:
# source = 'macrotrends'
# freq = 'A'
fd = finpie.Fundamentals(ticker, source = 'macrotrends', freq = 'A')

# source options for financial statements and key metrics:
# 'yahoo', 'marketwatch', 'macrotrends'
# freq options:
# 'A', 'Q'

# default key metrics for marketwatch and macrotrends come from Finviz

```

<br>



##	 <div id="A42"> <li> Financial statements <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>



#### <div id="f7"><i>Fundamentals(ticker, source, freq)<b>.income_statement()</b></i></div>


<ul>
<li>Returns a dataframe with income statements from either Macrotrends.com, Yahoo Finance or Marketwatch. Default source is 'macrotrends'.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: 'yahoo', 'marketwatch', 'macrotrends', default: 'macrotrends' </li>
	<li> <code>freq</code>: 'A' (annual data), 'Q' (quarterly data), default: 'A' </li>
	</ul>
</ul>
</ul>

<br>


<details>
<summary><i> Default Example </i></summary>

```python
fd = finpie.Fundamentals('AAPL', freq = 'A')
fd.income_statement()
```

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>revenue</th>      <th>cost_of_goods_sold</th>      <th>gross_profit</th>      <th>research_and_development_expenses</th>      <th>sganda_expenses</th>      <th>other_operating_income_or_expenses</th>      <th>operating_expenses</th>      <th>operating_income</th>      <th>total_nonoperating_income_to_expense</th>      <th>pretax_income</th>      <th>income_taxes</th>      <th>income_after_taxes</th>      <th>other_income</th>      <th>income_from_continuous_operations</th>      <th>income_from_discontinued_operations</th>      <th>net_income</th>      <th>ebitda</th>      <th>ebit</th>      <th>basic_shares_outstanding</th>      <th>shares_outstanding</th>      <th>basic_eps</th>      <th>eps__earnings_per_share</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2005-09-30</th>      <td>13931.0</td>      <td>9889.0</td>      <td>4042.0</td>      <td>535.0</td>      <td>1864.0</td>      <td>NaN</td>      <td>12288.0</td>      <td>1643.0</td>      <td>165.0</td>      <td>1808.0</td>      <td>480.0</td>      <td>1328.0</td>      <td>NaN</td>      <td>1328.0</td>      <td>NaN</td>      <td>1328.0</td>      <td>1822.0</td>      <td>1643.0</td>      <td>22636.0</td>      <td>23993.0</td>      <td>0.06</td>      <td>0.06</td>    </tr>    <tr>      <th>2006-09-30</th>      <td>19315.0</td>      <td>13717.0</td>      <td>5598.0</td>      <td>712.0</td>      <td>2433.0</td>      <td>NaN</td>      <td>16862.0</td>      <td>2453.0</td>      <td>365.0</td>      <td>2818.0</td>      <td>829.0</td>      <td>1989.0</td>      <td>NaN</td>      <td>1989.0</td>      <td>NaN</td>      <td>1989.0</td>      <td>2678.0</td>      <td>2453.0</td>      <td>23634.0</td>      <td>24571.0</td>      <td>0.08</td>      <td>0.08</td>    </tr>    <tr>      <th>2007-09-30</th>      <td>24578.0</td>      <td>16426.0</td>      <td>8152.0</td>      <td>782.0</td>      <td>2963.0</td>      <td>NaN</td>      <td>20171.0</td>      <td>4407.0</td>      <td>599.0</td>      <td>5006.0</td>      <td>1511.0</td>      <td>3495.0</td>      <td>NaN</td>      <td>3495.0</td>      <td>NaN</td>      <td>3495.0</td>      <td>4734.0</td>      <td>4407.0</td>      <td>24209.0</td>      <td>24900.0</td>      <td>0.14</td>      <td>0.14</td>    </tr>    <tr>      <th>2008-09-30</th>      <td>37491.0</td>      <td>24294.0</td>      <td>13197.0</td>      <td>1109.0</td>      <td>3761.0</td>      <td>NaN</td>      <td>29164.0</td>      <td>8327.0</td>      <td>620.0</td>      <td>8947.0</td>      <td>2828.0</td>      <td>6119.0</td>      <td>NaN</td>      <td>6119.0</td>      <td>NaN</td>      <td>6119.0</td>      <td>8823.0</td>      <td>8327.0</td>      <td>24685.0</td>      <td>25260.0</td>      <td>0.25</td>      <td>0.24</td>    </tr>    <tr>      <th>2009-09-30</th>      <td>42905.0</td>      <td>25683.0</td>      <td>17222.0</td>      <td>1333.0</td>      <td>4149.0</td>      <td>NaN</td>      <td>31165.0</td>      <td>11740.0</td>      <td>326.0</td>      <td>12066.0</td>      <td>3831.0</td>      <td>8235.0</td>      <td>NaN</td>      <td>8235.0</td>      <td>NaN</td>      <td>8235.0</td>      <td>12474.0</td>      <td>11740.0</td>      <td>25004.0</td>      <td>25396.0</td>      <td>0.33</td>      <td>0.32</td>    </tr>  </tbody></table>



</details>

<details>
<summary><i> Yahoo Example </i></summary>

```python
fd = finpie.Fundamentals('AAPL', source = 'yahoo') # no frequency choice for Yahoo...
fd.income_statement()
```

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>total_revenue</th>      <th>cost_of_revenue</th>      <th>gross_profit</th>      <th>operating_expense</th>      <th>operating_income</th>      <th>net_non_operating_interest_income_expense</th>      <th>other_income_expense</th>      <th>pretax_income</th>      <th>tax_provision</th>      <th>net_income_common_stockholders</th>      <th>diluted_ni_available_to_com_stockholders</th>      <th>basic_eps</th>      <th>diluted_eps</th>      <th>basic_average_shares</th>      <th>diluted_average_shares</th>      <th>total_operating_income_as_reported</th>      <th>total_expenses</th>      <th>net_income_from_continuing_and_discontinued_operation</th>      <th>normalized_income</th>      <th>interest_income</th>      <th>interest_expense</th>      <th>net_interest_income</th>      <th>ebit</th>      <th>ebitda</th>      <th>reconciled_cost_of_revenue</th>      <th>reconciled_depreciation</th>      <th>net_income_from_continuing_operation_net_minority_interest</th>      <th>normalized_ebitda</th>      <th>tax_rate_for_calcs</th>      <th>tax_effect_of_unusual_items</th>      <th>ticker</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2019-09-30</th>      <td>260174000</td>      <td>161782000</td>      <td>98392000</td>      <td>34462000</td>      <td>63930000</td>      <td>1385000</td>      <td>422000</td>      <td>65737000</td>      <td>10481000</td>      <td>55256000</td>      <td>55256000</td>      <td>0.003</td>      <td>0.003</td>      <td>18471336</td>      <td>18595652</td>      <td>63930000</td>      <td>196244000</td>      <td>55256000</td>      <td>55256000</td>      <td>4961000</td>      <td>3576000</td>      <td>1385000</td>      <td>69313000</td>      <td>NaN</td>      <td>161782000</td>      <td>12547000</td>      <td>55256000</td>      <td>81860000</td>      <td>0</td>      <td>0</td>      <td>AAPL</td>    </tr>    <tr>      <th>2018-09-30</th>      <td>265595000</td>      <td>163756000</td>      <td>101839000</td>      <td>30941000</td>      <td>70898000</td>      <td>2446000</td>      <td>-441000</td>      <td>72903000</td>      <td>13372000</td>      <td>59531000</td>      <td>59531000</td>      <td>0.003</td>      <td>0.003</td>      <td>19821508</td>      <td>20000436</td>      <td>70898000</td>      <td>194697000</td>      <td>59531000</td>      <td>59531000</td>      <td>5686000</td>      <td>3240000</td>      <td>2446000</td>      <td>76143000</td>      <td>NaN</td>      <td>163756000</td>      <td>10903000</td>      <td>59531000</td>      <td>87046000</td>      <td>0</td>      <td>0</td>      <td>AAPL</td>    </tr>    <tr>      <th>2017-09-30</th>      <td>229234000</td>      <td>141048000</td>      <td>88186000</td>      <td>26842000</td>      <td>61344000</td>      <td>2878000</td>      <td>-133000</td>      <td>64089000</td>      <td>15738000</td>      <td>48351000</td>      <td>48351000</td>      <td>0.0023</td>      <td>0.0023</td>      <td>20868968</td>      <td>21006768</td>      <td>61344000</td>      <td>167890000</td>      <td>48351000</td>      <td>48351000</td>      <td>5201000</td>      <td>2323000</td>      <td>2878000</td>      <td>66412000</td>      <td>NaN</td>      <td>141048000</td>      <td>10157000</td>      <td>48351000</td>      <td>76569000</td>      <td>0</td>      <td>0</td>      <td>AAPL</td>    </tr>  </tbody></table>

</details>

<details>
<summary><i> Marketwatch Example </i></summary>

```python
fd = Fundamentals('AAPL', source = 'marketwatch', freq = 'Q')
fd.income_statement()
```

<center><small><small>


<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>sales_revenue</th>      <th>sales_growth</th>      <th>cost_of_goods_sold_(cogs)_incl_danda</th>      <th>cogs_excluding_danda</th>      <th>depreciation_and_amortization_expense</th>      <th>depreciation</th>      <th>amortization_of_intangibles</th>      <th>cogs_growth</th>      <th>gross_income</th>      <th>gross_income_growth</th>      <th>gross_profit_margin</th>      <th>sganda_expense</th>      <th>research_and_development</th>      <th>other_sganda</th>      <th>sga_growth</th>      <th>other_operating_expense</th>      <th>unusual_expense</th>      <th>ebit_after_unusual_expense</th>      <th>non_operating_income_expense</th>      <th>non-operating_interest_income</th>      <th>equity_in_affiliates_(pretax)</th>      <th>interest_expense</th>      <th>interest_expense_growth</th>      <th>gross_interest_expense</th>      <th>interest_capitalized</th>      <th>pretax_income</th>      <th>pretax_income_growth</th>      <th>pretax_margin</th>      <th>income_tax</th>      <th>income_tax_-_current_domestic</th>      <th>income_tax_-_current_foreign</th>      <th>income_tax_-_deferred_domestic</th>      <th>income_tax_-_deferred_foreign</th>      <th>income_tax_credits</th>      <th>equity_in_affiliates</th>      <th>other_after_tax_income_(expense)</th>      <th>consolidated_net_income</th>      <th>minority_interest_expense</th>      <th>net_income</th>      <th>net_income_growth</th>      <th>net_margin_growth</th>      <th>extraordinaries_and_discontinued_operations</th>      <th>extra_items_and_gain_loss_sale_of_assets</th>      <th>cumulative_effect_-_accounting_chg</th>      <th>discontinued_operations</th>      <th>net_income_after_extraordinaries</th>      <th>preferred_dividends</th>      <th>net_income_available_to_common</th>      <th>eps_(basic)</th>      <th>eps_(basic)_growth</th>      <th>basic_shares_outstanding</th>      <th>eps_(diluted)</th>      <th>eps_(diluted)_growth</th>      <th>diluted_shares_outstanding</th>      <th>ebitda</th>      <th>ebitda_growth</th>      <th>ebitda_margin</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2019-06-30</th>      <td>5.374e+10</td>      <td>nan</td>      <td>3.357e+10</td>      <td>3.064e+10</td>      <td>2.93e+09</td>      <td>2.93e+09</td>      <td>nan</td>      <td>nan</td>      <td>2.017e+10</td>      <td>nan</td>      <td>nan</td>      <td>8.68e+09</td>      <td>4.26e+09</td>      <td>4.43e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>9.8e+07</td>      <td>1.19e+09</td>      <td>nan</td>      <td>8.66e+08</td>      <td>nan</td>      <td>8.66e+08</td>      <td>nan</td>      <td>1.191e+10</td>      <td>nan</td>      <td>nan</td>      <td>1.87e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.004e+10</td>      <td>nan</td>      <td>1.004e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.004e+10</td>      <td>nan</td>      <td>1.004e+10</td>      <td>0.55</td>      <td>nan</td>      <td>1.828e+10</td>      <td>0.55</td>      <td>nan</td>      <td>1.841e+10</td>      <td>1.442e+10</td>      <td>nan</td>      <td>nan</td>    </tr>    <tr>      <th>2019-09-30</th>      <td>6.394e+10</td>      <td>0.1897</td>      <td>3.977e+10</td>      <td>3.784e+10</td>      <td>1.93e+09</td>      <td>1.93e+09</td>      <td>nan</td>      <td>0.1848</td>      <td>2.417e+10</td>      <td>0.1979</td>      <td>nan</td>      <td>8.69e+09</td>      <td>4.11e+09</td>      <td>4.58e+09</td>      <td>0.0006</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>3.54e+08</td>      <td>1.11e+09</td>      <td>nan</td>      <td>8.1e+08</td>      <td>-0.0647</td>      <td>8.1e+08</td>      <td>nan</td>      <td>1.613e+10</td>      <td>0.354</td>      <td>nan</td>      <td>2.44e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.369e+10</td>      <td>nan</td>      <td>1.369e+10</td>      <td>0.3626</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.369e+10</td>      <td>nan</td>      <td>1.369e+10</td>      <td>0.76</td>      <td>0.3868</td>      <td>1.796e+10</td>      <td>0.76</td>      <td>0.387</td>      <td>1.808e+10</td>      <td>1.741e+10</td>      <td>0.2071</td>      <td>nan</td>    </tr>    <tr>      <th>2019-12-31</th>      <td>9.172e+10</td>      <td>0.4346</td>      <td>5.677e+10</td>      <td>5.396e+10</td>      <td>2.82e+09</td>      <td>2.82e+09</td>      <td>nan</td>      <td>0.4275</td>      <td>3.495e+10</td>      <td>0.4463</td>      <td>nan</td>      <td>9.65e+09</td>      <td>4.45e+09</td>      <td>5.2e+09</td>      <td>0.1105</td>      <td>nan</td>      <td>-1.28e+08</td>      <td>1.28e+08</td>      <td>2.29e+08</td>      <td>1.05e+09</td>      <td>nan</td>      <td>7.85e+08</td>      <td>-0.0309</td>      <td>7.85e+08</td>      <td>nan</td>      <td>2.592e+10</td>      <td>0.6071</td>      <td>nan</td>      <td>3.68e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>2.224e+10</td>      <td>nan</td>      <td>2.224e+10</td>      <td>0.6247</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>2.224e+10</td>      <td>nan</td>      <td>2.224e+10</td>      <td>1.26</td>      <td>0.6526</td>      <td>1.766e+10</td>      <td>1.25</td>      <td>0.6487</td>      <td>1.782e+10</td>      <td>2.812e+10</td>      <td>0.6151</td>      <td>nan</td>    </tr>    <tr>      <th>2020-03-31</th>      <td>5.835e+10</td>      <td>-0.3639</td>      <td>3.593e+10</td>      <td>3.315e+10</td>      <td>2.79e+09</td>      <td>2.79e+09</td>      <td>nan</td>      <td>-0.3671</td>      <td>2.242e+10</td>      <td>-0.3586</td>      <td>nan</td>      <td>9.52e+09</td>      <td>4.57e+09</td>      <td>4.95e+09</td>      <td>-0.0136</td>      <td>nan</td>      <td>-1.26e+08</td>      <td>1.26e+08</td>      <td>-1.82e+08</td>      <td>1.05e+09</td>      <td>nan</td>      <td>7.57e+08</td>      <td>-0.0357</td>      <td>7.57e+08</td>      <td>nan</td>      <td>1.314e+10</td>      <td>-0.4932</td>      <td>nan</td>      <td>1.89e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.125e+10</td>      <td>nan</td>      <td>1.125e+10</td>      <td>-0.4941</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.125e+10</td>      <td>nan</td>      <td>1.125e+10</td>      <td>0.65</td>      <td>-0.4877</td>      <td>1.744e+10</td>      <td>0.64</td>      <td>-0.4883</td>      <td>1.762e+10</td>      <td>1.569e+10</td>      <td>-0.4422</td>      <td>nan</td>    </tr>    <tr>      <th>2020-06-30</th>      <td>5.942e+10</td>      <td>0.0183</td>      <td>3.737e+10</td>      <td>3.462e+10</td>      <td>2.75e+09</td>      <td>2.75e+09</td>      <td>nan</td>      <td>0.04</td>      <td>2.205e+10</td>      <td>-0.0164</td>      <td>0.3711</td>      <td>9.59e+09</td>      <td>4.76e+09</td>      <td>4.83e+09</td>      <td>0.0076</td>      <td>nan</td>      <td>-1.19e+08</td>      <td>1.19e+08</td>      <td>3.55e+08</td>      <td>901M</td>      <td>nan</td>      <td>6.97e+08</td>      <td>-0.0793</td>      <td>6.97e+08</td>      <td>nan</td>      <td>1.314e+10</td>      <td>0.0002</td>      <td>0.2211</td>      <td>1.88e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.125e+10</td>      <td>nan</td>      <td>1.125e+10</td>      <td>0.0004</td>      <td>0.1894</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.125e+10</td>      <td>nan</td>      <td>1.125e+10</td>      <td>0.65</td>      <td>0.0113</td>      <td>1.725e+10</td>      <td>0.65</td>      <td>0.0117</td>      <td>1.742e+10</td>      <td>1.521e+10</td>      <td>-0.0302</td>      <td>0.256</td>    </tr>  </tbody></table>


</small></small></center>

</details>




<div align="right"> <a href="#i7">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id="f8"><i>Fundamentals(ticker, source, freq).balance\_sheet()</i></div>

<ul>
<li>Returns a dataframe with balance sheets from either Macrotrends.com, Yahoo Finance or Marketwatch. Default source is 'macrotrends'.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: 'yahoo', 'marketwatch', 'macrotrends', default: 'macrotrends' </li>
	<li> <code>freq</code>: 'A' (annual data), 'Q' (quarterly data), default: 'A' </li>
	</ul>
</ul>
</ul>

<br>


<details>
<summary><i> Default Example </i></summary>

```python
fd = Fundamentals('AAPL', freq = 'A')
fd.balance_sheet()
```

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>cash_on_hand</th>      <th>receivables</th>      <th>inventory</th>      <th>prepaid_expenses</th>      <th>other_current_assets</th>      <th>total_current_assets</th>      <th>property,_plant,_and_equipment</th>      <th>longterm_investments</th>      <th>goodwill_and_intangible_assets</th>      <th>other_longterm_assets</th>      <th>total_longterm_assets</th>      <th>total_assets</th>      <th>total_current_liabilities</th>      <th>long_term_debt</th>      <th>other_noncurrent_liabilities</th>      <th>total_long_term_liabilities</th>      <th>total_liabilities</th>      <th>common_stock_net</th>      <th>retained_earnings_(accumulated_deficit)</th>      <th>comprehensive_income</th>      <th>other_share_holders_equity</th>      <th>share_holder_equity</th>      <th>total_liabilities_and_share_holders_equity</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2005-09-30</th>      <td>8261.0</td>      <td>895.0</td>      <td>165.0</td>      <td>NaN</td>      <td>648.0</td>      <td>10300.0</td>      <td>817.0</td>      <td>NaN</td>      <td>96.0</td>      <td>303.0</td>      <td>1216.0</td>      <td>11516.0</td>      <td>3487.0</td>      <td>NaN</td>      <td>601.0</td>      <td>601.0</td>      <td>4088.0</td>      <td>3564.0</td>      <td>3925.0</td>      <td>NaN</td>      <td>NaN</td>      <td>7428.0</td>      <td>11516.0</td>    </tr>    <tr>      <th>2006-09-30</th>      <td>10110.0</td>      <td>1252.0</td>      <td>270.0</td>      <td>NaN</td>      <td>2270.0</td>      <td>14509.0</td>      <td>1281.0</td>      <td>NaN</td>      <td>177.0</td>      <td>1238.0</td>      <td>2696.0</td>      <td>17205.0</td>      <td>6443.0</td>      <td>NaN</td>      <td>778.0</td>      <td>778.0</td>      <td>7221.0</td>      <td>4355.0</td>      <td>5607.0</td>      <td>22.0</td>      <td>NaN</td>      <td>9984.0</td>      <td>17205.0</td>    </tr>    <tr>      <th>2007-09-30</th>      <td>15386.0</td>      <td>1637.0</td>      <td>346.0</td>      <td>NaN</td>      <td>3805.0</td>      <td>21956.0</td>      <td>1832.0</td>      <td>NaN</td>      <td>337.0</td>      <td>1222.0</td>      <td>3391.0</td>      <td>25347.0</td>      <td>9280.0</td>      <td>NaN</td>      <td>1535.0</td>      <td>1535.0</td>      <td>10815.0</td>      <td>5368.0</td>      <td>9101.0</td>      <td>63.0</td>      <td>NaN</td>      <td>14532.0</td>      <td>25347.0</td>    </tr>    <tr>      <th>2008-09-30</th>      <td>22111.0</td>      <td>2422.0</td>      <td>509.0</td>      <td>NaN</td>      <td>3920.0</td>      <td>30006.0</td>      <td>2455.0</td>      <td>2379.0</td>      <td>492.0</td>      <td>839.0</td>      <td>6165.0</td>      <td>36171.0</td>      <td>11361.0</td>      <td>NaN</td>      <td>1745.0</td>      <td>2513.0</td>      <td>13874.0</td>      <td>7177.0</td>      <td>15129.0</td>      <td>9.0</td>      <td>NaN</td>      <td>22297.0</td>      <td>36171.0</td>    </tr>    <tr>      <th>2009-09-30</th>      <td>23464.0</td>      <td>5057.0</td>      <td>455.0</td>      <td>NaN</td>      <td>1444.0</td>      <td>31555.0</td>      <td>2954.0</td>      <td>10528.0</td>      <td>453.0</td>      <td>2011.0</td>      <td>15946.0</td>      <td>47501.0</td>      <td>11506.0</td>      <td>NaN</td>      <td>3502.0</td>      <td>4355.0</td>      <td>15861.0</td>      <td>8210.0</td>      <td>23353.0</td>      <td>77.0</td>      <td>NaN</td>      <td>31640.0</td>      <td>47501.0</td>    </tr>  </tbody></table>



</details>

<details>
<summary><i> Yahoo Example </i></summary>

```python
fd = Fundamentals('AAPL', source = 'yahoo') # no frequency choice for Yahoo...
fd.balance_sheet()
```

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>total_assets</th>      <th>total_liabilities_net_minority_interest</th>      <th>total_equity_gross_minority_interest</th>      <th>total_capitalization</th>      <th>common_stock_equity</th>      <th>net_tangible_assets</th>      <th>working_capital</th>      <th>invested_capital</th>      <th>tangible_book_value</th>      <th>total_debt</th>      <th>net_debt</th>      <th>share_issued</th>      <th>ordinary_shares_number</th>      <th>ticker</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2019-09-30</th>      <td>338516000</td>      <td>248028000</td>      <td>90488000</td>      <td>182295000</td>      <td>90488000</td>      <td>90488000</td>      <td>57101000</td>      <td>198535000</td>      <td>90488000</td>      <td>108047000</td>      <td>59203000</td>      <td>17772944</td>      <td>17772944</td>      <td>AAPL</td>    </tr>    <tr>      <th>2018-09-30</th>      <td>365725000</td>      <td>258578000</td>      <td>107147000</td>      <td>200882000</td>      <td>107147000</td>      <td>107147000</td>      <td>14473000</td>      <td>221630000</td>      <td>107147000</td>      <td>114483000</td>      <td>88570000</td>      <td>19019944</td>      <td>19019944</td>      <td>AAPL</td>    </tr>    <tr>      <th>2017-09-30</th>      <td>375319000</td>      <td>241272000</td>      <td>134047000</td>      <td>231254000</td>      <td>134047000</td>      <td>126032000</td>      <td>27831000</td>      <td>249727000</td>      <td>126032000</td>      <td>115680000</td>      <td>95391000</td>      <td>20504804</td>      <td>20504804</td>      <td>AAPL</td>    </tr>  </tbody></table>




</details>

<details>
<summary><i> Marketwatch Example </i></summary>

```python
fd = Fundamentals('AAPL', source = 'marketwatch', freq = 'Q')
fd.balance_sheet()
```

<center><small><small>


<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>cash_and_short_term_investments</th>      <th>cash_only</th>      <th>short-term_investments</th>      <th>cash_and_short_term_investments_growth</th>      <th>cash_and_st_investments___total_assets</th>      <th>total_accounts_receivable</th>      <th>accounts_receivables_net</th>      <th>accounts_receivables_gross</th>      <th>bad_debt_doubtful_accounts</th>      <th>other_receivables</th>      <th>accounts_receivable_growth</th>      <th>accounts_receivable_turnover</th>      <th>inventories</th>      <th>finished_goods</th>      <th>work_in_progress</th>      <th>raw_materials</th>      <th>progress_payments_and_other</th>      <th>other_current_assets</th>      <th>miscellaneous_current_assets</th>      <th>total_current_assets</th>      <th>net_property_plant_and_equipment</th>      <th>property_plant_and_equipment_-_gross</th>      <th>buildings</th>      <th>land_and_improvements</th>      <th>computer_software_and_equipment</th>      <th>other_property_plant_and_equipment</th>      <th>accumulated_depreciation</th>      <th>total_investments_and_advances</th>      <th>other_long-term_investments</th>      <th>long-term_note_receivable</th>      <th>intangible_assets</th>      <th>net_goodwill</th>      <th>net_other_intangibles</th>      <th>other_assets</th>      <th>tangible_other_assets</th>      <th>total_assets</th>      <th>assets_-_total_-_growth</th>      <th>st_debt_and_current_portion_lt_debt</th>      <th>short_term_debt</th>      <th>current_portion_of_long_term_debt</th>      <th>accounts_payable</th>      <th>accounts_payable_growth</th>      <th>income_tax_payable</th>      <th>other_current_liabilities</th>      <th>dividends_payable</th>      <th>accrued_payroll</th>      <th>miscellaneous_current_liabilities</th>      <th>total_current_liabilities</th>      <th>long-term_debt</th>      <th>long-term_debt_excl_capitalized_leases</th>      <th>non-convertible_debt</th>      <th>convertible_debt</th>      <th>capitalized_lease_obligations</th>      <th>provision_for_risks_and_charges</th>      <th>deferred_taxes</th>      <th>deferred_taxes_-_credit</th>      <th>deferred_taxes_-_debit</th>      <th>other_liabilities</th>      <th>other_liabilities_(excl_deferred_income)</th>      <th>deferred_income</th>      <th>total_liabilities</th>      <th>non-equity_reserves</th>      <th>total_liabilities___total_assets</th>      <th>preferred_stock_(carrying_value)</th>      <th>redeemable_preferred_stock</th>      <th>non-redeemable_preferred_stock</th>      <th>common_equity_(total)</th>      <th>common_stock_par_carry_value</th>      <th>retained_earnings</th>      <th>esop_debt_guarantee</th>      <th>cumulative_translation_adjustment_unrealized_for_exch_gain</th>      <th>unrealized_gain_loss_marketable_securities</th>      <th>revaluation_reserves</th>      <th>treasury_stock</th>      <th>common_equity___total_assets</th>      <th>total_shareholders\'_equity</th>      <th>total_shareholders\'_equity___total_assets</th>      <th>accumulated_minority_interest</th>      <th>total_equity</th>      <th>liabilities_and_shareholders\'_equity</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2019-06-30</th>      <td>9.488e+10</td>      <td>2.29e+10</td>      <td>nan</td>      <td>nan</td>      <td>0.2944</td>      <td>2.647e+10</td>      <td>1.415e+10</td>      <td>1.415e+10</td>      <td>nan</td>      <td>1.233e+10</td>      <td>nan</td>      <td>2.03</td>      <td>3.36e+09</td>      <td>3.36e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.026e+10</td>      <td>1.026e+10</td>      <td>1.3497e+11</td>      <td>3.764e+10</td>      <td>9.398e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>5.635e+10</td>      <td>1.1735e+11</td>      <td>1.1735e+11</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>3.228e+10</td>      <td>3.228e+10</td>      <td>3.2224e+11</td>      <td>nan</td>      <td>2.348e+10</td>      <td>9.95e+09</td>      <td>1.353e+10</td>      <td>2.912e+10</td>      <td>nan</td>      <td>nan</td>      <td>3.711e+10</td>      <td>nan</td>      <td>nan</td>      <td>3.711e+10</td>      <td>8.97e+10</td>      <td>8.494e+10</td>      <td>8.494e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>3.052e+10</td>      <td>1.61e+10</td>      <td>1.61e+10</td>      <td>nan</td>      <td>4.52e+09</td>      <td>4.52e+09</td>      <td>nan</td>      <td>2.2578e+11</td>      <td>nan</td>      <td>0.7007</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>9.646e+10</td>      <td>4.337e+10</td>      <td>5.372e+10</td>      <td>nan</td>      <td>-1.18e+09</td>      <td>328M</td>      <td>nan</td>      <td>nan</td>      <td>0.2993</td>      <td>9.646e+10</td>      <td>0.2993</td>      <td>nan</td>      <td>9.646e+10</td>      <td>3.2224e+11</td>    </tr>    <tr>      <th>2019-09-30</th>      <td>1.0058e+11</td>      <td>2.812e+10</td>      <td>nan</td>      <td>0.0601</td>      <td>0.2971</td>      <td>4.58e+10</td>      <td>2.293e+10</td>      <td>2.293e+10</td>      <td>nan</td>      <td>2.288e+10</td>      <td>0.7302</td>      <td>1.40</td>      <td>4.11e+09</td>      <td>4.11e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.233e+10</td>      <td>1.233e+10</td>      <td>1.6282e+11</td>      <td>3.738e+10</td>      <td>9.596e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>5.858e+10</td>      <td>1.067e+11</td>      <td>1.067e+11</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>3.162e+10</td>      <td>3.162e+10</td>      <td>3.3852e+11</td>      <td>0.0505</td>      <td>1.624e+10</td>      <td>5.98e+09</td>      <td>1.026e+10</td>      <td>4.624e+10</td>      <td>0.588</td>      <td>nan</td>      <td>4.324e+10</td>      <td>nan</td>      <td>nan</td>      <td>4.324e+10</td>      <td>1.0572e+11</td>      <td>9.181e+10</td>      <td>9.181e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>2.955e+10</td>      <td>1.692e+10</td>      <td>1.692e+10</td>      <td>nan</td>      <td>4.04e+09</td>      <td>4.04e+09</td>      <td>nan</td>      <td>2.4803e+11</td>      <td>nan</td>      <td>0.7327</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>9.049e+10</td>      <td>4.517e+10</td>      <td>4.59e+10</td>      <td>nan</td>      <td>-1.46e+09</td>      <td>707M</td>      <td>nan</td>      <td>nan</td>      <td>0.2673</td>      <td>9.049e+10</td>      <td>0.2673</td>      <td>nan</td>      <td>9.049e+10</td>      <td>3.3852e+11</td>    </tr>    <tr>      <th>2019-12-31</th>      <td>1.0723e+11</td>      <td>2.299e+10</td>      <td>nan</td>      <td>0.0661</td>      <td>0.3148</td>      <td>3.995e+10</td>      <td>2.097e+10</td>      <td>2.097e+10</td>      <td>nan</td>      <td>1.898e+10</td>      <td>-0.1279</td>      <td>2.30</td>      <td>4.1e+09</td>      <td>4.1e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.196e+10</td>      <td>1.196e+10</td>      <td>1.6323e+11</td>      <td>4.429e+10</td>      <td>1.0525e+11</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>6.096e+10</td>      <td>1.0173e+11</td>      <td>1.0173e+11</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>3.137e+10</td>      <td>3.137e+10</td>      <td>3.4062e+11</td>      <td>0.0062</td>      <td>1.647e+10</td>      <td>6.24e+09</td>      <td>1.024e+10</td>      <td>4.511e+10</td>      <td>-0.0243</td>      <td>nan</td>      <td>4.058e+10</td>      <td>nan</td>      <td>nan</td>      <td>4.058e+10</td>      <td>1.0216e+11</td>      <td>1.0028e+11</td>      <td>9.308e+10</td>      <td>nan</td>      <td>nan</td>      <td>6.27e+08</td>      <td>2.82e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>2.045e+10</td>      <td>2.045e+10</td>      <td>nan</td>      <td>2.5109e+11</td>      <td>nan</td>      <td>0.7372</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>8.953e+10</td>      <td>4.597e+10</td>      <td>4.398e+10</td>      <td>nan</td>      <td>-1.26e+09</td>      <td>822M</td>      <td>nan</td>      <td>nan</td>      <td>0.2628</td>      <td>8.953e+10</td>      <td>0.2628</td>      <td>nan</td>      <td>8.953e+10</td>      <td>3.4062e+11</td>    </tr>    <tr>      <th>2020-03-31</th>      <td>9.513e+10</td>      <td>2.996e+10</td>      <td>nan</td>      <td>-0.1129</td>      <td>0.2969</td>      <td>3.068e+10</td>      <td>1.572e+10</td>      <td>1.572e+10</td>      <td>nan</td>      <td>1.496e+10</td>      <td>-0.232</td>      <td>1.90</td>      <td>3.33e+09</td>      <td>3.33e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.461e+10</td>      <td>1.461e+10</td>      <td>1.4375e+11</td>      <td>4.399e+10</td>      <td>1.0684e+11</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>6.285e+10</td>      <td>1.0059e+11</td>      <td>1.0059e+11</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>3.207e+10</td>      <td>3.207e+10</td>      <td>3.204e+11</td>      <td>-0.0594</td>      <td>2.163e+10</td>      <td>1.121e+10</td>      <td>1.041e+10</td>      <td>3.242e+10</td>      <td>-0.2813</td>      <td>nan</td>      <td>4.205e+10</td>      <td>nan</td>      <td>nan</td>      <td>4.205e+10</td>      <td>9.609e+10</td>      <td>9.714e+10</td>      <td>8.909e+10</td>      <td>nan</td>      <td>nan</td>      <td>6.29e+08</td>      <td>2.819e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>2.056e+10</td>      <td>2.056e+10</td>      <td>nan</td>      <td>2.4198e+11</td>      <td>nan</td>      <td>0.7552</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>7.843e+10</td>      <td>4.803e+10</td>      <td>3.318e+10</td>      <td>nan</td>      <td>-1.83e+09</td>      <td>-1.47e+09</td>      <td>nan</td>      <td>nan</td>      <td>0.2448</td>      <td>7.843e+10</td>      <td>0.2448</td>      <td>nan</td>      <td>7.843e+10</td>      <td>3.204e+11</td>    </tr>    <tr>      <th>2020-06-30</th>      <td>9.305e+10</td>      <td>2.73e+10</td>      <td>nan</td>      <td>-0.0218</td>      <td>0.2932</td>      <td>3.208e+10</td>      <td>1.788e+10</td>      <td>1.788e+10</td>      <td>nan</td>      <td>1.419e+10</td>      <td>0.0456</td>      <td>1.85</td>      <td>3.98e+09</td>      <td>3.98e+09</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.096e+10</td>      <td>1.096e+10</td>      <td>1.4007e+11</td>      <td>4.385e+10</td>      <td>1.0908e+11</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>6.523e+10</td>      <td>1.0222e+11</td>      <td>1.0222e+11</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>3.121e+10</td>      <td>3.121e+10</td>      <td>3.1734e+11</td>      <td>-0.0095</td>      <td>2.005e+10</td>      <td>1.252e+10</td>      <td>7.53e+09</td>      <td>3.533e+10</td>      <td>0.0896</td>      <td>nan</td>      <td>3.995e+10</td>      <td>nan</td>      <td>nan</td>      <td>3.995e+10</td>      <td>9.532e+10</td>      <td>1.0214e+11</td>      <td>9.405e+10</td>      <td>nan</td>      <td>nan</td>      <td>6.3e+08</td>      <td>2.819e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>1.942e+10</td>      <td>1.942e+10</td>      <td>nan</td>      <td>2.4506e+11</td>      <td>nan</td>      <td>0.7722</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>7.228e+10</td>      <td>4.87e+10</td>      <td>2.414e+10</td>      <td>nan</td>      <td>-1.63e+09</td>      <td>1.61e+09</td>      <td>nan</td>      <td>nan</td>      <td>0.2278</td>      <td>7.228e+10</td>      <td>0.2278</td>      <td>nan</td>      <td>7.228e+10</td>      <td>3.1734e+11</td>    </tr>  </tbody></table>


</small></small></center>

</details>





<div align="right"> <a href="#i8">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <div id="f9"><i>Fundamentals(ticker, source, freq).cashflow\_statement()</i></div>

<ul>
<li>Returns a dataframe with cashflow statements from either Macrotrends.com, Yahoo Finance or Marketwatch. Default source is 'macrotrends'.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: 'yahoo', 'marketwatch', 'macrotrends', default: 'macrotrends' </li>
	<li> <code>freq</code>: 'A' (annual data), 'Q' (quarterly data), default: 'A' </li>
	</ul>
</ul>
</ul>



<br>


<details>
<summary><i> Default Example </i></summary>

```python
fd = Fundamentals('AAPL', freq = 'A')
fd.cashflow_statement()
```

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>net_income_to_loss</th>      <th>total_depreciation_and_amortization__cash_flow</th>      <th>other_noncash_items</th>      <th>total_noncash_items</th>      <th>change_in_accounts_receivable</th>      <th>change_in_inventories</th>      <th>change_in_accounts_payable</th>      <th>change_in_assets_to_liabilities</th>      <th>total_change_in_assets_to_liabilities</th>      <th>cash_flow_from_operating_activities</th>      <th>net_change_in_property,_plant,_and_equipment</th>      <th>net_change_in_intangible_assets</th>      <th>net_acquisitions_to_divestitures</th>      <th>net_change_in_shortterm_investments</th>      <th>net_change_in_longterm_investments</th>      <th>net_change_in_investments__total</th>      <th>investing_activities__other</th>      <th>cash_flow_from_investing_activities</th>      <th>net_longterm_debt</th>      <th>net_current_debt</th>      <th>debt_issuance_to_retirement_net__total</th>      <th>net_common_equity_issued_to_repurchased</th>      <th>net_total_equity_issued_to_repurchased</th>      <th>total_common_and_preferred_stock_dividends_paid</th>      <th>financial_activities__other</th>      <th>cash_flow_from_financial_activities</th>      <th>net_cash_flow</th>      <th>stockbased_compensation</th>      <th>common_stock_dividends_paid</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2005-09-30</th>      <td>1328.0</td>      <td>179.0</td>      <td>536.0</td>      <td>715.0</td>      <td>121.0</td>      <td>64.0</td>      <td>328.0</td>      <td>349.0</td>      <td>492.0</td>      <td>2535.0</td>      <td>260.0</td>      <td>NaN</td>      <td>NaN</td>      <td>2861.0</td>      <td>586.0</td>      <td>2275.0</td>      <td>21.0</td>      <td>2556.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>543.0</td>      <td>543.0</td>      <td>NaN</td>      <td>NaN</td>      <td>543.0</td>      <td>522.0</td>      <td>49.0</td>      <td>NaN</td>    </tr>    <tr>      <th>2006-09-30</th>      <td>1989.0</td>      <td>225.0</td>      <td>231.0</td>      <td>456.0</td>      <td>357.0</td>      <td>105.0</td>      <td>1611.0</td>      <td>1374.0</td>      <td>225.0</td>      <td>2220.0</td>      <td>657.0</td>      <td>28.0</td>      <td>NaN</td>      <td>1057.0</td>      <td>25.0</td>      <td>1032.0</td>      <td>10.0</td>      <td>357.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>318.0</td>      <td>318.0</td>      <td>NaN</td>      <td>6.0</td>      <td>324.0</td>      <td>2901.0</td>      <td>163.0</td>      <td>NaN</td>    </tr>    <tr>      <th>2007-09-30</th>      <td>3495.0</td>      <td>327.0</td>      <td>327.0</td>      <td>654.0</td>      <td>385.0</td>      <td>76.0</td>      <td>1494.0</td>      <td>288.0</td>      <td>1321.0</td>      <td>5470.0</td>      <td>735.0</td>      <td>251.0</td>      <td>NaN</td>      <td>2295.0</td>      <td>17.0</td>      <td>2312.0</td>      <td>49.0</td>      <td>3249.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>365.0</td>      <td>365.0</td>      <td>NaN</td>      <td>374.0</td>      <td>739.0</td>      <td>2960.0</td>      <td>242.0</td>      <td>NaN</td>    </tr>    <tr>      <th>2008-09-30</th>      <td>6119.0</td>      <td>496.0</td>      <td>936.0</td>      <td>1432.0</td>      <td>785.0</td>      <td>163.0</td>      <td>596.0</td>      <td>2397.0</td>      <td>2045.0</td>      <td>9596.0</td>      <td>1091.0</td>      <td>108.0</td>      <td>220.0</td>      <td>6722.0</td>      <td>38.0</td>      <td>6760.0</td>      <td>10.0</td>      <td>8189.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>483.0</td>      <td>483.0</td>      <td>NaN</td>      <td>633.0</td>      <td>1116.0</td>      <td>2523.0</td>      <td>516.0</td>      <td>NaN</td>    </tr>    <tr>      <th>2009-09-30</th>      <td>8235.0</td>      <td>734.0</td>      <td>1750.0</td>      <td>2484.0</td>      <td>939.0</td>      <td>54.0</td>      <td>92.0</td>      <td>233.0</td>      <td>560.0</td>      <td>10159.0</td>      <td>1144.0</td>      <td>69.0</td>      <td>NaN</td>      <td>16046.0</td>      <td>NaN</td>      <td>16046.0</td>      <td>175.0</td>      <td>17434.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>475.0</td>      <td>475.0</td>      <td>NaN</td>      <td>188.0</td>      <td>663.0</td>      <td>6612.0</td>      <td>710.0</td>      <td>NaN</td>    </tr>    <tr>      <th>2010-09-30</th>      <td>14013.0</td>      <td>1027.0</td>      <td>2319.0</td>      <td>3346.0</td>      <td>2142.0</td>      <td>596.0</td>      <td>6307.0</td>      <td>2333.0</td>      <td>1236.0</td>      <td>18595.0</td>      <td>2005.0</td>      <td>116.0</td>      <td>638.0</td>      <td>11075.0</td>      <td>NaN</td>      <td>11075.0</td>      <td>20.0</td>      <td>13854.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>912.0</td>      <td>912.0</td>      <td>NaN</td>      <td>345.0</td>      <td>1257.0</td>      <td>5998.0</td>      <td>879.0</td>      <td>NaN</td>    </tr>    <tr>      <th>2011-09-30</th>      <td>25922.0</td>      <td>1814.0</td>      <td>4036.0</td>      <td>5850.0</td>      <td>143.0</td>      <td>275.0</td>      <td>2515.0</td>      <td>2824.0</td>      <td>5757.0</td>      <td>37529.0</td>      <td>4260.0</td>      <td>3192.0</td>      <td>244.0</td>      <td>32464.0</td>      <td>NaN</td>      <td>32464.0</td>      <td>259.0</td>      <td>40419.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>831.0</td>      <td>831.0</td>      <td>NaN</td>      <td>613.0</td>      <td>1444.0</td>      <td>1446.0</td>      <td>1168.0</td>      <td>NaN</td>    </tr>    <tr>      <th>2012-09-30</th>      <td>41733.0</td>      <td>3277.0</td>      <td>6145.0</td>      <td>9422.0</td>      <td>5551.0</td>      <td>15.0</td>      <td>4467.0</td>      <td>800.0</td>      <td>299.0</td>      <td>50856.0</td>      <td>8295.0</td>      <td>1107.0</td>      <td>350.0</td>      <td>38427.0</td>      <td>NaN</td>      <td>38427.0</td>      <td>48.0</td>      <td>48227.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>665.0</td>      <td>665.0</td>      <td>2488.0</td>      <td>125.0</td>      <td>1698.0</td>      <td>931.0</td>      <td>1740.0</td>      <td>2488.0</td>    </tr>    <tr>      <th>2013-09-30</th>      <td>37037.0</td>      <td>6757.0</td>      <td>3394.0</td>      <td>10151.0</td>      <td>2172.0</td>      <td>973.0</td>      <td>2340.0</td>      <td>7283.0</td>      <td>6478.0</td>      <td>53666.0</td>      <td>8165.0</td>      <td>911.0</td>      <td>496.0</td>      <td>24042.0</td>      <td>NaN</td>      <td>24042.0</td>      <td>160.0</td>      <td>33774.0</td>      <td>16896.0</td>      <td>NaN</td>      <td>16896.0</td>      <td>22330.0</td>      <td>22330.0</td>      <td>10564.0</td>      <td>381.0</td>      <td>16379.0</td>      <td>3513.0</td>      <td>2253.0</td>      <td>10564.0</td>    </tr>    <tr>      <th>2014-09-30</th>      <td>39510.0</td>      <td>7946.0</td>      <td>5210.0</td>      <td>13156.0</td>      <td>4232.0</td>      <td>76.0</td>      <td>5938.0</td>      <td>5417.0</td>      <td>7047.0</td>      <td>59713.0</td>      <td>9571.0</td>      <td>242.0</td>      <td>3765.0</td>      <td>9017.0</td>      <td>10.0</td>      <td>9027.0</td>      <td>26.0</td>      <td>22579.0</td>      <td>11960.0</td>      <td>6306.0</td>      <td>18266.0</td>      <td>44270.0</td>      <td>44270.0</td>      <td>11126.0</td>      <td>419.0</td>      <td>37549.0</td>      <td>415.0</td>      <td>2863.0</td>      <td>11126.0</td>    </tr>    <tr>      <th>2015-09-30</th>      <td>53394.0</td>      <td>11257.0</td>      <td>5353.0</td>      <td>16610.0</td>      <td>417.0</td>      <td>238.0</td>      <td>5001.0</td>      <td>6082.0</td>      <td>11262.0</td>      <td>81266.0</td>      <td>11247.0</td>      <td>241.0</td>      <td>343.0</td>      <td>44417.0</td>      <td>NaN</td>      <td>44417.0</td>      <td>26.0</td>      <td>56274.0</td>      <td>27114.0</td>      <td>2191.0</td>      <td>29305.0</td>      <td>34710.0</td>      <td>34710.0</td>      <td>11561.0</td>      <td>750.0</td>      <td>17716.0</td>      <td>7276.0</td>      <td>3586.0</td>      <td>11561.0</td>    </tr>    <tr>      <th>2016-09-30</th>      <td>45687.0</td>      <td>10505.0</td>      <td>9634.0</td>      <td>20139.0</td>      <td>527.0</td>      <td>217.0</td>      <td>2117.0</td>      <td>2456.0</td>      <td>405.0</td>      <td>66231.0</td>      <td>12734.0</td>      <td>297.0</td>      <td>NaN</td>      <td>30634.0</td>      <td>1388.0</td>      <td>32022.0</td>      <td>924.0</td>      <td>45977.0</td>      <td>22454.0</td>      <td>397.0</td>      <td>22057.0</td>      <td>30797.0</td>      <td>30797.0</td>      <td>12150.0</td>      <td>NaN</td>      <td>20890.0</td>      <td>636.0</td>      <td>4210.0</td>      <td>12150.0</td>    </tr>    <tr>      <th>2017-09-30</th>      <td>48351.0</td>      <td>10157.0</td>      <td>10640.0</td>      <td>20797.0</td>      <td>2093.0</td>      <td>2723.0</td>      <td>8966.0</td>      <td>9073.0</td>      <td>4923.0</td>      <td>64225.0</td>      <td>12451.0</td>      <td>NaN</td>      <td>329.0</td>      <td>33147.0</td>      <td>395.0</td>      <td>33542.0</td>      <td>124.0</td>      <td>46446.0</td>      <td>25162.0</td>      <td>3852.0</td>      <td>29014.0</td>      <td>32345.0</td>      <td>32345.0</td>      <td>12769.0</td>      <td>1874.0</td>      <td>17974.0</td>      <td>195.0</td>      <td>4840.0</td>      <td>12769.0</td>    </tr>    <tr>      <th>2018-09-30</th>      <td>59531.0</td>      <td>10903.0</td>      <td>27694.0</td>      <td>16791.0</td>      <td>5322.0</td>      <td>828.0</td>      <td>9175.0</td>      <td>30013.0</td>      <td>34694.0</td>      <td>77434.0</td>      <td>13313.0</td>      <td>NaN</td>      <td>721.0</td>      <td>32363.0</td>      <td>1518.0</td>      <td>30845.0</td>      <td>745.0</td>      <td>16066.0</td>      <td>469.0</td>      <td>37.0</td>      <td>432.0</td>      <td>72069.0</td>      <td>72069.0</td>      <td>13712.0</td>      <td>2527.0</td>      <td>87876.0</td>      <td>5624.0</td>      <td>5340.0</td>      <td>13712.0</td>    </tr>    <tr>      <th>2019-09-30</th>      <td>55256.0</td>      <td>12547.0</td>      <td>5076.0</td>      <td>17623.0</td>      <td>245.0</td>      <td>289.0</td>      <td>1923.0</td>      <td>1521.0</td>      <td>3488.0</td>      <td>69391.0</td>      <td>10495.0</td>      <td>NaN</td>      <td>624.0</td>      <td>57460.0</td>      <td>633.0</td>      <td>58093.0</td>      <td>1078.0</td>      <td>45896.0</td>      <td>1842.0</td>      <td>5977.0</td>      <td>7819.0</td>      <td>66116.0</td>      <td>66116.0</td>      <td>14119.0</td>      <td>2922.0</td>      <td>90976.0</td>      <td>24311.0</td>      <td>6068.0</td>      <td>14119.0</td>    </tr>  </tbody></table>



</details>

<details>
<summary><i> Yahoo Example </i></summary>

```python
fd = Fundamentals('AAPL', source = 'yahoo') # no frequency choice for Yahoo...
fd.cashflow_statement()
```

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>operating_cash_flow</th>      <th>investing_cash_flow</th>      <th>financing_cash_flow</th>      <th>end_cash_position</th>      <th>income_tax_paid_supplemental_data</th>      <th>interest_paid_supplemental_data</th>      <th>capital_expenditure</th>      <th>issuance_of_capital_stock</th>      <th>issuance_of_debt</th>      <th>repayment_of_debt</th>      <th>repurchase_of_capital_stock</th>      <th>free_cash_flow</th>      <th>ticker</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2019-09-30</th>      <td>69391000</td>      <td>45896000</td>      <td>-90976000</td>      <td>50224000</td>      <td>15263000</td>      <td>3423000</td>      <td>-10495000</td>      <td>781000</td>      <td>6963000</td>      <td>-8805000</td>      <td>-66897000</td>      <td>58896000</td>      <td>AAPL</td>    </tr>    <tr>      <th>2018-09-30</th>      <td>77434000</td>      <td>16066000</td>      <td>-87876000</td>      <td>25913000</td>      <td>10417000</td>      <td>3022000</td>      <td>-13313000</td>      <td>669000</td>      <td>6969000</td>      <td>-6500000</td>      <td>-72738000</td>      <td>64121000</td>      <td>AAPL</td>    </tr>    <tr>      <th>2017-09-30</th>      <td>63598000</td>      <td>-46446000</td>      <td>-17347000</td>      <td>20289000</td>      <td>11591000</td>      <td>2092000</td>      <td>-12795000</td>      <td>555000</td>      <td>28662000</td>      <td>-3500000</td>      <td>-32900000</td>      <td>50803000</td>      <td>AAPL</td>    </tr>  </tbody></table>





</details>

<details>
<summary><i> Marketwatch Example </i></summary>

```python
fd = Fundamentals('AAPL', source = 'marketwatch', freq = 'Q')
fd.cashflow_statement()
```

<center><small><small>

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>net_income_before_extraordinaries</th>      <th>net_income_growth</th>      <th>depreciation_depletion_and_amortization</th>      <th>depreciation_and_depletion</th>      <th>amortization_of_intangible_assets</th>      <th>deferred_taxes_and_investment_tax_credit</th>      <th>deferred_taxes</th>      <th>investment_tax_credit</th>      <th>other_funds</th>      <th>funds_from_operations</th>      <th>extraordinaries</th>      <th>changes_in_working_capital</th>      <th>receivables</th>      <th>accounts_payable</th>      <th>other_assets_liabilities</th>      <th>net_operating_cash_flow</th>      <th>net_operating_cash_flow_growth</th>      <th>net_operating_cash_flow___sales</th>      <th>capital_expenditures</th>      <th>capital_expenditures_(fixed_assets)</th>      <th>capital_expenditures_(other_assets)</th>      <th>capital_expenditures_growth</th>      <th>capital_expenditures___sales</th>      <th>net_assets_from_acquisitions</th>      <th>sale_of_fixed_assets_and_businesses</th>      <th>purchase_sale_of_investments</th>      <th>purchase_of_investments</th>      <th>sale_maturity_of_investments</th>      <th>other_uses</th>      <th>other_sources</th>      <th>net_investing_cash_flow</th>      <th>net_investing_cash_flow_growth</th>      <th>net_investing_cash_flow___sales</th>      <th>cash_dividends_paid_-_total</th>      <th>common_dividends</th>      <th>preferred_dividends</th>      <th>change_in_capital_stock</th>      <th>repurchase_of_common_and_preferred_stk</th>      <th>sale_of_common_and_preferred_stock</th>      <th>proceeds_from_stock_options</th>      <th>other_proceeds_from_sale_of_stock</th>      <th>issuance_reduction_of_debt_net</th>      <th>change_in_current_debt</th>      <th>change_in_long-term_debt</th>      <th>issuance_of_long-term_debt</th>      <th>reduction_in_long-term_debt</th>      <th>other_funds1</th>      <th>other_uses1</th>      <th>other_sources1</th>      <th>net_financing_cash_flow</th>      <th>net_financing_cash_flow_growth</th>      <th>net_financing_cash_flow___sales</th>      <th>exchange_rate_effect</th>      <th>miscellaneous_funds</th>      <th>net_change_in_cash</th>      <th>free_cash_flow</th>      <th>free_cash_flow_growth</th>      <th>free_cash_flow_yield</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2019-06-30</th>      <td>1.004e+10</td>      <td>nan</td>      <td>2.93e+09</td>      <td>2.93e+09</td>      <td>nan</td>      <td>nan</td>      <td>8.6e+07</td>      <td>nan</td>      <td>1.37e+09</td>      <td>1.443e+10</td>      <td>nan</td>      <td>-2.8e+09</td>      <td>-214M</td>      <td>220M</td>      <td>-4.31e+09</td>      <td>1.164e+10</td>      <td>nan</td>      <td>0.2165</td>      <td>-2e+09</td>      <td>-2e+09</td>      <td>nan</td>      <td>nan</td>      <td>-0.0372</td>      <td>-3.2e+08</td>      <td>nan</td>      <td>3.012e+10</td>      <td>-8.19e+09</td>      <td>3.831e+10</td>      <td>-2.68e+08</td>      <td>-3e+07</td>      <td>2.75e+10</td>      <td>nan</td>      <td>0.5118</td>      <td>-3.63e+09</td>      <td>-3.63e+09</td>      <td>nan</td>      <td>-1.695e+10</td>      <td>-1.696e+10</td>      <td>1e+06</td>      <td>1e+06</td>      <td>nan</td>      <td>-5.03e+09</td>      <td>-2.03e+09</td>      <td>-3e+09</td>      <td>nan</td>      <td>-3e+09</td>      <td>-1.2e+09</td>      <td>-1.2e+09</td>      <td>nan</td>      <td>-2.68e+10</td>      <td>nan</td>      <td>-0.4988</td>      <td>nan</td>      <td>nan</td>      <td>1.233e+10</td>      <td>9.64e+09</td>      <td>nan</td>      <td>nan</td>    </tr>    <tr>      <th>2019-09-30</th>      <td>1.369e+10</td>      <td>0.3626</td>      <td>3.18e+09</td>      <td>3.18e+09</td>      <td>nan</td>      <td>nan</td>      <td>-3.02e+08</td>      <td>nan</td>      <td>1.19e+09</td>      <td>1.775e+10</td>      <td>nan</td>      <td>2.16e+09</td>      <td>-1.932e+10</td>      <td>1.788e+10</td>      <td>4.38e+09</td>      <td>1.991e+10</td>      <td>0.7111</td>      <td>0.3114</td>      <td>-2.78e+09</td>      <td>-2.78e+09</td>      <td>nan</td>      <td>-0.3885</td>      <td>-0.0434</td>      <td>-1.3e+07</td>      <td>nan</td>      <td>2.8e+09</td>      <td>-1.81e+10</td>      <td>2.09e+10</td>      <td>-8.1e+08</td>      <td>nan</td>      <td>-798M</td>      <td>-1.029</td>      <td>-0.0125</td>      <td>-3.48e+09</td>      <td>-3.48e+09</td>      <td>nan</td>      <td>-1.705e+10</td>      <td>-1.744e+10</td>      <td>3.9e+08</td>      <td>3.9e+08</td>      <td>nan</td>      <td>-293M</td>      <td>-3.95e+09</td>      <td>3.66e+09</td>      <td>6.96e+09</td>      <td>-3.31e+09</td>      <td>-213M</td>      <td>-213M</td>      <td>nan</td>      <td>-2.104e+10</td>      <td>0.2151</td>      <td>-0.3291</td>      <td>nan</td>      <td>nan</td>      <td>-1.93e+09</td>      <td>1.713e+10</td>      <td>0.778</td>      <td>nan</td>    </tr>    <tr>      <th>2019-12-31</th>      <td>2.224e+10</td>      <td>0.6247</td>      <td>2.82e+09</td>      <td>2.82e+09</td>      <td>nan</td>      <td>nan</td>      <td>-3.49e+08</td>      <td>nan</td>      <td>1.57e+09</td>      <td>2.627e+10</td>      <td>nan</td>      <td>4.25e+09</td>      <td>5.92e+09</td>      <td>-1.09e+09</td>      <td>-555M</td>      <td>3.052e+10</td>      <td>0.5327</td>      <td>0.3327</td>      <td>-2.11e+09</td>      <td>-2.11e+09</td>      <td>nan</td>      <td>0.2413</td>      <td>-0.023</td>      <td>-9.58e+08</td>      <td>nan</td>      <td>-1.047e+10</td>      <td>-3.749e+10</td>      <td>2.702e+10</td>      <td>-1.3e+08</td>      <td>nan</td>      <td>-1.367e+10</td>      <td>-16.1278</td>      <td>-0.149</td>      <td>-3.54e+09</td>      <td>-3.54e+09</td>      <td>nan</td>      <td>-2.07e+10</td>      <td>-2.071e+10</td>      <td>2e+06</td>      <td>2e+06</td>      <td>nan</td>      <td>231M</td>      <td>-979M</td>      <td>1.21e+09</td>      <td>2.21e+09</td>      <td>-1e+09</td>      <td>-1.4e+09</td>      <td>-1.4e+09</td>      <td>nan</td>      <td>-2.541e+10</td>      <td>-0.2076</td>      <td>-0.277</td>      <td>nan</td>      <td>nan</td>      <td>-8.56e+09</td>      <td>2.841e+10</td>      <td>0.6581</td>      <td>nan</td>    </tr>    <tr>      <th>2020-03-31</th>      <td>1.125e+10</td>      <td>-0.4941</td>      <td>2.79e+09</td>      <td>2.79e+09</td>      <td>nan</td>      <td>nan</td>      <td>-3.02e+08</td>      <td>nan</td>      <td>1.58e+09</td>      <td>1.531e+10</td>      <td>nan</td>      <td>-2e+09</td>      <td>9.29e+09</td>      <td>-1.243e+10</td>      <td>412M</td>      <td>1.331e+10</td>      <td>-0.5638</td>      <td>0.2281</td>      <td>-1.85e+09</td>      <td>-1.85e+09</td>      <td>nan</td>      <td>0.1206</td>      <td>-0.0318</td>      <td>-1.76e+08</td>      <td>nan</td>      <td>1.134e+10</td>      <td>-2.914e+10</td>      <td>4.048e+10</td>      <td>-2.96e+08</td>      <td>nan</td>      <td>9.01e+09</td>      <td>1.6594</td>      <td>0.1545</td>      <td>-3.38e+09</td>      <td>-3.38e+09</td>      <td>nan</td>      <td>-1.815e+10</td>      <td>-1.857e+10</td>      <td>4.28e+08</td>      <td>4.28e+08</td>      <td>nan</td>      <td>803M</td>      <td>5.05e+09</td>      <td>-4.25e+09</td>      <td>nan</td>      <td>-4.25e+09</td>      <td>-222M</td>      <td>-222M</td>      <td>nan</td>      <td>-2.094e+10</td>      <td>0.1758</td>      <td>-0.3589</td>      <td>nan</td>      <td>nan</td>      <td>1.38e+09</td>      <td>1.146e+10</td>      <td>-0.5967</td>      <td>nan</td>    </tr>    <tr>      <th>2020-06-30</th>      <td>1.125e+10</td>      <td>0.0004</td>      <td>2.75e+09</td>      <td>2.75e+09</td>      <td>nan</td>      <td>nan</td>      <td>8.33e+08</td>      <td>nan</td>      <td>1.86e+09</td>      <td>1.67e+10</td>      <td>nan</td>      <td>-430M</td>      <td>-1.37e+09</td>      <td>2.73e+09</td>      <td>-1.1e+09</td>      <td>1.627e+10</td>      <td>0.2224</td>      <td>0.2739</td>      <td>-1.57e+09</td>      <td>-1.57e+09</td>      <td>nan</td>      <td>0.1554</td>      <td>-0.0263</td>      <td>-3.39e+08</td>      <td>nan</td>      <td>-3e+09</td>      <td>-3.018e+10</td>      <td>2.718e+10</td>      <td>-2.63e+08</td>      <td>nan</td>      <td>-5.17e+09</td>      <td>-1.5731</td>      <td>-0.0869</td>      <td>-3.66e+09</td>      <td>-3.66e+09</td>      <td>nan</td>      <td>-1.589e+10</td>      <td>-1.589e+10</td>      <td>nan</td>      <td>nan</td>      <td>nan</td>      <td>2.17e+09</td>      <td>1.12e+09</td>      <td>1.05e+09</td>      <td>8.43e+09</td>      <td>-7.38e+09</td>      <td>-1.74e+09</td>      <td>-1.74e+09</td>      <td>nan</td>      <td>-1.912e+10</td>      <td>0.0871</td>      <td>-0.3217</td>      <td>nan</td>      <td>nan</td>      <td>-8.01e+09</td>      <td>1.471e+10</td>      <td>0.2835</td>      <td>0.044</td>    </tr>  </tbody></table>



</small></small></center>

</details>




_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _




<br>



###	 <div id="A41"> <li>Financial ratios and key metrics <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>


#### <div id="f102"><i>Fundamentals(ticker, source, freq).ratios()</i></div>

<ul>
<li>Returns a dataframe with annual or quarterly financial ratios up to 2005 from Macrotrends.com.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Macrotrends.com </li>
	<li> <code>freq</code>: 'A' (annual data), 'Q' (quarterly data), default: 'A' </li>
	</ul>
</ul>
</ul>


<br>


<details>
<summary><i> Example </i></summary>


```python
fd = Fundamentals('AAPL', freq = 'A')
fd.ratios()
```

<center><small><small>


<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>current_ratio</th>      <th>longterm_debt_to_capital</th>      <th>debt_to_equity_ratio</th>      <th>gross_margin</th>      <th>operating_margin</th>      <th>ebit_margin</th>      <th>ebitda_margin</th>      <th>pretax_profit_margin</th>      <th>net_profit_margin</th>      <th>asset_turnover</th>      <th>inventory_turnover_ratio</th>      <th>receiveable_turnover</th>      <th>days_sales_in_receivables</th>      <th>roe__return_on_equity</th>      <th>return_on_tangible_equity</th>      <th>roa__return_on_assets</th>      <th>roi__return_on_investment</th>      <th>book_value_per_share</th>      <th>operating_cash_flow_per_share</th>      <th>free_cash_flow_per_share</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2005-09-30</th>      <td>2.9538</td>      <td>NaN</td>      <td>NaN</td>      <td>29.0144</td>      <td>11.7938</td>      <td>11.7938</td>      <td>13.0787</td>      <td>12.9783</td>      <td>9.5327</td>      <td>1.2097</td>      <td>59.9333</td>      <td>15.5654</td>      <td>23.4495</td>      <td>17.8783</td>      <td>18.1124</td>      <td>11.5318</td>      <td>17.8783</td>      <td>0.3177</td>      <td>0.1057</td>      <td>0.0948</td>    </tr>    <tr>      <th>2006-09-30</th>      <td>2.2519</td>      <td>NaN</td>      <td>NaN</td>      <td>28.9827</td>      <td>12.7000</td>      <td>12.7000</td>      <td>13.8649</td>      <td>14.5897</td>      <td>10.2977</td>      <td>1.1226</td>      <td>50.8037</td>      <td>15.4273</td>      <td>23.6593</td>      <td>19.9219</td>      <td>20.2814</td>      <td>11.5606</td>      <td>19.9219</td>      <td>0.4169</td>      <td>0.0153</td>      <td>0.0312</td>    </tr>    <tr>      <th>2007-09-30</th>      <td>2.3659</td>      <td>NaN</td>      <td>NaN</td>      <td>33.1679</td>      <td>17.9307</td>      <td>17.9307</td>      <td>19.2611</td>      <td>20.3678</td>      <td>14.2200</td>      <td>0.9697</td>      <td>47.4740</td>      <td>15.0141</td>      <td>24.3106</td>      <td>24.0504</td>      <td>24.6214</td>      <td>13.7886</td>      <td>24.0504</td>      <td>0.5950</td>      <td>0.1293</td>      <td>0.1266</td>    </tr>    <tr>      <th>2008-09-30</th>      <td>2.6411</td>      <td>NaN</td>      <td>NaN</td>      <td>35.2005</td>      <td>22.2107</td>      <td>22.2107</td>      <td>23.5337</td>      <td>23.8644</td>      <td>16.3213</td>      <td>1.0365</td>      <td>47.7289</td>      <td>15.4794</td>      <td>23.5798</td>      <td>27.4432</td>      <td>28.0624</td>      <td>16.9169</td>      <td>27.4432</td>      <td>0.8964</td>      <td>0.1602</td>      <td>0.1465</td>    </tr>    <tr>      <th>2009-09-30</th>      <td>2.7425</td>      <td>NaN</td>      <td>NaN</td>      <td>40.1399</td>      <td>27.3628</td>      <td>27.3628</td>      <td>29.0735</td>      <td>28.1226</td>      <td>19.1936</td>      <td>0.9032</td>      <td>56.4462</td>      <td>8.4843</td>      <td>43.0207</td>      <td>26.0272</td>      <td>26.4052</td>      <td>17.3365</td>      <td>26.0272</td>      <td>1.2558</td>      <td>0.0201</td>      <td>0.0183</td>    </tr>  </tbody></table>



</small></small></center>

</details>

<div align="right"> <a href="#i102">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id="f2"><i>Fundamentals(ticker, source, freq).key\_metrics()</i></div>

<ul>
<li>Returns a dataframe with current key statistics and financial ratios from either Yahoo Finance or Finviz. Default key metrics for the 'macrotrends' and 'marketwatch' source is from Finviz.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: 'yahoo', 'marketwatch', 'macrotrends', default: 'macrotrends' </li>
	<li> <code>freq</code>: choice has no effect, most recent data is returned </li>
	</ul>
</ul>
</ul>

<br>



<details>
<summary><i> Default Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.key_metrics()
```

<center><small><small>

|    | index       |   market_cap |    income |      sales |   book\_to\_sh | .. |
|---:|:------------|-------------:|----------:|-----------:|-------------:| ---: |
|  0 | DJIA S&P500 |  1.94097e+12 | 5.842e+10 | 2.7386e+11 |         4.19 | ... |


</small></small></center>

</details>


<details>
<summary><i> Yahoo Example </i></summary>

```python
fd = Fundamentals('AAPL', source = 'yahoo')
fd.key_metrics()
```

<center><small><small>

|    |   payout\_ratio |   profit\_margin |   operating\_margin\_(ttm) |   return\_on\_assets\_(ttm) |   return\_on\_equity\_(ttm) |   ...|
|---:|---------------:|----------------:|-------------------------:|-------------------------:|-------------------------:|----------------:|
|  0 |         0.2373 |          0.2133 |                   0.2452 |                   0.1312 |                   0.6925 |      ... |

</small></small></center>

</details>


<div align="right"> <a href="#i2">To index</a> </div>

<br>




###	 <div id="A43"> <li>Earnings and revenue estimates<hr style="border:0.5px solid gray"> </hr> </li> </div>


<div align="right"><a href="#0">Back to top</a> </div>

#### <div id = "f11" ><i>Fundamentals( ticker, source, freq ).earnings\_estimates()</i></div>

<ul>
<li>Returns current earnings estimates for the current quarter, next quarter, current year and the next year from Yahoo Finance.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</ul>
</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.earnings_estimates('AAPL')
```

<center><small><small>

|    | date                    |   no\_of\_analysts |   avg\_estimate |   low\_estimate |   high\_estimate |   year\_ago\_eps |
|---:|:------------------------|------------------:|----------------:|---------------:|----------------:|---------------:|
|  1 | Current Qtr. (Sep 2020) |                28 |            2.8  |           2.18 |            3.19 |           3.03 |
|  2 | Next Qtr. (Dec 2020)    |                24 |            5.45 |           4.76 |            6.82 |           4.99 |
|  3 | Current Year (2020)     |                35 |           12.97 |          12.36 |           13.52 |          11.89 |
|  4 | Next Year (2021)        |                35 |           15.52 |          12.67 |           18    |          12.97 |

</small></small></center>

</details>

<div align="right"> <a href="#i11">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f12" ><i> Fundamentals( ticker, source, freq ).earnings\_estimate\_trends()</i></div>

<ul>
<li>Returns earnings estimates for the current quarter, next quarter, current year and the next year for the current date, 7 days ago, 30 days ago, 60 days ago and 90 days ago from Yahoo Finance.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</ul>
</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.earnings_estimate_trends()
```

<center><small><small>

|    | date                    |   current\_estimate |   7\_days\_ago |   30\_days\_ago |   60\_days\_ago |   90\_days\_ago |
|---:|:------------------------|-------------------:|-------------:|--------------:|--------------:|--------------:|
|  1 | Current Qtr. (Sep 2020) |               2.8  |         2.84 |          2.79 |          2.82 |          2.8  |
|  2 | Next Qtr. (Dec 2020)    |               5.45 |         5.44 |          5.22 |          5.21 |          5.22 |
|  3 | Current Year (2020)     |              12.97 |        13    |         12.41 |         12.39 |         12.32 |
|  4 | Next Year (2021)        |              15.52 |        15.54 |         14.94 |         14.86 |         14.73 |

</small></small></center>

</details>

<div align="right"> <a href="#i12">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f13" ><i> Fundamentals( ticker, source, freq ).earnings\_history()</i></div>

<ul>
<li>Returns earnings estimates and actual earnings for the past 4 quarters from Yahoo Finance.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</ul>
</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.earnings_history()
```

<center><small><small>

|    | date       |   eps\_est |   eps\_actual |   difference |   surprise\_% |
|---:|:-----------|-----------:|-------------:|-------------:|-------------:|
|  1 | 9/29/2019  |       2.84 |         3.03 |         0.19 |        0.067 |
|  2 | 12/30/2019 |       4.55 |         4.99 |         0.44 |        0.097 |
|  3 | 3/30/2020  |       2.26 |         2.55 |         0.29 |        0.128 |
|  4 | 6/29/2020  |       2.04 |         2.58 |         0.54 |        0.265 |

</small></small></center>

</details>

<div align="right"> <a href="#i13">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f14" ><i> Fundamentals(ticker, source, freq).revenue\_estimates()</i></div>

<ul>
<li>Returns revenue estimates for the current quarter, next quarter, current year and the next year from Yahoo Finance.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</ul>
</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.revenue_estimates()
```

<center><small><small>

|    | date                    |   no\_of\_analysts |   avg\_estimate |   low\_estimate |   high\_estimate |   year\_ago\_sales |   sales\_growth\_(yearest) |
|---:|:------------------------|------------------:|----------------:|---------------:|----------------:|-----------------:|-------------------------:|
|  1 | Current Qtr. (Sep 2020) |                26 |      6.351e+10  |     5.255e+10  |      6.85e+10   |       6.404e+10  |                   -0.008 |
|  2 | Next Qtr. (Dec 2020)    |                24 |      1.0036e+11 |     8.992e+10  |      1.157e+11  |       8.85e+10   |                    0.134 |
|  3 | Current Year (2020)     |                33 |      2.7338e+11 |     2.6236e+11 |      2.8089e+11 |       2.6017e+11 |                    0.051 |
|  4 | Next Year (2021)        |                33 |      3.0734e+11 |     2.7268e+11 |      3.3153e+11 |       2.7338e+11 |                    0.124 |

</small></small></center>

</details>

<div align="right"> <a href="#i14">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f15" ><i> Fundamentals( ticker, source, freq ).growth\_estimates()</i></div>

<ul>
<li>Returns earnings estimates and actual earnings for the past 4 quarters from Yahoo Finance.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</ul>
</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.growth_estimates()
```

<i> Output </i>

<center><small><small>

|                          |    aapl |   industry |   sector(s) |   sandp_500 |
|:-------------------------|--------:|-----------:|------------:|------------:|
| Current\_Qtr.             | -0.079  |        nan |         nan |         nan |
| Next\_Qtr.                |  0.088  |        nan |         nan |         nan |
| Current_Year             |  0.088  |        nan |         nan |         nan |
| Next_Year                |  0.195  |        nan |         nan |         nan |
| Next\_5\_Years\_(per\_annum) |  0.1246 |        nan |         nan |         nan |
| Past\_5\_Years\_(per\_annum) |  0.0842 |        nan |         nan |         nan |


</small></small></center>

</details>

<div align="right"> <a href="#i15">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

###	 <div id="A48"> <li>Earnings Call Transcripts<hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>

The earnings call transcripts are collected from <a href="https://www.fool.com/">The Motley Fool</a> and are available until Q1 2018. The data returns a simple breakdown of the sections of the earnings call which will still need to be processed further. The full html of the call is also available.


#### <div id = "f131" ><i> Fundamentals( ticker, source, freq ).transcripts(html = True)</i></div>

<ul>
<li>Returns recent history (up to Q1 2018) of earnings call transcripts.</li>
<ul>
<li> <i>Function Arguments: </i> </li>
<ul>
 <li>
 <code>html = True</code> returns additional columns with html of transcript from Motley Fool.
 </li>
</ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is the Motley Fool </li>
	<li> <code>freq</code>:  choice has no effect </li>
	</ul>
</li>
</ul>
</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.transcripts(html = True)
```

<center><small><small>

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>prepared_remarks</th>      <th>questions_and_answers</th>      <th>call_participants</th>      <th>ticker</th>      <th>html</th>      <th>date</th>     <th>time</th>      <th>quarter</th>      <th>link</th>    </tr>  </thead>  <tbody>    <tr>      <th>2020-07-31</th>      <td>Operator  Good day, everyone. Welcome to the Apple Inc. third-quarter fiscal year 2020 earnings con ...</td>    <td>Operator  [Operator instructions]  Luca Maestri -- Chief Financial Officer  Operator, may we plea ...</td>      <td>Tejas Gala -- Senior Manager, Corporate Finance, and Investor Relations  Tim Cook -- Chief Executiv ...</td>    <td>AAPL</td>     <td>&lt;h2&gt;Prepared Remarks:&lt;/h2&gt; &lt;p&gt;&lt;strong&gt;Operator&lt;/strong&gt;&lt;/p&gt; &lt;p&gt;Good day, everyone. Welcome to the Ap ...</td>      <td>2020/07/31</td>      <td>5:00 p.m. ET</td>      <td>Q3 2020</td>      <td>https://www.fool.com/earnings/call-transcripts/2020/07/31/apple-aapl-q3-2020-earnings-call-transcrip ...</td>    </tr>   <tr>     <th>2020-04-30</th>      <td>Operator  Good day, everyone. Welcome to the Apple Inc. Second Quarter Fiscal Year 2020 Earnings Co ...</td>      <td>Operator  Yes. That will come from Shannon Cross, Cross Research.  Shannon Cross -- Cross Research ...</td>     <td>Tejas Gala -- Senior Manager, Corporate Finance and Investor Relations  Tim Cook -- Chief Executive ...</td>      <td>AAPL</td>     <td>&lt;h2&gt;Prepared Remarks:&lt;/h2&gt; &lt;p&gt;&lt;strong&gt;Operator&lt;/strong&gt;&lt;/p&gt; &lt;p&gt;Good day, everyone. Welcome to the Ap ...</td>     <td>2020/04/30</td>      <td>5:00 p.m. ET</td>      <td>Q2 2020</td>      <td>https://www.fool.com/earnings/call-transcripts/2020/04/30/apple-inc-aapl-q2-2020-earnings-call-trans ...</td>    </tr>    <tr>      <th>2020-01-28</th>      <td>Operator  Good day everyone. Welcome to the Apple Incorporated First Quarter Fiscal Year 2020 Earni ...</td>      <td>Operator  Yes. That will be from Amit Daryanani with Evercore.  Amit Daryanani -- Evercore ISI --  ...</td>      <td>Tejas Gala -- Senior Analyst, Corporate Finance and Investor Relations  Tim Cook -- Chief Executive ...</td>      <td>AAPL</td>      <td>&lt;h2&gt;Prepared Remarks:&lt;/h2&gt; &lt;p&gt;&lt;strong&gt;Operator&lt;/strong&gt;&lt;/p&gt; &lt;p&gt;Good day everyone. Welcome to the App ...</td>      <td>2020/01/28</td>      <td>5:00 p.m. ET</td>      <td>Q1 2020</td>      <td>https://www.fool.com/earnings/call-transcripts/2020/01/28/apple-inc-aapl-q1-2020-earnings-call-trans ...</td>    </tr>  
<tr>      <th>...</th>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>    </tr>
</tbody></table>

</center></small></small>


</details>

<div align="right"> <a href="#i131">To index</a> </div>


-----

<br>

###	 <div id="A44"> <li>Insider transactions and analyst ratings <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>


#### <div id = "f16" ><i> Fundamentals( ticker, source, freq ).insider\_transactions()</i></div>

<ul>
<li>Returns company insider transactions for the past year from Finviz.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Finviz </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</li>
</ul>
</ul>


<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.insider_transactions()
```

<center><small><small>

|    | insider_trading   | relationship                 | date   | transaction     |   cost |   #shares |   value\_($) |   #shares\_total | sec\_form\_4      |
|---:|:------------------|:-----------------------------|:-------|:----------------|-------:|----------:|------------:|----------------:|:----------------|
|  0 | COOK TIMOTHY D    | Chief Executive Officer      | Aug 25 | Sale            | 496.91 |    265160 |   131761779 |          837374 | Aug 25 06:45 PM |
|  1 | KONDO CHRIS       | Principal Accounting Officer | May 08 | Sale            | 305.62 |      4491 |     1372539 |            7370 | May 12 06:30 PM |
|  2 | JUNG ANDREA       | Director                     | Apr 28 | Option Exercise |  48.95 |      9590 |      469389 |           33548 | Apr 30 09:30 PM |
|  3 | O'BRIEN DEIRDRE   | Senior Vice President        | Apr 16 | Sale            | 285.12 |      9137 |     2605141 |           33972 | Apr 17 06:31 PM |
|  4 | Maestri Luca      | Senior Vice President, CFO   | Apr 07 | Sale            | 264.44 |     41062 |    10858445 |           27568 | Apr 09 06:30 PM |
|  ... |...     | ...  | ...| ...            | ... |     ... |    ... |           ... | ... |

</small></small></center>

</details>

<div align="right"> <a href="#i16">To index</a> </div>

-----

#### <div id = "f17" ><i> Fundamentals( ticker, source, freq ).analyst\_ratings()</i></div>

<ul>
<li>Returns recent history of analyst ratings from Finviz.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Finviz </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</li>
</ul>

</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.analyst_ratings()
```

<i> Output </i>

<center><small><small>

| date                | action     | rating_institution     | rating     | price_target   |
|:--------------------|:-----------|:-----------------------|:-----------|:---------------|
| 2020-09-01 00:00:00 | Reiterated | JP Morgan              | Overweight | $115 → $150    |
| 2020-09-01 00:00:00 | Reiterated | Cowen                  | Outperform | $530 → $133    |
| 2020-08-31 00:00:00 | Reiterated | Monness Crespi & Hardt | Buy        | $117.50 → $144 |
| 2020-08-26 00:00:00 | Reiterated | Wedbush                | Outperform | $515 → $600    |
| 2020-08-25 00:00:00 | Reiterated | Cowen                  | Outperform | $470 → $530    |
| ...| ... | ...                  | ... | ...    |


</small></small></center>

</details>

<div align="right"> <a href="#i17">To index</a> </div>

-----


<br>

###	 <div id="A46"> <li> ESG scores<hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>



#### <div id = "f18" ><i>Fundamentals( ticker, source, freq ).esg\_score()</i></div>

<ul>
<li>Returns current ESG scores from Sustainalytics published on Yahoo Finance.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</li>
</ul>

</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.esg_score()
```

<center><small><small>

|    | date       |   total\_esg\_risk_score | risk\_category   | risk\_percentile   |   environment\_risk_score |   social\_risk\_score |   ... |
|---:|:-----------|-----------------------:|:----------------|:------------------|-------------------------:|--------------------:|------------------------:|
|  0 | 2020-08-25 |                     24 | Medium          | 33rd              |                      0.5 |                  13 |                    ... |

</small></small></center>

</details>


<div align="right"> <a href="#i18">To index</a> </div>

----

#### <div id = "f19" ><i>Fundamentals( ticker, source, freq ).corporate\_governance\_score()</i></div>

<ul>
<li>Returns current corporate governance scores from Institutional Shareholder Services (ISS) published on Yahoo Finance.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect, most recent data is returned </li>
	</ul>
</li>
</ul>

</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.corporate_governance_score()
```

<i> Output </i>

<center><small><small>

|    |   audit |   board |   shareholder\_rights |   compensation |   quality\_score | ticker   | date       |
|---:|--------:|--------:|---------------------:|---------------:|----------------:|:---------|:-----------|
|  0 |       1 |       1 |                    1 |              3 |               1 | AAPL     | 2020-08-25 |

</small></small></center>

</details>

<div align="right"> <a href="#i19">To index</a> </div>

----

<br>


###	 <div id="A47"> <li>Company info<hr style="border:0.5px solid gray"> </hr> </li> </div>


<div align="right"><a href="#0">Back to top</a> </div>


#### <div id = "f20" ><i>Fundamentals( ticker, source, freq ).profile()</i></div>

<ul>
<li>Returns company sector, industry, current number of employees and a company description.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect </li>
	</ul>
</li>
</ul>
</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.profile()
```

<center><small><small>

|    | company\_name   | sector     | industry             |   number\_of\_employees | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ticker   |
|---:|:---------------|:-----------|:---------------------|----------------------:|:----------|:---------|
|  0 | Apple Inc.     | Technology | Consumer Electronics |                137000 | Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide...  | AAPL     |

</small></small></center>

</details>

<div align="right"> <a href="#i20">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f21" ><i>Fundamentals( ticker, source, freq ).executives_info()</i></div>

<ul>
<li>Returns current company executives with name, title, salary, age and their gender.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: choice has no effect, data is from Yahoo Finance </li>
	<li> <code>freq</code>:  choice has no effect </li>
	</ul>
</li>
</ul>

</ul>

<br>

<details>
<summary><i> Example </i></summary>

```python
fd = Fundamentals('AAPL')
fd.executives_info()
```

<center><small><small>

|    | name                    | title                       |       pay |   exercised |   year\_born | gender   |   age\_at\_end\_of\_year |
|---:|:------------------------|:----------------------------|----------:|------------:|------------:|:---------|---------------------:|
|  0 | Mr. Timothy D. Cook     | CEO & Director              | 1.156e+07 |         nan |        1961 | male     |                   59 |
|  1 | Mr. Luca Maestri        | CFO & Sr. VP                | 3.58e+06  |         nan |        1964 | male     |                   56 |
|  2 | Mr. Jeffrey E. Williams | Chief Operating Officer     | 3.57e+06  |         nan |        1964 | male     |                   56 |
|  3 | Ms. Katherine L. Adams  | Sr. VP, Gen. Counsel & Sec. | 3.6e+06   |         nan |        1964 | female   |                   56 |
|  4 | Ms. Deirdre O'Brien     | Sr. VP of People & Retail   | 2.69e+06  |         nan |        1967 | female   |                   53 |

</small></small></center>

</details>

<div align = "right">  <a href="#i21">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

## <div id="A5"> Price data </div>

<div align="right"><a href="#0">Back to top</a> </div>

The functions below help to retrieve daily historical price data from <code>Yahoo Finance</code> as well as most recent option prices from Yahoo Finance or CBOE.

Furthermore, the <code>historical\_futures\_contracts</code> function enables a bulk download of historical monthly futures contracts up to the year 2000 for currencies, indices, interest rates and commodities including energy, metals and agricultural contracts. The data is downloaded from <a href = "www.mrci.com">www.mrci.com</a> but the data is not completely cleaned (yet).

```python
import finpie.price_data

# Historical price data from Yahoo Finance, most recent option prices from Yahoo Finance and CBOE, and futures prices bulk-download...
# from finpie.price_data import price_data
import finpie
```

###	 <div id="A51"> <li> Stock and ETF prices <hr style="border:0.5px solid gray"> </hr> </li> </div>


#### <div id="f22"><i>historical_prices( ticker )</i></div>

<ul>
<li>Returns dataframe with daily historical prices from Yahoo Finance.</li>

</ul>

<details>
<summary><i> Example </i></summary>

```python
historical_prices('AAPL')
```

<center><small><small>

|    | Date       |    Open |    High |     Low |   Close |   Adj Close |   Volume |
|---:|:-----------|--------:|--------:|--------:|--------:|------------:|---------:|
|  0 | 1993-01-29 | 43.9688 | 43.9688 | 43.75   | 43.9375 |     26.1841 |  1003200 |
|  1 | 1993-02-01 | 43.9688 | 44.25   | 43.9688 | 44.25   |     26.3703 |   480500 |
|  2 | 1993-02-02 | 44.2188 | 44.375  | 44.125  | 44.3438 |     26.4262 |   201300 |
|  3 | 1993-02-03 | 44.4062 | 44.8438 | 44.375  | 44.8125 |     26.7055 |   529400 |
|  4 | 1993-02-04 | 44.9688 | 45.0938 | 44.4688 | 45      |     26.8172 |   531500 |
|  ... | ... | ... | ... | ... | ...      |     ... |   ... |

</small></small></center>

</details>

<div align="right"> <a href="#i22">To index</a> </div>

--------

<br>

###	 <div id="A52"> <li> Option prices <hr style="border:0.5px solid gray"> </hr> </li> </div>
<div align="right"><a href="#0">Back to top</a> </div>


#### <div id="f27"><i>yahoo\_option_chain( ticker )</i></div>

<ul>
<li>Returns two dataframes for current put and call options from Yahoo Finance.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
calls, puts = yahoo_option_chain('AAPL')
```

<i>Call options chain</i>
<center><small><small>

|    | contract_name       | last\_trade\_date        |   strike |   last\_price |   ... |
|---:|:--------------------|:-----------------------|---------:|-------------:|------:|
|  0 | AAPL200828C00190000 | 2020-08-25 3:40PM EDT  |      190 |       310.29 |     ... |
|  1 | AAPL200828C00195000 | 2020-08-25 12:36PM EDT |      195 |       300.7  |     ... |
|  2 | AAPL200828C00200000 | 2020-08-25 12:13PM EDT |      200 |       294.8  |     ... |
|  3 | AAPL200828C00205000 | 2020-08-06 3:07PM EDT  |      205 |       249.54 |     ... |
|  ... | ... | ...  |      ... |       ... |     ... |

</small></small></center>

<i>Put options chain</i>
<center><small><small>

|    | contract_name       | last_trade_date        |   strike |   last_price |   bid |
|---:|:--------------------|:-----------------------|---------:|-------------:|------:|
|  0 | AAPL200828P00190000 | 2020-08-24 2:05PM EDT  |      190 |         0.01 |     ... |
|  1 | AAPL200828P00195000 | 2020-08-10 10:38AM EDT |      195 |         0.02 |     ... |
|  2 | AAPL200828P00200000 | 2020-08-24 1:36PM EDT  |      200 |         0.01 |     ... |
|  3 | AAPL200828P00205000 | 2020-08-24 10:08AM EDT |      205 |         0.02 |     ... |
|  ... | ... | ... |      ... |         ... |     ... |

</small></small></center>

</details>

<div align="right"> <a href="#i27">To index</a> </div>

------

#### <div id="f106"><i>cboe\_option_chain( ticker, head = False )</i></div>

<ul>
<li>Returns two dataframes for current put and call options from CBOE.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
calls, puts = cboe_option_chain('AAPL')
```


<i>Call options chain</i>
<center><small><small>

|    | expiration   | calls               |   last_sale |    net |   bid |   ask |   vol |   iv |   delta |   gamma |   open_int |   strike |   underlying |
|---:|:-------------|:--------------------|------------:|-------:|------:|------:|------:|-----:|--------:|--------:|-----------:|---------:|-------------:|
|  0 | 09/25/2020   | AAPL200925C00058750 |       46.75 | -2.375 | 50.1  | 52.65 |    15 | 0.02 |  1      |  0.0002 |          0 |    58.75 |       110.13 |
|  1 | 09/25/2020   | AAPL200925C00060000 |       49.2  |  1.325 | 48.85 | 51.4  |    33 | 0.02 |  1      |  0.0001 |         38 |    60    |       110.13 |
|  2 | 09/25/2020   | AAPL200925C00061250 |       49.3  |  0     | 47.6  | 50.2  |     0 | 0.02 |  1      |  0.0002 |          0 |    61.25 |       110.13 |
|  3 | 09/25/2020   | AAPL200925C00062500 |       43.1  | -2.3   | 47.2  | 48.05 |     2 | 0.02 |  0.9989 |  0.0002 |          6 |    62.5  |       110.13 |
|  ... | ...   | ... |       ...  | ...   | ...  | ... |     ... | ... |  ... |  ... |          ... |    ...  |       ... |

</small></small></center>

<i>Put options chain</i>
<center><small><small>

|    | expiration   | puts                |   last_sale |    net |   bid |   ask |   vol |     iv |   delta |   gamma |   open_int |   strike |   underlying |
|---:|:-------------|:--------------------|------------:|-------:|------:|------:|------:|-------:|--------:|--------:|-----------:|---------:|-------------:|
|  0 | 09/25/2020   | AAPL200925P00058750 |        0.06 |  0     |     0 |  0.01 |     0 | 2.001  | -0.001  |  0.0001 |         76 |    58.75 |       110.13 |
|  1 | 09/25/2020   | AAPL200925P00060000 |        0.01 |  0     |     0 |  0.01 |     0 | 1.876  | -0.0008 |  0.0001 |        505 |    60    |       110.13 |
|  2 | 09/25/2020   | AAPL200925P00061250 |        0.03 |  0     |     0 |  0.01 |     0 | 1.8406 | -0.0009 |  0.0001 |         17 |    61.25 |       110.13 |
|  3 | 09/25/2020   | AAPL200925P00062500 |        0.01 | -0.005 |     0 |  0.03 |    10 | 1.8178 | -0.0011 |  0.0002 |        123 |    62.5  |       110.13 |
|  ... | ...   | ... |       ...  | ...   | ...  | ... |     ... | ... |  ... |  ... |          ... |    ...  |       ... |

</small></small></center>

</details>

<div align="right"> <a href="#i106">To index</a> </div>


###	 <div id="A53"> <li> Futures prices <hr style="border:0.5px solid gray"> </hr> </li> </div>
<div align="right"><a href="#0">Back to top</a> </div>


#### <div id="f28"><i>historical\_futures\_contracts( pandas.date_range )</i></div>

<ul>
<li>
Returns daily price data for a number of monthly future contracts including open interest of each contract for the given date range.
</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
historical_futures_contracts( pd.date_range('2020-01-01', '2020-09-01') )
```


<center><small><small>

|                     | month   |   date |   open |   high |   low |   close |   change |   volume |   open_interest | change_in_oi   | future             |
|:--------------------|:--------|-------:|-------:|-------:|------:|--------:|---------:|---------:|----------------:|:---------------|:-------------------|
| 2020-01-06 | Jan20   | 200106 |  296.2 |  299.4 | 296.2 |   297.7 |      1.6 |     4103 |            2459 | -811           | Soybean Meal(CBOT) |
| 2020-01-06 | Mar20   | 200106 |  301.5 |  304.5 | 300.6 |   302.9 |      1.7 |    58930 |          222007 | 3,678          | Soybean Meal(CBOT) |
| 2020-01-06 | May20   | 200106 |  305.3 |  308.3 | 304.6 |   306.9 |      1.7 |    23500 |           92983 | 2,616          | Soybean Meal(CBOT) |
| ... | ...   | ... |  ... |  ... | ... |   ... |      ... |    ... |           ... | ...         | ... |


</small></small></center>

</details>

<div align="right"> <a href="#i28">To index</a> </div>

----


#### <div id="f29"><i>futures\_contracts( date )</i></div>

<ul>
<li>Returns daily price data for a number of monthly future contracts including open interest of each contract for the given date.
</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
futures_prices('2020-01-06')
```


<center><small><small>

|                     | month   |   date |   open |   high |   low |   close |   change |   volume |   open_interest | change_in_oi   | future             |
|:--------------------|:--------|-------:|-------:|-------:|------:|--------:|---------:|---------:|----------------:|:---------------|:-------------------|
| 2020-01-06 | Jan20   | 200106 |  296.2 |  299.4 | 296.2 |   297.7 |      1.6 |     4103 |            2459 | -811           | Soybean Meal(CBOT) |
| 2020-01-06 | Mar20   | 200106 |  301.5 |  304.5 | 300.6 |   302.9 |      1.7 |    58930 |          222007 | 3,678          | Soybean Meal(CBOT) |
| 2020-01-06 | May20   | 200106 |  305.3 |  308.3 | 304.6 |   306.9 |      1.7 |    23500 |           92983 | 2,616          | Soybean Meal(CBOT) |
| ... | ...   | ... |  ... |  ... | ... |   ... |      ... |    ... |           ... | ...         | ... |

</small></small></center>

</details>

<div align="right"> <a href="#i29">To index</a> </div>

------




<br>





## <div id="A7">News data</div>

<div align="right"><a href="#0">Back to top</a> </div>

The functions below retrieve news headlines based on keyword searches from <code>Barrons</code>, <code>CNBC</code>, the <code>Financial Times</code>, the <code>New York Times</code>, <code>Reuters</code>, <code>Seeking Alpha</code> and the <code>Wall Street Journal</code>. The keyword for Seeking Alpha is simply the relevant stock ticker.


The scrape is based on Selenium and may not be very stable if the website layouts change.

Furthermore, some of the functions can run for a long-time so it is recommended to use a reasonable <code>datestop</code> value.

Some downloads may fail occasionally as access to the website could be blocked.

```python
# Importing the NewsData class
from finpie import NewsData #
news = NewsData('XOM', 'exxon mobil')
news.head = False # default = false, ensures selenium headless mode
news.verbose = True # default = False, prints total number of collected articles
```

<br>

-----

#### <div id = "f78" ><i>NewsData(ticker, keywords).barrons()</i></div>

<ul>
<li>Returns the news headlines from Barrons.com for the specified keywords.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.barrons(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

<center><small><small>

| date       | link                                                                                                           | headline                                                                      | description                                                                                                                                                                                                   | newspaper   | author                  | date_retrieved             | ticker   |   comments |   tag | search_term   | id                                                                                                                                                                                                | source   |
|:-----------|:---------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:------------------------|:---------------------------|:---------|-----------:|------:|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| 15/09/2020 | https://www.barrons.com/articles/options-traders-are-pricing-in-an-exxon-dividend-cut-analyst-says-51600181938 | Options Traders Are Pricing In an Exxon Dividend Cut, Analyst Says            | Whether Exxon can maintain its dividend is one of the most active debates right now among energy investors. The company has a strong incentive to keep making payments at current levels.                     | Barrons.com | Avi Salzman             | 2020-09-16 13:35:26.574289 | XOM      |        nan |   nan | exxon mobil   | Barrons.comOptions Traders Are Pricing In an Exxon Dividend Cut, Analyst Sayshttps://www.barrons.com/articles/options-traders-are-pricing-in-an-exxon-dividend-cut-analyst-says-51600181938       | barrons  |
| 13/09/2020 | https://www.wsj.com/articles/exxon-used-to-be-americas-most-valuable-company-what-happened-oil-gas-11600037243 | Exxon Used to Be America’s Most Valuable Company. What Happened?              | The oil giant doubled down on oil and gas at what now looks to be the worst possible time. Investors are fleeing and workers are grumbling about the direction of a company some see as out of touch.         | WSJ.com     | Christopher M. Matthews | 2020-09-16 13:35:26.574289 | XOM      |        nan |   nan | exxon mobil   | WSJ.comExxon Used to Be America’s Most Valuable Company. What Happened?https://www.wsj.com/articles/exxon-used-to-be-americas-most-valuable-company-what-happened-oil-gas-11600037243             | barrons  |
| 11/09/2020 | https://www.barrons.com/articles/where-to-find-bargains-in-oil-stocks-51599837910                              | Where to Find Bargains in Oil Stocks Now                                      | Goldman Sachs analyst likes certain refiners and Canadian oil companies.                                                                                                                                      | Barrons.com | Avi Salzman             | 2020-09-16 13:35:26.574289 | XOM      |        nan |   nan | exxon mobil   | Barrons.comWhere to Find Bargains in Oil Stocks Nowhttps://www.barrons.com/articles/where-to-find-bargains-in-oil-stocks-51599837910                                                              | barrons  |
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|


</small></small></center>

</details>

<div align = "right">  <a href="#i78">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f80" ><i>NewsData(ticker, keywords).cnbc()</i></div>

<ul>
<li>Returns the news headlines from CNBC for the specified keywords.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.cnbc(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

<center><small><small>

| date                | link                                                                                                                              | headline                                                            | description                                                                                                                                                               | tag             | author       | date_retrieved             | ticker   |   comments | newspaper   | search_term   | id                                                                                                                                                                                                       | source   |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:-------------|:---------------------------|:---------|-----------:|:------------|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| 2020-09-10 00:00:00 | https://www.cnbc.com/video/2020/09/10/honeywell-ceo-darius-adamczyk-on-rejoining-the-dow.html?&qsearchterm=exxon mobil            | Honeywell CEO Darius Adamczyk on rejoining the Dow                  | S&P Dow Jones Indices said Monday that three new companies will be joining the 30-stock benchmark. Salesforce.com will replace Exxon Mobil, Amgen will replace Pfizer ... | Squawk Box U.S. | nan          | 2020-09-16 14:14:43.533664 | XOM      |        nan | CNBC        | exxon mobil   | CNBCHoneywell CEO Darius Adamczyk on rejoining the Dowhttps://www.cnbc.com/video/2020/09/10/honeywell-ceo-darius-adamczyk-on-rejoining-the-dow.html?&qsearchterm=exxon mobil                             | cnbc     |
| 2020-09-09 00:00:00 | https://www.cnbc.com/2020/09/09/options-market-predicts-exxon-mobils-dividend-could-be-in-danger.html?&qsearchterm=exxon mobil    | Options market predicts Exxon Mobil’s dividend could be in danger   | One of the most consistent dividend payers in the history of the energy trade could be in danger of having to slash its payout, according ...                             | Options Action  | Tyler Bailey | 2020-09-16 14:14:43.533664 | XOM      |        nan | CNBC        | exxon mobil   | CNBCOptions market predicts Exxon Mobil’s dividend could be in dangerhttps://www.cnbc.com/2020/09/09/options-market-predicts-exxon-mobils-dividend-could-be-in-danger.html?&qsearchterm=exxon mobil      | cnbc     |
| 2020-09-08 00:00:00 | https://www.cnbc.com/2020/09/08/exxon-downsizes-global-empire-as-wall-street-worries-about-dividend.html?&qsearchterm=exxon mobil | Exxon downsizes global empire as Wall Street worries about dividend | Ill-timed bets on rising demand have Exxon Mobil facing a shortfall of about $48 billion through 2021, according to a Reuters tally and Wall Street ...                   | Oil and Gas     | nan          | 2020-09-16 14:14:43.533664 | XOM      |        nan | CNBC        | exxon mobil   | CNBCExxon downsizes global empire as Wall Street worries about dividendhttps://www.cnbc.com/2020/09/08/exxon-downsizes-global-empire-as-wall-street-worries-about-dividend.html?&qsearchterm=exxon mobil | cnbc     |
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|


</small></small></center>

</details>

<div align = "right">  <a href="#i80">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f81" ><i>NewsData(ticker, keywords).ft()</i></div>

<ul>
<li>Returns the news headlines from the Financial Times for the specified keywords.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.ft(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

<center><small><small>

| date                | link                                          | headline                                                         | description                                                                                                                                                                                                                     | tag                  | date_retrieved             | ticker   |   comments |   author | newspaper   | search_term   | id                                                                                                              | source   |
|:--------------------|:----------------------------------------------|:-----------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|:---------------------------|:---------|-----------:|---------:|:------------|:--------------|:----------------------------------------------------------------------------------------------------------------|:---------|
| 2020-07-31 00:00:00 | /content/64d7e86e-079c-4502-a9a4-5ab7439c732f | Big Oil gets smaller as Chevron and Exxon losses mount to $9.4bn | ...destruction in the second quarter was unprecedented in the history of modern oil markets,” Neil Chapman, Exxon senior vice-president, told analysts on an investor call.                  “To put it in context, absolute... | Oil & Gas industry   | 2020-09-16 14:20:31.865540 | XOM      |        nan |      nan | FT          | exxon mobil   | FTBig Oil gets smaller as Chevron and Exxon losses mount to $9.4bn/content/64d7e86e-079c-4502-a9a4-5ab7439c732f | ft       |
| 2020-05-27 00:00:00 | /content/c43ead81-5af3-44de-af1e-b108d6491354 | Exxon shareholders vote against splitting chair and CEO roles    | ...Exxon, said the appointment of a lead director had helped improve oversight.                  A separate resolution calling for increased transparency about Exxon’s lobbying activity won 37.5 per cent support, a...       | Oil & Gas industry   | 2020-09-16 14:20:31.865540 | XOM      |        nan |      nan | FT          | exxon mobil   | FTExxon shareholders vote against splitting chair and CEO roles/content/c43ead81-5af3-44de-af1e-b108d6491354    | ft       |
| 2020-05-12 00:00:00 | /content/c54ee229-f4e7-43c8-87a5-e383099542fb | Big Exxon shareholder to vote against chief                      | ...company to disclose its lobbying activities, arguing it was falling behind global peers by failing to act on climate change.                  Wednesday’s move by LGIM, whose roughly $1bn stake makes it a top-20 Exxon...  | Corporate governance | 2020-09-16 14:20:31.865540 | XOM      |        nan |      nan | FT          | exxon mobil   | FTBig Exxon shareholder to vote against chief/content/c54ee229-f4e7-43c8-87a5-e383099542fb                      | ft       |
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|


</small></small></center>

</details>

<div align = "right">  <a href="#i81">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f82" ><i>NewsData(ticker, keywords).nyt()</i></div>

<ul>
<li>Returns the news headlines from the New York Times for the specified keywords.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.nyt(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

<center><small><small>

| date                | link                                                                                                  | headline                                                                       | description                                                                                                                                                                                                                                                             | tag      | author               |   comments | date_retrieved             | ticker   | newspaper   | search_term   | id                                                                                                                                                                                 | source   |
|:--------------------|:------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------------|-----------:|:---------------------------|:---------|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| 2020-09-08 00:00:00 | /aponline/2020/09/08/business/ap-financial-markets-stocks.html?searchResultPosition=2                 | Exxon, Tesla Fall; Nikola, Beyond Meat Rise                                    | Stocks that moved heavily or traded substantially Tuesday:                                                                                                                                                                                                              | Business | The Associated Press |        nan | 2020-09-16 14:22:13.032245 | XOM      | NYT         | exxon mobil   | NYTExxon, Tesla Fall; Nikola, Beyond Meat Rise/aponline/2020/09/08/business/ap-financial-markets-stocks.html?searchResultPosition=2                                                | nyt      |
| 2020-09-08 00:00:00 | /reuters/2020/09/08/business/08reuters-exxon-mobil-spending-exclusive.html?searchResultPosition=3     | Exclusive: Exxon Downsizes Global Empire as Wall Street Worries About Dividend | Ill-timed bets on rising demand have Exxon Mobil Corp facing a shortfall of about $48 billion through 2021, according to a Reuters tally and Wall Street estimates, a situation that will require the top U.S. oil company to make deep cuts to its staff and projects. | Business | Reuters              |        nan | 2020-09-16 14:22:13.032245 | XOM      | NYT         | exxon mobil   | NYTExclusive: Exxon Downsizes Global Empire as Wall Street Worries About Dividend/reuters/2020/09/08/business/08reuters-exxon-mobil-spending-exclusive.html?searchResultPosition=3 | nyt      |
| 2020-09-03 00:00:00 | /reuters/2020/09/03/business/03reuters-refinery-operations-exxon-beaumont.html?searchResultPosition=4 | Exxon Beaumont, Texas, Refinery Restarts Large Crude Unit: Sources             | Exxon Mobil Corp restarted the large crude distillation unit (CDU) at its 369,024 barrel-per-day (bpd) Beaumont, Texas, refinery on Thursday, said sources familiar with plant operations.                                                                              | Business | Reuters              |        nan | 2020-09-16 14:22:13.032245 | XOM      | NYT         | exxon mobil   | NYTExxon Beaumont, Texas, Refinery Restarts Large Crude Unit: Sources/reuters/2020/09/03/business/03reuters-refinery-operations-exxon-beaumont.html?searchResultPosition=4         | nyt      |
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|


</small></small></center>

</details>

<div align = "right">  <a href="#i82">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <div id = "f84" ><i>NewsData(ticker, keywords).seeking\_alpha(datestop, press_releases = False)</i></div>

<ul>
<li>Returns the news headlines from Seeking Alpha for the specified keywords.</li>
<li>It can happen that access to SeekingAlpha requires to solve a captcha by pressing and holding a button when run for the first time in a program. Will try to fix this in future versions. <code>press_releases = True</code> will get press releases instead of news headlines.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.seeking_alpha(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

<center><small><small>

| date                | link                                                                                                                                                                                         | headline                                                    | author   | comments   | date_retrieved             | ticker   |   description |   tag | newspaper   | search_term   | id                                                                                                                                                                                                                                                               | source   |
|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|:---------|:-----------|:---------------------------|:---------|--------------:|------:|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| 2020-09-15 00:00:00 | /news/3614409-options-traders-pricing-in-exxon-dividend-cut-analyst-says?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:1 | Options traders pricing in Exxon dividend cut, analyst says | SA News  | 0 comments | 2020-09-16 15:14:23.575898 | XOM      |           nan |   nan | SA - News   | exxon mobil   | SA - NewsOptions traders pricing in Exxon dividend cut, analyst says/news/3614409-options-traders-pricing-in-exxon-dividend-cut-analyst-says?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:1 | sa       |
| 2020-09-14 00:00:00 | /news/3613801-connecticut-latest-state-to-sue-exxon-over-climate-change?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:2  | Connecticut latest state to sue Exxon over climate change   | SA News  | 0 comments | 2020-09-16 15:14:23.575898 | XOM      |           nan |   nan | SA - News   | exxon mobil   | SA - NewsConnecticut latest state to sue Exxon over climate change/news/3613801-connecticut-latest-state-to-sue-exxon-over-climate-change?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:2 | sa       |
| 2020-09-10 00:00:00 | /news/3612953-exxon-rated-new-buy-mkm-shares-slip?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:3                         | Exxon rated new Buy at MKM but shares slip                  | SA News  | 0 comments | 2020-09-16 15:14:23.575898 | XOM      |           nan |   nan | SA - News   | exxon mobil   | SA - NewsExxon rated new Buy at MKM but shares slip/news/3612953-exxon-rated-new-buy-mkm-shares-slip?source=content_type:react|section:News|sectionAsset:News|first_level_url:symbol|button:Author|lock_status:No|line:3                                         | sa       |
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|


</small></small></center>

</details>

<div align = "right">  <a href="#i84">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <div id = "f85" ><i>NewsData(ticker, keywords).wsj()</i></div>

<ul>
<li>Returns the news headlines from the Wall Street Journal for the specified keywords.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.wsj(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

<center><small><small>


| date                | link                                                                                                                       | headline                                                         | description                                                                                                                                                                                                     | author                  | tag                 | date_retrieved             | ticker   | newspaper   | search_term   | id                                                                                                                                                                                            |   comments | source   |
|:--------------------|:---------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|:--------------------|:---------------------------|:---------|:------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------:|:---------|
| 2020-09-13 00:00:00 | /articles/exxon-used-to-be-americas-most-valuable-company-what-happened-oil-gas-11600037243?mod=searchresults&page=1&pos=1 | Exxon Used to Be America’s Most Valuable Company. What Happened? | The oil giant doubled down on oil and gas at what now looks to be the worst possible time. Investors are fleeing and workers are grumbling about the direction of a company some see as out of touch.           | Christopher M. Matthews | Business            | 2020-09-16 15:19:39.733511 | XOM      | WSJ         | exxon mobil   | WSJExxon Used to Be America’s Most Valuable Company. What Happened?/articles/exxon-used-to-be-americas-most-valuable-company-what-happened-oil-gas-11600037243?mod=searchresults&page=1&pos=1 |        nan | wsj      |
| 2020-09-10 00:00:00 | /articles/oil-major-bp-gives-a-taste-of-how-it-will-go-green-11599745648?mod=searchresults&page=1&pos=2                    | Oil Major BP Gives a Taste of How It Will Go Green               | A deal to buy into wind farms off the coast of New York and Massachusetts showcases the British company’s ambitions in the clean-energy sector—and the risks it is taking.                                      | Rochelle Toplensky      | Heard on the Street | 2020-09-16 15:19:39.733511 | XOM      | WSJ         | exxon mobil   | WSJOil Major BP Gives a Taste of How It Will Go Green/articles/oil-major-bp-gives-a-taste-of-how-it-will-go-green-11599745648?mod=searchresults&page=1&pos=2                                  |        nan | wsj      |
| 2020-09-08 00:00:00 | /articles/oil-prices-drop-on-faltering-recovery-in-demand-11599562101?mod=searchresults&page=1&pos=3                       | Oil Prices Tumble on Faltering Recovery in Demand                | Oil prices slumped to their lowest level in nearly three months, under pressure from a stalling recovery in demand and planned production expansions by OPEC that threaten to add to an existing glut of crude. | Joe Wallace             | Oil Markets         | 2020-09-16 15:19:39.733511 | XOM      | WSJ         | exxon mobil   | WSJOil Prices Tumble on Faltering Recovery in Demand/articles/oil-prices-drop-on-faltering-recovery-in-demand-11599562101?mod=searchresults&page=1&pos=3                                      |        nan | wsj      |
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|


</small></small></center>

</details>

<div align = "right">  <a href="#i85">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


## <div id="A8">Other data</div>


<div align="right"><a href="#0">Back to top</a> </div>


#### <div id = "f86" ><i>nasdaq\_tickers()</i></div>

<ul>
<li>Returns dataframe of tickers traded on the Nasdaq exchange.</li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
nasdaq_tickers()
```

<center><small><small>

|    | Symbol   | Security Name                                                                                    |
|---:|:---------|:-------------------------------------------------------------------------------------------------|
|  0 | AACG     | ATA Creativity Global - American Depositary Shares, each representing two common shares          |
|  1 | AACQ     | Artius Acquisition Inc. - Class A Common Stock                                                   |
|  2 | AACQU    | Artius Acquisition Inc. - Unit consisting of one ordinary share and one third redeemable warrant |
|  3 | AACQW    | Artius Acquisition Inc. - Warrant                                                                |
|  4 | AAL      | American Airlines Group, Inc. - Common Stock                                                     |
|  ... | ...    | ...        				                                                                           |


</small></small></center>

</details>

<div align = "right">  <a href="#i86">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <div id = "f87" ><i>global\_tickers()</i></div>

<ul>
<li>Returns 100.000+ global tickers from Gurufocus.com. Note that companies are listed in different countries or exchanges with different ticker symbols. </li>
</ul>

<details>
<summary><i> Example </i></summary>

```python
global_tickers()
```

<center><small><small>

|    | Symbol          | Company                      |
|---:|:----------------|:-----------------------------|
|  0 | QNCO.Israel     | (Y.Z) Queenco Ltd            |
|  1 | ONE.Canada      | 01 Communique Laboratory Inc |
|  2 | DFK.Germany     | 01 Communique Laboratory Inc |
|  3 | OCQLF           | 01 Communique Laboratory Inc |
|  4 | 01C.Poland      | 01Cyberaton SA               |
|  5 | 1PG.Australia   | 1 Page Ltd                   |
|  6 | I8Y.Germany     | 1 Page Ltd                   |
|  8 | 8458.Taiwan     | 1 Production Film Co         |
|  9 | DRI.Austria     | 1&1 Drillisch AG             |
| 10 | DRI.Switzerland | 1&1 Drillisch AG             |
|  ... | ...    | ...        				    |

</small></small></center>

</details>

<div align = "right">  <a href="#i87">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <div id = "f132" ><i>cftc( report_type = 'futures\_traders', year = 2000 )</i></div>

<ul>
<li>Returns the CFTC reports for the given report type and period. Information on the data can be found <a href = "https://cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm">here</a>.</li>
<li>
<code>report_type</code> options:
<ul>
<li>'disaggregated_futures': Disaggregated Futures Only Reports </li>
<li>'disaggregated_combined':  Disaggregated Futures-and-Options Combined Reports </li>
<li>'futures_traders' (default):  Traders in Financial Futures ; Futures Only Reports  </li>
<li>'futures_traders_combined':  Traders in Financial Futures ; Futures-and-Options Combined Reports  </li>
<li>'futures':  Futures Only Reports  </li>
<li>'futures_combined':  Futures-and-Options Combined Reports  </li>
<li>'commodity_index':  Commodity Index Trader Supplement  </li>
</ul>
</li>
<li> If the <code>year</code> parameter is smaller than 2016, all available data will be returned.
</ul>

<details>
<summary><i> Example </i></summary>

```python
cftc(report_type = 'futures', year = 2020)
```

<center><small><small>

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>market_and_exchange_names</th>      <th>cftc_contract_market_code</th>      <th>cftc_market_code_in_initials</th>      <th>cftc_region_code</th>      <th>cftc_commodity_code</th>      <th>open_interest_(all)</th>      <th>noncommercial_positions-long_(all)</th>      <th>noncommercial_positions-short_(all)</th>      <th>noncommercial_positions-spreading_(all)</th>      <th>commercial_positions-long_(all)</th>      <th>commercial_positions-short_(all)</th>      <th>_total_reportable_positions-long_(all)</th>      <th>total_reportable_positions-short_(all)</th>      <th>nonreportable_positions-long_(all)</th>      <th>nonreportable_positions-short_(all)</th>      <th>open_interest_(old)</th>      <th>noncommercial_positions-long_(old)</th>      <th>noncommercial_positions-short_(old)</th>      <th>noncommercial_positions-spreading_(old)</th>      <th>commercial_positions-long_(old)</th>      <th>commercial_positions-short_(old)</th>      <th>total_reportable_positions-long_(old)</th>      <th>total_reportable_positions-short_(old)</th>      <th>nonreportable_positions-long_(old)</th>      <th>nonreportable_positions-short_(old)</th>      <th>open_interest_(other)</th>      <th>noncommercial_positions-long_(other)</th>      <th>noncommercial_positions-short_(other)</th>      <th>noncommercial_positions-spreading_(other)</th>      <th>commercial_positions-long_(other)</th>      <th>commercial_positions-short_(other)</th>      <th>total_reportable_positions-long_(other)</th>      <th>total_reportable_positions-short_(other)</th>      <th>nonreportable_positions-long_(other)</th>      <th>nonreportable_positions-short_(other)</th>      <th>change_in_open_interest_(all)</th>      <th>change_in_noncommercial-long_(all)</th>      <th>change_in_noncommercial-short_(all)</th>      <th>change_in_noncommercial-spreading_(all)</th>      <th>change_in_commercial-long_(all)</th>      <th>change_in_commercial-short_(all)</th>      <th>change_in_total_reportable-long_(all)</th>      <th>change_in_total_reportable-short_(all)</th>      <th>change_in_nonreportable-long_(all)</th>      <th>change_in_nonreportable-short_(all)</th>      <th>%_of_open_interest_(oi)_(all)</th>      <th>%_of_oi-noncommercial-long_(all)</th>      <th>%_of_oi-noncommercial-short_(all)</th>      <th>%_of_oi-noncommercial-spreading_(all)</th>      <th>%_of_oi-commercial-long_(all)</th>      <th>%_of_oi-commercial-short_(all)</th>      <th>%_of_oi-total_reportable-long_(all)</th>      <th>%_of_oi-total_reportable-short_(all)</th>      <th>%_of_oi-nonreportable-long_(all)</th>      <th>%_of_oi-nonreportable-short_(all)</th>      <th>%_of_open_interest_(oi)(old)</th>      <th>%_of_oi-noncommercial-long_(old)</th>      <th>%_of_oi-noncommercial-short_(old)</th>      <th>%_of_oi-noncommercial-spreading_(old)</th>      <th>%_of_oi-commercial-long_(old)</th>      <th>%_of_oi-commercial-short_(old)</th>      <th>%_of_oi-total_reportable-long_(old)</th>      <th>%_of_oi-total_reportable-short_(old)</th>      <th>%_of_oi-nonreportable-long_(old)</th>      <th>%_of_oi-nonreportable-short_(old)</th>      <th>%_of_open_interest_(oi)_(other)</th>      <th>%_of_oi-noncommercial-long_(other)</th>      <th>%_of_oi-noncommercial-short_(other)</th>      <th>%_of_oi-noncommercial-spreading_(other)</th>      <th>%_of_oi-commercial-long_(other)</th>      <th>%_of_oi-commercial-short_(other)</th>      <th>%_of_oi-total_reportable-long_(other)</th>      <th>%_of_oi-total_reportable-short_(other)</th>      <th>%_of_oi-nonreportable-long_(other)</th>      <th>%_of_oi-nonreportable-short_(other)</th>      <th>traders-total_(all)</th>      <th>traders-noncommercial-long_(all)</th>      <th>traders-noncommercial-short_(all)</th>      <th>traders-noncommercial-spreading_(all)</th>      <th>traders-commercial-long_(all)</th>      <th>traders-commercial-short_(all)</th>      <th>traders-total_reportable-long_(all)</th>      <th>traders-total_reportable-short_(all)</th>      <th>traders-total_(old)</th>      <th>traders-noncommercial-long_(old)</th>      <th>traders-noncommercial-short_(old)</th>      <th>traders-noncommercial-spreading_(old)</th>      <th>traders-commercial-long_(old)</th>      <th>traders-commercial-short_(old)</th>      <th>traders-total_reportable-long_(old)</th>      <th>traders-total_reportable-short_(old)</th>      <th>traders-total_(other)</th>      <th>traders-noncommercial-long_(other)</th>      <th>traders-noncommercial-short_(other)</th>      <th>traders-noncommercial-spreading_(other)</th>      <th>traders-commercial-long_(other)</th>      <th>traders-commercial-short_(other)</th>      <th>traders-total_reportable-long_(other)</th>      <th>traders-total_reportable-short_(other)</th>      <th>concentration-gross_lt_=_4_tdr-long_(all)</th>      <th>concentration-gross_lt_=4_tdr-short_(all)</th>      <th>concentration-gross_lt_=8_tdr-long_(all)</th>      <th>concentration-gross_lt_=8_tdr-short_(all)</th>      <th>concentration-net_lt_=4_tdr-long_(all)</th>      <th>concentration-net_lt_=4_tdr-short_(all)</th>      <th>concentration-net_lt_=8_tdr-long_(all)</th>      <th>concentration-net_lt_=8_tdr-short_(all)</th>      <th>concentration-gross_lt_=4_tdr-long_(old)</th>      <th>concentration-gross_lt_=4_tdr-short_(old)</th>      <th>concentration-gross_lt_=8_tdr-long_(old)</th>      <th>concentration-gross_lt_=8_tdr-short_(old)</th>      <th>concentration-net_lt_=4_tdr-long_(old)</th>      <th>concentration-net_lt_=4_tdr-short_(old)</th>      <th>concentration-net_lt_=8_tdr-long_(old)</th>      <th>concentration-net_lt_=8_tdr-short_(old)</th>      <th>concentration-gross_lt_=4_tdr-long_(other)</th>      <th>concentration-gross_lt_=4_tdr-short(other)</th>      <th>concentration-gross_lt_=8_tdr-long_(other)</th>      <th>concentration-gross_lt_=8_tdr-short(other)</th>      <th>concentration-net_lt_=4_tdr-long_(other)</th>      <th>concentration-net_lt_=4_tdr-short_(other)</th>      <th>concentration-net_lt_=8_tdr-long_(other)</th>      <th>concentration-net_lt_=8_tdr-short_(other)</th>      <th>contract_units</th>      <th>cftc_contract_market_code_(quotes)</th>      <th>cftc_market_code_in_initials_(quotes)</th>      <th>cftc_commodity_code_(quotes)</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2020-11-17</th>      <td>WHEAT-SRW - CHICAGO BOARD OF TRADE</td>      <td>001602</td>      <td>CBT</td>      <td>0</td>      <td>1</td>      <td>432714</td>      <td>127007</td>      <td>108586</td>      <td>108258</td>      <td>162186</td>      <td>168899</td>      <td>397451</td>      <td>385743</td>      <td>35263</td>      <td>46971</td>      <td>290010</td>      <td>100877</td>      <td>91806</td>      <td>55396</td>      <td>107265</td>      <td>114199</td>      <td>263538</td>      <td>261401</td>      <td>26472</td>      <td>28609</td>      <td>142704</td>      <td>49751</td>      <td>40401</td>      <td>29241</td>      <td>54921</td>      <td>54700</td>      <td>133913</td>      <td>124342</td>      <td>8791</td>      <td>18362</td>      <td>-8804</td>      <td>-14010</td>      <td>1027</td>      <td>6421</td>      <td>-1417</td>      <td>-14619</td>      <td>-9006</td>      <td>-7171</td>      <td>202</td>      <td>-1633</td>      <td>100</td>      <td>29.4</td>      <td>25.1</td>      <td>25</td>      <td>37.5</td>      <td>39</td>      <td>91.9</td>      <td>89.1</td>      <td>8.1</td>      <td>10.9</td>      <td>100</td>      <td>34.8</td>      <td>31.7</td>      <td>19.1</td>      <td>37</td>      <td>39.4</td>      <td>90.9</td>      <td>90.1</td>      <td>9.1</td>      <td>9.9</td>      <td>100</td>      <td>34.9</td>      <td>28.3</td>      <td>20.5</td>      <td>38.5</td>      <td>38.3</td>      <td>93.8</td>      <td>87.1</td>      <td>6.2</td>      <td>12.9</td>      <td>392</td>      <td>113</td>      <td>120</td>      <td>114</td>      <td>83</td>      <td>127</td>      <td>268</td>      <td>301</td>      <td>373</td>      <td>106</td>      <td>121</td>      <td>89</td>      <td>73</td>      <td>122</td>      <td>233</td>      <td>281</td>      <td>223</td>      <td>54</td>      <td>55</td>      <td>39</td>      <td>49</td>      <td>87</td>      <td>128</td>      <td>161</td>      <td>16.8</td>      <td>12.4</td>      <td>25.5</td>      <td>19.5</td>      <td>14.1</td>      <td>8.2</td>      <td>21.6</td>      <td>13.4</td>      <td>15.9</td>      <td>9.2</td>      <td>25.9</td>      <td>17.1</td>      <td>15.4</td>      <td>8</td>      <td>25.1</td>      <td>14.9</td>      <td>24.4</td>      <td>27.7</td>      <td>36.3</td>      <td>37.9</td>      <td>17.3</td>      <td>16.3</td>      <td>26.4</td>      <td>23.8</td>      <td>(CONTRACTS OF 5,000 BUSHELS)</td>      <td>001602</td>      <td>CBT</td>      <td>1</td>    </tr>    <tr>      <th>2020-11-10</th>      <td>WHEAT-SRW - CHICAGO BOARD OF TRADE</td>      <td>001602</td>      <td>CBT</td>      <td>0</td>      <td>1</td>      <td>441518</td>      <td>141017</td>      <td>107559</td>      <td>101837</td>      <td>163603</td>      <td>183518</td>      <td>406457</td>      <td>392914</td>      <td>35061</td>      <td>48604</td>      <td>309149</td>      <td>117977</td>      <td>91684</td>      <td>53973</td>      <td>110678</td>      <td>132654</td>      <td>282628</td>      <td>278311</td>      <td>26521</td>      <td>30838</td>      <td>132369</td>      <td>45187</td>      <td>38022</td>      <td>25717</td>      <td>52925</td>      <td>50864</td>      <td>123829</td>      <td>114603</td>      <td>8540</td>      <td>17766</td>      <td>-17695</td>      <td>-3704</td>      <td>4074</td>      <td>-3266</td>      <td>-11418</td>      <td>-16834</td>      <td>-18388</td>      <td>-16026</td>      <td>693</td>      <td>-1669</td>      <td>10000</td>      <td>3109</td>      <td>2404</td>      <td>2301</td>      <td>3701</td>      <td>4106</td>      <td>9201</td>      <td>8900</td>      <td>709</td>      <td>1100</td>      <td>10000</td>      <td>3802</td>      <td>2907</td>      <td>1705</td>      <td>3508</td>      <td>4209</td>      <td>9104</td>      <td>9000</td>      <td>806</td>      <td>1000</td>      <td>10000</td>      <td>3401</td>      <td>2807</td>      <td>1904</td>      <td>4000</td>      <td>3804</td>      <td>9305</td>      <td>8606</td>      <td>605</td>      <td>1304</td>      <td>389</td>      <td>120</td>      <td>106</td>      <td>108</td>      <td>87</td>      <td>127</td>      <td>273</td>      <td>286</td>      <td>373</td>      <td>111</td>      <td>111</td>      <td>86</td>      <td>77</td>      <td>121</td>      <td>239</td>      <td>270</td>      <td>220</td>      <td>52</td>      <td>52</td>      <td>35</td>      <td>49</td>      <td>88</td>      <td>125</td>      <td>155</td>      <td>1605</td>      <td>1301</td>      <td>2504</td>      <td>2008</td>      <td>1308</td>      <td>900</td>      <td>2106</td>      <td>1405</td>      <td>1500</td>      <td>1000</td>      <td>2504</td>      <td>1802</td>      <td>1405</td>      <td>809</td>      <td>2406</td>      <td>1600</td>      <td>2508</td>      <td>2709</td>      <td>3805</td>      <td>3808</td>      <td>1709</td>      <td>1601</td>      <td>2706</td>      <td>2404</td>      <td>(CONTRACTS OF 5,000 BUSHELS)</td>      <td>001602</td>      <td>CBT</td>      <td>1</td>    </tr>    <tr>      <th>2020-11-03</th>      <td>WHEAT-SRW - CHICAGO BOARD OF TRADE</td>      <td>001602</td>      <td>CBT</td>      <td>0</td>      <td>1</td>      <td>459213</td>      <td>144721</td>      <td>103485</td>      <td>105103</td>      <td>175021</td>      <td>200352</td>      <td>424845</td>      <td>408940</td>      <td>34368</td>      <td>50273</td>      <td>335930</td>      <td>124897</td>      <td>93364</td>      <td>58310</td>      <td>126302</td>      <td>151768</td>      <td>309509</td>      <td>303442</td>      <td>26421</td>      <td>32488</td>      <td>123283</td>      <td>43831</td>      <td>34128</td>      <td>22786</td>      <td>48719</td>      <td>48584</td>      <td>115336</td>      <td>105498</td>      <td>7947</td>      <td>17785</td>      <td>1309</td>      <td>-6915</td>      <td>-4209</td>      <td>-2235</td>      <td>11389</td>      <td>7396</td>      <td>2239</td>      <td>952</td>      <td>-930</td>      <td>357</td>      <td>100</td>      <td>31.5</td>      <td>22.5</td>      <td>22.9</td>      <td>38.1</td>      <td>43.6</td>      <td>92.5</td>      <td>89.1</td>      <td>7.5</td>      <td>10.9</td>      <td>100</td>      <td>37.2</td>      <td>27.8</td>      <td>17.4</td>      <td>37.6</td>      <td>45.2</td>      <td>92.1</td>      <td>90.3</td>      <td>7.9</td>      <td>9.7</td>      <td>100</td>      <td>35.6</td>      <td>27.7</td>      <td>18.5</td>      <td>39.5</td>      <td>39.4</td>      <td>93.6</td>      <td>85.6</td>      <td>6.4</td>      <td>14.4</td>      <td>393</td>      <td>119</td>      <td>108</td>      <td>106</td>      <td>91</td>      <td>130</td>      <td>275</td>      <td>290</td>      <td>382</td>      <td>111</td>      <td>114</td>      <td>88</td>      <td>76</td>      <td>122</td>      <td>243</td>      <td>274</td>      <td>204</td>      <td>46</td>      <td>47</td>      <td>31</td>      <td>51</td>      <td>84</td>      <td>116</td>      <td>146</td>      <td>15.7</td>      <td>13.7</td>      <td>24.5</td>      <td>21.7</td>      <td>12.4</td>      <td>8.7</td>      <td>20.2</td>      <td>14.6</td>      <td>14.5</td>      <td>11.9</td>      <td>24.3</td>      <td>19.6</td>      <td>12.9</td>      <td>9.4</td>      <td>22.4</td>      <td>16.3</td>      <td>25.8</td>      <td>28.7</td>      <td>38.9</td>      <td>39.2</td>      <td>17.1</td>      <td>16.7</td>      <td>27.5</td>      <td>24.4</td>      <td>(CONTRACTS OF 5,000 BUSHELS)</td>      <td>001602</td>      <td>CBT</td>      <td>1</td>    </tr>    <tr>      <th>2020-10-27</th>      <td>WHEAT-SRW - CHICAGO BOARD OF TRADE</td>      <td>001602</td>      <td>CBT</td>      <td>0</td>      <td>1</td>      <td>457904</td>      <td>151636</td>      <td>107694</td>      <td>107338</td>      <td>163632</td>      <td>192956</td>      <td>422606</td>      <td>407988</td>      <td>35298</td>      <td>49916</td>      <td>340631</td>      <td>132614</td>      <td>101843</td>      <td>60118</td>      <td>120105</td>      <td>145840</td>      <td>312837</td>      <td>307801</td>      <td>27794</td>      <td>32830</td>      <td>117273</td>      <td>45561</td>      <td>32390</td>      <td>20681</td>      <td>43527</td>      <td>47116</td>      <td>109769</td>      <td>100187</td>      <td>7504</td>      <td>17086</td>      <td>13223</td>      <td>2593</td>      <td>5188</td>      <td>788</td>      <td>7089</td>      <td>7666</td>      <td>10470</td>      <td>13642</td>      <td>2753</td>      <td>-419</td>      <td>100</td>      <td>33.1</td>      <td>23.5</td>      <td>23.4</td>      <td>35.7</td>      <td>42.1</td>      <td>92.3</td>      <td>89.1</td>      <td>7.7</td>      <td>10.9</td>      <td>100</td>      <td>38.9</td>      <td>29.9</td>      <td>17.6</td>      <td>35.3</td>      <td>42.8</td>      <td>91.8</td>      <td>90.4</td>      <td>8.2</td>      <td>9.6</td>      <td>100</td>      <td>38.9</td>      <td>27.6</td>      <td>17.6</td>      <td>37.1</td>      <td>40.2</td>      <td>93.6</td>      <td>85.4</td>      <td>6.4</td>      <td>14.6</td>      <td>402</td>      <td>129</td>      <td>115</td>      <td>106</td>      <td>82</td>      <td>125</td>      <td>271</td>      <td>294</td>      <td>388</td>      <td>119</td>      <td>120</td>      <td>88</td>      <td>68</td>      <td>118</td>      <td>240</td>      <td>276</td>      <td>206</td>      <td>49</td>      <td>48</td>      <td>29</td>      <td>49</td>      <td>82</td>      <td>112</td>      <td>149</td>      <td>14.8</td>      <td>13.2</td>      <td>23.8</td>      <td>21.4</td>      <td>11.8</td>      <td>8.9</td>      <td>19.9</td>      <td>15.6</td>      <td>14.3</td>      <td>11.6</td>      <td>23.9</td>      <td>20.5</td>      <td>13.2</td>      <td>10.1</td>      <td>22.3</td>      <td>16.9</td>      <td>25.6</td>      <td>29.2</td>      <td>38.6</td>      <td>39</td>      <td>16.9</td>      <td>18.2</td>      <td>28.2</td>      <td>25.7</td>      <td>(CONTRACTS OF 5,000 BUSHELS)</td>      <td>001602</td>      <td>CBT</td>      <td>1</td>    </tr>    <tr>      <th>2020-10-20</th>      <td>WHEAT-SRW - CHICAGO BOARD OF TRADE</td>      <td>001602</td>      <td>CBT</td>      <td>0</td>      <td>1</td>      <td>444681</td>      <td>149043</td>      <td>102506</td>      <td>106550</td>      <td>156543</td>      <td>185290</td>      <td>412136</td>      <td>394346</td>      <td>32545</td>      <td>50335</td>      <td>334451</td>      <td>132530</td>      <td>99016</td>      <td>60133</td>      <td>116411</td>      <td>141422</td>      <td>309074</td>      <td>300571</td>      <td>25377</td>      <td>33880</td>      <td>110230</td>      <td>43092</td>      <td>30069</td>      <td>19838</td>      <td>40132</td>      <td>43868</td>      <td>103062</td>      <td>93775</td>      <td>7168</td>      <td>16455</td>      <td>28174</td>      <td>13140</td>      <td>9401</td>      <td>1205</td>      <td>11140</td>      <td>14955</td>      <td>25485</td>      <td>25561</td>      <td>2689</td>      <td>2613</td>      <td>100</td>      <td>33.5</td>      <td>23.1</td>      <td>24</td>      <td>35.2</td>      <td>41.7</td>      <td>92.7</td>      <td>88.7</td>      <td>7.3</td>      <td>11.3</td>      <td>100</td>      <td>39.6</td>      <td>29.6</td>      <td>18</td>      <td>34.8</td>      <td>42.3</td>      <td>92.4</td>      <td>89.9</td>      <td>7.6</td>      <td>10.1</td>      <td>100</td>      <td>39.1</td>      <td>27.3</td>      <td>18</td>      <td>36.4</td>      <td>39.8</td>      <td>93.5</td>      <td>85.1</td>      <td>6.5</td>      <td>14.9</td>      <td>390</td>      <td>122</td>      <td>109</td>      <td>105</td>      <td>79</td>      <td>126</td>      <td>261</td>      <td>291</td>      <td>379</td>      <td>117</td>      <td>113</td>      <td>84</td>      <td>69</td>      <td>121</td>      <td>232</td>      <td>275</td>      <td>200</td>      <td>49</td>      <td>42</td>      <td>29</td>      <td>46</td>      <td>83</td>      <td>108</td>      <td>145</td>      <td>14.9</td>      <td>13.5</td>      <td>24.2</td>      <td>21.1</td>      <td>11.7</td>      <td>9.4</td>      <td>20</td>      <td>15.9</td>      <td>14.3</td>      <td>10.9</td>      <td>24.7</td>      <td>19.1</td>      <td>13.4</td>      <td>9.9</td>      <td>22.3</td>      <td>17.3</td>      <td>27.4</td>      <td>30.6</td>      <td>39.7</td>      <td>40.8</td>      <td>18</td>      <td>18.9</td>      <td>27.9</td>      <td>27.1</td>      <td>(CONTRACTS OF 5,000 BUSHELS)</td>      <td>001602</td>      <td>CBT</td>      <td>1</td>    </tr>
<tr>      <th>2020-10-13</th>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>      <td>...</td>    </tr>  </tbody></table>


</small></small></center>

</details>

<div align = "right">  <a href="#i132">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

## <div id="A9"> Sources </div>

<li>Barrons, www.barrons.com</li>
<li>CBOE, www.cboe.com</li>
<li>CFTC, www.cftc.gov</li>
<li>CNBC, www.cnbc.com</li>
<li>Financial Times, www.ft.com</li>
<li>Finviz, www.finviz.com</li>
<li>Gurufocus, www.gurufocus.com</li>
<li>Investing.com, www.investing.com </li>
<li>MarketWatch, www.marketwatch.com </li>
<li>Macrotrends, www.macrotrends.net</li>
<li>Moore Research Center, www.mrci.com </li>
<li>Motley Fool, www.fool.com</li>
<li>NASDAQ, www.nasdaq.com</li>
<li>Seeking Alpha, www.seekingalpha.com</li>
<li>Wall Street Journal, www.wsj.com</li>
<li>Yahoo Finance, www.finance.yahoo.com </li>

<br>

<div align="right"><a href="#0">Back to top</a> </div>

----

## <div id="A10">License</div>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2020 Peter la Cour
