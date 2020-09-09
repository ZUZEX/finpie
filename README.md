

-------------



# jippy - a simple library to download some financial data

<p>


<b>For recreational use only. Made for finance students for personal educational purposes to have easier access to some financial and finance related data.</b>


</p>

<p>This library is an ongoing project designed to facilitate access to some finance related data, however, the library is still far from perfect. It tries to cover most useful or interesting data points but unfortunately some functions will only return single point data which however could be aggregated over time to construct a limited time series. On the other hand, some functions that retrieve large amounts of data or depending on the data source will take some time to run. See the <a href="#3">function index </a> for more information on issues of data availability and run time.</p> 
<p>
The company fundamentals module includes functions to retrive data from <code>Yahoo Finance</code>, <code>MarketWatch</code> and <code>Finviz</code>. The price data module retrieves data from <code>Yahoo Finance</code>, <code>Investing.com</code> and also includes a wrapper for price data APIs including <code>Alpha-Vantage</code>, <code>IEX Cloud</code> and <code>Tiingo</code> which require a (free) api-key from the respective provider. The economic data is solely pulled from the <code>OECD database</code> at this point and the news module enables historical news collection from the <code>FT</code>, <code>NYT</code>, <code>WSJ</code>, <code>Barrons</code>, <code>Seeking Alpha</code>, <code>Bloomberg</code> and <code>Reuters</code> based on keyword searches. The library also provides a function to get all Nasdaq-listed stock tickers as well as worldwide stock symbols (these need some cleaning still once retrieved).
</p>

<p>
<i>To do list:</i>
<ul>
<li> Add a section for SEC filings and CIK finder </li>
<li> Add an earnings transcript section </li>
<li> Add EIA and USDA data, CFTC COT and potentially add weather data sources (e.g. heating degree days, cooling degree days in NE USA) </li>
<li> Add social media data (Twitter, Stocktwits, Weibo, Reddit WSB?) </li>
</ul>
</p>

<p>
If there are any issues or recommendations please contact xxx@xxxx.com.
</p>

<br>

## <div id="0">Documentation</div>

<ol>
<li>
<a href="#2">Installation</a>
</li>
<li><a href="#3">Function index</a></li>
<li>
<a href="#4">Company fundamental data</a><ul>
	<li><a href="#A21">Valuation metrics and financial ratios</a></li>
	<li><a href="#A22">Financial statements</a></li>
	<li><a href="#A23">Earnings and revenue estimates</a></li>
	<li><a href = "">Insider transactions and analyst ratings</a></li>
	<li><a href = "">Earnings conference calls</a></li>
	<li><a href = "">ESG data</a></li>
	<li><a href = "">Company profile</a></li>
	</ul>
</li>
<li>
<a href="#5">Price data</a><ul>
	<li><a href="">Stock prices</a></li>
	<li><a href="">Option prices</a></li>
	<li><a href="#A23">Futures prices</a></li>
	</ul>

</li>
<li><a href="#6">Economic data</a></li>
<ul>
<li><a href = "">OECD composite leading indicators</a></li>
<li><a href = "">OECD business tendency survey</a></li>
<li><a href = "">OECD main economic indicators</a></li>
<li><a href = "">OECD balance of payment</a></li>

</ul>
<li><a href="#7">News data</a></li>
<li><a href="#8">Other data</a></li>
<li><a href="#9">Sources</a></li>
</ol>

## <div id="2">Installation</div>

Python3 is required. Pip install is available. Google Chrome version <code>84.\*.\*\*\*\*.\*\*\*</code> or higher required for some functions.

```python
$ pip install jippy
```

<div align="right"><a href="#0">Back to top</a> </div>



## <div id="3"> Index </div>

|Output|Data Output|Runtime|
|:-----|:-----|:-----:|
|<b>Company Fundamentals</b>|||
|<u>Valuation metrics and financial ratios</u>|||
|<li> <a href='#f1'>yahoo.valuation\_metrics()</a> </li>|5 quarters|Fast|
|<li> <a href='#f2'>yahoo.ratios()</a> </li>|Today's data|Fast|
|<u>Financial statements</u>|||
|<li> <a href='#f3'>yahoo.income\_statement()</a> </li>|4 years / quarters|Fast|
|<li> <a href='#f4'>yahoo.balance\_sheet()</a> </li>|4 years / quarters|Fast|
|<li> <a href='#f5'>yahoo.cashflow\_statement()</a> </li>|4 years / quarters|Fast|
|<li> <a href='#f6'>yahoo.statements()</a> </li>|4 years / quarters|Fast|
|<li> <a href='#f7'>mwatch.income\_statement()</a> </li>|5 years / quarters|Fast|
|<li> <a href='#f8'>mwatch.balance\_sheet()</a> </li>|5 years / quarters|Fast|
|<li> <a href='#f9'>mwatch.cashflow\_statement()</a> </li>|5 years / quarters|Fast|
|<li> <a href='#f10'>mwatch.statements()</a> </li>|5 years / quarters|Fast|
|<u>Earnings and revenue estimates</u>|||
|<li> <a href='#f11'>yahoo.earnings\_estimates()</a> </li>|Today's data|Fast|
|<li> <a href='#f12'>yahoo.earnings\_history()</a> </li>|4 quarters|Fast|
|<li> <a href='#f13'>yahoo.revenue\_estimates()</a> </li>|Today's data|Fast|
|<li> <a href='#f14'>yahoo.growth\_estimates()</a> </li>|Today's data|Fast|
|<u>Insider transactions and analyst ratings</u>|||
|<li> <a href='#f15'>finviz.insider\_transactions()</a> </li>|Last year|Fast|
|<li> <a href='#f16'>finviz.analyst\_ratings()</a> </li>|Most recent ratings|Fast|
|<u>ESG data</u>|||
|<li> <a href='#f17'>yahoo.esg\_score()</a> </li>|Today's data|Fast|
|<li> <a href='#f18'>yahoo.corporate\_governance\_score()</a> </li>|Today's data|Fast|
|<u>Company profile</u>|||
|<li> <a href='#f19'>yahoo.profile()</a> </li>|Today's data|Fast|
|<li> <a href='#f20'>yahoo.exceutives\_info()</a> </li>|Today's data|Fast|
|<b>Price data</b>|||
|<li> <a href='#f21'>yahoo\_prices(ticker)</a> </li>|Timeseries|Slow|
|<li> <a href='#f22'>investing\_com\_prices(url)</a> </li>|Timeseries|Slow|
|<li> <a href='#f23'>alpha\_vantage\_prices(ticker,api\_token)</a> </li>|Timeseries|Fast|
|<li> <a href='#f24'>iex_intraday(ticker, api\_token)</a> </li>|Timeseries|Depends on timeframe|
|<li> <a href='#f25'>tingo\_prices(ticker, api\_token, start\_date, end\_date, freq)</a> </li>|Timeseries|Depends on timeframe|
|<li> <a href='#f26'>yahoo\_option\_chain(ticker)</a> </li>|Today's data|Slow|
|<li> <a href='#f27'>futures\_historical\_prices(date\_range)</a> </li>|Timeseries|Very slow|
|<li> <a href='#f28'>futures\_prices(date)</a> </li>|Any date|Fast|
|<b>Economic data</b>|||
|<u>Composite leading indicators</u>|||
|<li> <a href='#f29'>oecd.cli(subject = 'amplitude)</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f30'>oecd.cci()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f31'>oecd.bci()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<u>Financial indicators</u>|||
|<li> <a href='#f32'>oecd.monetary\_aggregates\_m1()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f33'>oecd.monetary\_aggregates\_m3()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f34'>oecd.interbank\_rates()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f35'>oecd.short\_term\_rates()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f36'>oecd.long\_term\_rates()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f37'>oecd.all\_share\_prices( )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f38'>oecd.share\_prices\_industrials()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f39'>oecd.share\_prices\_industrials()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f40'>oecd.usd\_exchange\_rates\_spot()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f41'>oecd.usd\_exchange\_rates\_average( )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f42'>oecd.rer\_overall()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<u>Trade indicators</u>|||
|<li> <a href='#f43'>oecd.exports\_value()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f44'>oecd.imports\_value( )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<b>Labour market indicators</b>|||
|<li> <a href='#f45'>oecd.unemployment\_rate( )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<u>Price indices</u>|||
|<li> <a href='#f46'>oecd.cpi\_total()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f47'>oecd.cpi\_city\_total( )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f48'>oecd.cpi\_non\_food\_non\_energy()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f49'>oecd.cpi\_energy( )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<u>Business tendency and consumer opinion </u>|||
|<li> <a href='#f50'>oecd.business\_tendency\_survey( sector )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f51'>oecd.consumer\_opinion\_survey( measure = ‘national' )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<u>National accounts </u>|||
|<li> <a href='#f52'>oecd.gdp\_deflator()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f53'>oecd.gdp\_total()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f54'>oecd.gdp\_final\_consumption()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f55'>oecd.gdp\_government\_consumption()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f56'>oecd.gdp\_fixed\_capital\_formation()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f57'>oecd.gdp\_exports()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f58'>oecd.gdp\_imports()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<u>Production and sales </u>|||
|<li> <a href='#f59'>oecd.total\_manufacturing\_index()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f60'>oecd.total\_industry\_production\_ex\_construction()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f61'>oecd.total\_construction()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f62'>oecd.total\_retail\_trade()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f63'>oecd.passenger\_car\_registration()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f64'>oecd.construction\_permits\_issued()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<u>OECD Business Tendency Survey </u>|||
|<li> <a href='#f65'>oecd.business\_tendency\_survey(sector)</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f66'>oecd.consumer\_opinion\_survey( measure = ‘national' )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<u>OECD Balance of Payments </u>|||
|<i>Current Account</i>|||
|<li> <a href='#f67'>oecd.current\_account(percent\_of\_gdp = False)</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f68'>oecd.goods\_balance( xm = ‘balance’ )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f69'>oecd.services\_balance( xm = ‘balance’ )</a> </li>|Timeseries|Not slow, depends on # of countries|
|<i>Financial account</i>|||
|<li> <a href='#f70'>oecd.financial\_account(assets\_or\_liabs = None)</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f71'>oecd.direct\_investment(assets\_or\_liabs = None)</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f72'>oecd.portfolio\_investment(assets\_or\_liabs = None)</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f73'>oecd.other\_investment(assets\_or\_liabs = None)</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f74'>oecd.financial\_derivatives()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<li> <a href='#f75'>oecd.reserve\_assets()</a> </li>|Timeseries|Not slow, depends on # of countries|
|<b>News data</b>|||
|<li> <a href='#f76'>news.barrons()</a> </li>|Timeseries|Not that slow|
|<li> <a href='#f77'>news.bloomberg()</a> </li>|Timeseries|Very slow|
|<li> <a href='#f78'>news.cnbc(datestop = False)</a> </li>|Timeseries|Very slow|
|<li> <a href='#f79'>news.ft()</a> </li>|Timeseries|Slow|
|<li> <a href='#f80'>news.nyt()</a> </li>|Timeseries|Slow|
|<li> <a href='#f81'>news.reuters()</a> </li>|Timeseries|Very slow|
|<li> <a href='#f82'>news.seeking\_alpha()</a> </li>|Timeseries|Not that slow|
|<li> <a href='#f83'>news.wsj()</a> </li>|Timeseries|Slow|
|<b>Other data</b>|||
|<li> <a href='#f84'>nasdaq\_tickers()</a> </li>|List of stock tickers|Fast|
|<li> <a href='#f85'>global\_tickers()</a> </li>|List of stock tickers|Very slow|

-----

<br>

## <div id="4"> Company Fundamental data</a>

<div align="right"><a href="#0">Back to top</a> </div>





```python
# Yahoo financial statements, valuation metrics and earnings estimates
from jippy.fundamental_data.yahoo_fundamentals import *

# Marketwatch financial statements
from jippy.fundamental_data.mwatch_fundamentals import *

# Finviz insider transactions and ratings
from jippy.fundamental_data.insider_transactions_and_ratings import *

# Yahoo ESG data
from jippy.fundamental_data.yahoo_esg import *

# Yahoo company profile
from jippy.fundamental_data.yahoo_profile import *

```

<br>

###	 <div id="A21"> <li> Yahoo valuation metrics and financial ratios <hr style="border:0.5px solid gray"> </hr> </li> </div>




#### <div id="f1"><i>yahooData(ticker).valuation\_metrics()</i></div>

<ul>
<li>Returns a dataframe with valuation metrics for the last five quarters and for the current date including trailing P/E, PEG ratio, P/S, etc.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.valuation_metrics()
```

<i> Output </i>

<center><small><small>

|    | date                  |   market\_cap\_(intraday) |   forward\_pe |   peg\_ratio\_(5\_yr\_expected) |   pricesales\_(ttm) |   pricebook\_(mrq) |   ... |
|---:|:----------------------|------------------------:|-------------:|----------------------------:|-------------------:|------------------:|--------------:|
|  1 | As of Date: 8/23/2020 |              2.02e+12   |        30.12 |                        2.4  |               7.66 |             27.98 |         ... |
|  2 | 6/30/2020             |              1.56e+12   |        24.33 |                        2.02 |               6.12 |             19.93 |         ... |
|  3 | 3/31/2020             |              1.1e+12    |        19.65 |                        1.58 |               4.34 |             12.28 |         ... |
|  4 | 12/31/2019            |              1.29e+12   |        22.17 |                        2.03 |               5.25 |             14.23 |         ...  |
|  5 | 9/30/2019             |              9.9515e+11 |        17.27 |                        2.04 |               4.09 |             10.32 |         ... |
|  6 | 6/30/2019             |              9.1064e+11 |        15.97 |                        1.45 |               3.68 |              8.47 |         ... |



</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>yahooData(ticker).ratios()</i>

<ul>
<li>Returns a dataframe with current key statistics and financial ratios.</li>
</ul>

<i> Example </i>

```python
yahoo_ratios('AAPL')
```

<i> Output </i>

<center><small><small>

|    |   payout\_ratio |   profit\_margin |   operating\_margin\_(ttm) |   return\_on\_assets\_(ttm) |   return\_on\_equity\_(ttm) |   ...|
|---:|---------------:|----------------:|-------------------------:|-------------------------:|-------------------------:|----------------:|
|  0 |         0.2373 |          0.2133 |                   0.2452 |                   0.1312 |                   0.6925 |      ... |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>


###	 <div id="A21"> <li> MarketWatch financial statements <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>


#### <i>mwatchData(ticker).income\_statement( freq = 'annual' )</i>

<i>Arguments:</i>
	<code>freq = 'annual'/'a' or 'quarterly'/'q' </code>

<ul>
<li><code>freq = 'annual'</code>: Returns annual income statement for the past 5 years.</li>
<li><code>freq = 'quarterly'</code>: Returns quarterly income statement for the past 5 quarters.</li>
</ul>

<i> Example </i>

```python
mwatch = mwatchData('AAPL')
mwatch.income_statement('q')
```
<i> Output </i>
<center><small><small>

| date        |   sales\_revenue |   sales\_growth |   cost\_of\_goods\_sold\_(cogs)\_incl_danda |   cogs\_excluding\_danda |   depreciation\_and\_amortization\_expense |   ... |
|:------------|----------------:|---------------:|---------------------------------------:|-----------------------:|----------------------------------------:|---------------:|
| 30-Jun-2019 |       5.374e+10 |       nan      |                              3.357e+10 |              3.064e+10 |                                2.93e+09 |       ... |
| 30-Sep-2019 |       6.394e+10 |         0.1897 |                              3.977e+10 |              3.784e+10 |                                1.93e+09 |       ... |
| 31-Dec-2019 |       9.172e+10 |         0.4346 |                              5.677e+10 |              5.396e+10 |                                2.82e+09 |       ... |
| 31-Mar-2020 |       5.835e+10 |        -0.3639 |                              3.593e+10 |              3.315e+10 |                                2.79e+09 |      ... |
| 30-Jun-2020 |       5.942e+10 |         0.0183 |                              3.737e+10 |              3.462e+10 |                                2.75e+09 |      ... |


</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>mwatchData(ticker).balance\_sheet( freq = 'annual' )</i>

<i>Arguments:</i>
	<code>freq = 'annual'/'a' or 'quarterly'/'q' </code> 
<ul><li><code>freq = 'annual'</code>: Returns annual balance sheet for the past 5 years.</li><li><code>freq = 'quarterly'</code>: Returns quarterly balance sheet for the past 5 quarters.</li>
</ul>

<i> Example </i>

```python
mwatch = mwatchData('AAPL')
mwatch.balance_sheet('q')
```
<i> Output </i>
<center><small><small>

| date        |   cash\_and\_short\_term\_investments |   cash\_only |   short-term\_investments |   cash\_and\_short\_term\_investments\_growth |   ... |
|:------------|----------------------------------:|------------:|-------------------------:|-----------------------------------------:|-----------------------------------------:|
| 30-Jun-2019 |                        9.488e+10  |   2.29e+10  |                      nan |                                 nan      |                                   ... |
| 30-Sep-2019 |                        1.0058e+11 |   2.812e+10 |                      nan |                                   0.0601 |                                   ... |
| 31-Dec-2019 |                        1.0723e+11 |   2.299e+10 |                      nan |                                   0.0661 |                                   ... |
| 31-Mar-2020 |                        9.513e+10  |   2.996e+10 |                      nan |                                  -0.1129 |                                   ... |
| 30-Jun-2020 |                        9.305e+10  |   2.73e+10  |                      nan |                                  -0.0218 |                                   ... |




</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>mwatchData(ticker).cashflow\_statement( freq = 'annual' )</i>

<i>Arguments:</i>
	<code>freq = 'annual'/'a' or 'quarterly'/'q' </code> 
	
<ul>
<li><code>freq = 'annual'</code>: Returns annual cashflow statement for the past 5 years.</li>
<li><code>freq = 'quarterly'</code>: Returns quarterly cashflow statement for the past 5 quarters.</li>
</ul>


<i> Example: </i>

```python
mwatch = mwatchData('AAPL')
mwatch.cashflow_statement('q')
```

<i> Output: </i>
<center><small><small>

| date        |   net\_income\_before\_extraordinaries |   net\_income\_growth |   depreciation\_depletion\_and\_amortization |   depreciation\_and\_depletion |   ... |
|:------------|------------------------------------:|--------------------:|-------------------------------------------:|-----------------------------:|------------------------------------:|
| 30-Jun-2019 |                           1.004e+10 |            nan      |                                   2.93e+09 |                     2.93e+09 |                                 ... |
| 30-Sep-2019 |                           1.369e+10 |              0.3626 |                                   3.18e+09 |                     3.18e+09 |                                 ... |
| 31-Dec-2019 |                           2.224e+10 |              0.6247 |                                   2.82e+09 |                     2.82e+09 |                                 ... |
| 31-Mar-2020 |                           1.125e+10 |             -0.4941 |                                   2.79e+09 |                     2.79e+09 |                                 ... |
| 30-Jun-2020 |                           1.125e+10 |              0.0004 |                                   2.75e+09 |                     2.75e+09 |                                 ... |


</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>mwatchData(ticker).statements( freq = 'annual' )</i>

<ul>
<li>Returns <code>mwatchData(ticker).income_statement(freq = 'annual')</code>, <code>mwatchData(ticker).balance_sheet(freq = 'annual')</code> and <code>mwatchData(ticker).cashflow_statement(freq = 'annual')</code> for the given company.</li>
</ul> 

<div align="right"> <a href="#F2">To index</a> </div>


<br>


###	 <div id="A21"> <li> Yahoo financial statements <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>

#### <i>yahooData( ticker ).income\_statement()</i>

<ul>
<li>Returns annual income statement for the past 4 years.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.income_statement()
```

<i> Output </i>

<center><small><small>

|    | breakdown   |   total\_revenue |   cost\_of\_revenue |   gross\_profit |   operating\_expense |   operating\_income |   ... |
|---:|:------------|----------------:|------------------:|---------------:|--------------------:|-------------------:|--------------------------------------------:|
|  0 | ttm         |       273857000 |         169277000 |      104580000 |            37442000 |           67138000 |                                     ... |
|  1 | 9/30/2019   |       260174000 |         161782000 |       98392000 |            34462000 |           63930000 |                                     ... |
|  2 | 9/30/2018   |       265595000 |         163756000 |      101839000 |            30941000 |           70898000 |                                     ... |
|  3 | 9/30/2017   |       229234000 |         141048000 |       88186000 |            26842000 |           61344000 |                                     ... |
|  4 | 9/30/2016   |       215639000 |         131376000 |       84263000 |            24239000 |           60024000 |                                     ... |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>yahooData( ticker ).balance\_sheet()</i>

<ul>
<li>Returns annual balance sheet for the past 4 years.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.balance_sheet()
```

<i> Output </i>

<center><small><small>

|    | breakdown   |   total\_assets |   total\_liabilities\_net\_minority\_interest |   total\_equity\_gross\_minority\_interest |   total\_capitalization |   ... |
|---:|:------------|---------------:|------------------------------------------:|---------------------------------------:|-----------------------:|----------------------:|
|  0 | 9/30/2019   |      338516000 |                                 248028000 |                               90488000 |              182295000 |              ... |
|  1 | 9/30/2018   |      365725000 |                                 258578000 |                              107147000 |              200882000 |             ... |
|  2 | 9/30/2017   |      375319000 |                                 241272000 |                              134047000 |              231254000 |             ... |
|  3 | 9/30/2016   |      321686000 |                                 193437000 |                              128249000 |              203676000 |             ... |


</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>yahooData( ticker ).cashflow\_statement()</i>

<ul>
<li>Returns annual cashflow statement for the past 4 years.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.cashflow_statement()
```

<i> Output </i>

<center><small><small>

|    | breakdown   |   operating\_cash\_flow |   investing\_cash\_flow |   financing\_cash\_flow |   end\_cash\_position |   ... |
|---:|:------------|----------------------:|----------------------:|----------------------:|--------------------:|------------------------------------:|
|  0 | ttm         |              80008000 |             -10618000 |             -86502000 |            35039000 |                            ... |
|  1 | 9/30/2019   |              69391000 |              45896000 |             -90976000 |            50224000 |                            ... |
|  2 | 9/30/2018   |              77434000 |              16066000 |             -87876000 |            25913000 |                            ... |
|  3 | 9/30/2017   |              63598000 |             -46446000 |             -17347000 |            20289000 |                            ... |
|  4 | 9/30/2016   |              65824000 |             -45977000 |             -20483000 |            20484000 |                            ... |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>yahooData( ticker ).statements()</i>

<ul>
<li>Returns <code>yahooData(ticker).income_statement()</code>, <code>yahooData(ticker).balance_sheet()</code> and <code>yahooData(ticker).cashflow_statement()</code> for the given company.</li>
</ul> 

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>




###	 <div id="A21"> <li>Yahoo Earnings and revenue estimates<hr style="border:0.5px solid gray"> </hr> </li> </div>


<div align="right"><a href="#0">Back to top</a> </div>

#### <i>yahooData( ticker ).earnings\_estimates()</i>

<ul>
<li>Returns current earnings estimates for the current quarter, next quarter, current year and the next year.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.earnings_estimates('AAPL')
```

<i> Output </i>
<center><small><small>

|    | date                    |   no\_of\_analysts |   avg\_estimate |   low\_estimate |   high\_estimate |   year\_ago\_eps |
|---:|:------------------------|------------------:|----------------:|---------------:|----------------:|---------------:|
|  1 | Current Qtr. (Sep 2020) |                28 |            2.8  |           2.18 |            3.19 |           3.03 |
|  2 | Next Qtr. (Dec 2020)    |                24 |            5.45 |           4.76 |            6.82 |           4.99 |
|  3 | Current Year (2020)     |                35 |           12.97 |          12.36 |           13.52 |          11.89 |
|  4 | Next Year (2021)        |                35 |           15.52 |          12.67 |           18    |          12.97 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i> yahooData( ticker ).earnings\_estimate\_trends()</i>

<ul>
<li>Returns earnings estimates for the current quarter, next quarter, current year and the next year for the current date, 7 days ago, 30 days ago, 60 days ago and 90 days ago.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.earnings_estimate_trends()
```

<i> Output </i>

<center><small><small>

|    | date                    |   current\_estimate |   7\_days\_ago |   30\_days\_ago |   60\_days\_ago |   90\_days\_ago |
|---:|:------------------------|-------------------:|-------------:|--------------:|--------------:|--------------:|
|  1 | Current Qtr. (Sep 2020) |               2.8  |         2.84 |          2.79 |          2.82 |          2.8  |
|  2 | Next Qtr. (Dec 2020)    |               5.45 |         5.44 |          5.22 |          5.21 |          5.22 |
|  3 | Current Year (2020)     |              12.97 |        13    |         12.41 |         12.39 |         12.32 |
|  4 | Next Year (2021)        |              15.52 |        15.54 |         14.94 |         14.86 |         14.73 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i> yahooData( ticker ).earnings\_history()</i>

<ul>
<li>Returns earnings estimates and actual earnings for the past 4 quarters.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.earnings_history()
```

<i> Output </i>

<center><small><small>

|    | date       |   eps\_est |   eps\_actual |   difference |   surprise\_% |
|---:|:-----------|-----------:|-------------:|-------------:|-------------:|
|  1 | 9/29/2019  |       2.84 |         3.03 |         0.19 |        0.067 |
|  2 | 12/30/2019 |       4.55 |         4.99 |         0.44 |        0.097 |
|  3 | 3/30/2020  |       2.26 |         2.55 |         0.29 |        0.128 |
|  4 | 6/29/2020  |       2.04 |         2.58 |         0.54 |        0.265 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i> yahooData(ticker)._revenue\_estimates()</i>

<ul>
<li>Returns revenue estimates for the current quarter, next quarter, current year and the next year.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.revenue_estimates()
```

<i> Output </i>

<center><small><small>

|    | date                    |   no\_of\_analysts |   avg\_estimate |   low\_estimate |   high\_estimate |   year\_ago\_sales |   sales\_growth\_(yearest) |
|---:|:------------------------|------------------:|----------------:|---------------:|----------------:|-----------------:|-------------------------:|
|  1 | Current Qtr. (Sep 2020) |                26 |      6.351e+10  |     5.255e+10  |      6.85e+10   |       6.404e+10  |                   -0.008 |
|  2 | Next Qtr. (Dec 2020)    |                24 |      1.0036e+11 |     8.992e+10  |      1.157e+11  |       8.85e+10   |                    0.134 |
|  3 | Current Year (2020)     |                33 |      2.7338e+11 |     2.6236e+11 |      2.8089e+11 |       2.6017e+11 |                    0.051 |
|  4 | Next Year (2021)        |                33 |      3.0734e+11 |     2.7268e+11 |      3.3153e+11 |       2.7338e+11 |                    0.124 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i> yahooData( ticker ).growth\_estimates()</i>

<ul>
<li>Returns earnings estimates and actual earnings for the past 4 quarters.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.growth_estimates()
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

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

###	 <div id="A21"> <li> Finviz insider transactions and analyst ratings <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>


#### <i> finvizData( ticker ).insider\_transactions()</i>

<ul>
<li>Returns company insider transactions for the past year.</li>
</ul>

<i> Example </i>

```python
finviz = finvizData('AAPL')
finviz.insider_transactions()
```

<i> Output </i>

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

<div align="right"> <a href="#F2">To index</a> </div>

-----

#### <i> finvizData( ticker ).analyst\_ratings()</i>

<ul>
<li>Returns recent history of analyst ratings.</li>
</ul>

<i> Example </i>

```python
finviz = finvizData('AAPL')
finviz.analyst_ratings()
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

<div align="right"> <a href="#F2">To index</a> </div>

-----

<br>

###	 <div id="A21"> <li> Earnings conference calls <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>



<div align="right"> <a href="#F2">To index</a> </div>

-----

<br>

###	 <div id="A21"> <li> Yahoo ESG data<hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>

<br>


```python
from jippy.esg.yahoo_esg import *
```

<br>

----


#### <i>yahooData( ticker ).esg\_score()</i>

<ul>
<li>Returns current ESG scores from XXXX published on Yahoo Finance.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.esg_score()
```

<i> Output </i>

<center><small><small>

|    | date       |   total\_esg\_risk_score | risk\_category   | risk\_percentile   |   environment\_risk_score |   social\_risk\_score |   ... |
|---:|:-----------|-----------------------:|:----------------|:------------------|-------------------------:|--------------------:|------------------------:|
|  0 | 2020-08-25 |                     24 | Medium          | 33rd              |                      0.5 |                  13 |                    ... | 

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

----

#### <i>yahooData( ticker ).corporate\_governance\_score()</i>

<ul>
<li>Returns current corporate governance scores from XXXX published on Yahoo Finance.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.corporate_governance_score()
```

<i> Output </i>

<center><small><small>

|    |   audit |   board |   shareholder\_rights |   compensation |   quality\_score | ticker   | date       |
|---:|--------:|--------:|---------------------:|---------------:|----------------:|:---------|:-----------|
|  0 |       1 |       1 |                    1 |              3 |               1 | AAPL     | 2020-08-25 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

----

<br>


###	 <div id="A21"> <li> Yahoo company info<hr style="border:0.5px solid gray"> </hr> </li> </div>


<div align="right"><a href="#0">Back to top</a> </div>


#### <i>yahooData( ticker ).profile()</i>

<ul>
<li>Returns company sector, industry, current number of employees and a company description.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.profile()
```

<i> Output </i>

<center><small><small>

|    | company\_name   | sector     | industry             |   number\_of\_employees | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ticker   |
|---:|:---------------|:-----------|:---------------------|----------------------:|:----------|:---------|
|  0 | Apple Inc.     | Technology | Consumer Electronics |                137000 | Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide...  | AAPL     |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>yahooData( ticker ).executives_info()</i>

<ul>
<li>Returns current company executives with name, title, salary, age and their gender.</li>
</ul>

<i> Example </i>

```python
yahoo = yahooData('AAPL')
yahoo.executives_info()
```

<i> Output </i>


<center><small><small>

|    | name                    | title                       |       pay |   exercised |   year\_born | gender   |   age\_at\_end\_of\_year |
|---:|:------------------------|:----------------------------|----------:|------------:|------------:|:---------|---------------------:|
|  0 | Mr. Timothy D. Cook     | CEO & Director              | 1.156e+07 |         nan |        1961 | male     |                   59 |
|  1 | Mr. Luca Maestri        | CFO & Sr. VP                | 3.58e+06  |         nan |        1964 | male     |                   56 |
|  2 | Mr. Jeffrey E. Williams | Chief Operating Officer     | 3.57e+06  |         nan |        1964 | male     |                   56 |
|  3 | Ms. Katherine L. Adams  | Sr. VP, Gen. Counsel & Sec. | 3.6e+06   |         nan |        1964 | female   |                   56 |
|  4 | Ms. Deirdre O'Brien     | Sr. VP of People & Retail   | 2.69e+06  |         nan |        1967 | female   |                   53 |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

## <div id="5"> Price data </div>

<div align="right"><a href="#0">Back to top</a> </div>


###	 <div id="A21"> <li> Stock and ETF prices <hr style="border:0.5px solid gray"> </hr> </li> </div>

```python
from jippy.price_data.yahoo_price_data import *
```

#### <i>yahoo\_prices( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
yahoo_prices('AAPL')
```

<i> Output </i>

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

<div align="right"> <a href="#F2">To index</a> </div>

----

#### <i>investing\_com\_prices( url, start_date = None, end_date = None )</i>

<ul>
<li></li>
<li></li>
</ul>

<i> Example </i>

```python
investing_com_prices('https://www.investing.com/etfs/spdr-s-p-500', start_date = '2000-01-01')
```

<i> Output </i>

<center><small><small>

| date                |   price |   open |   high |    low |    volume |
|:--------------------|--------:|-------:|-------:|-------:|----------:|
| 2000-01-03 00:00:00 |  145.44 | 148.25 | 148.25 | 143.88 | 8.16e+06  |
| 2000-01-04 00:00:00 |  139.75 | 143.53 | 144.06 | 139.64 | 8.09e+06  |
| 2000-01-05 00:00:00 |  140    | 139.94 | 141.53 | 137.25 | 1.218e+07 |
| 2000-01-06 00:00:00 |  137.75 | 139.62 | 141.5  | 137.75 | 6.23e+06  |
| 2000-01-07 00:00:00 |  145.75 | 140.31 | 145.75 | 140.06 | 8.07e+06  |
| ...|  ... | ... | ... | ... | ...  |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>


----


#### <i>alpha\_vantage\_prices( ticker, api_token, start_date = None )</i>

<ul>
<li></li>
<li></li>
</ul>

<i> Example </i>

```python
alpha_vantage_prices('AAPL', <api_token>)
```

<i> Output </i>

<center><small><small>

| date                |   open |   high |   low |   close |   adjusted_close |     volume |   dividend_amount |   split_coefficient |
|:--------------------|-------:|-------:|------:|--------:|-----------------:|-----------:|------------------:|--------------------:|
| 1999-11-01 00:00:00 |  80    |  80.69 | 77.37 |   77.62 |           0.5988 | 2.4873e+06 |                 0 |                   1 |
| 1999-11-02 00:00:00 |  78    |  81.69 | 77.31 |   80.25 |           0.6191 | 3.5646e+06 |                 0 |                   1 |
| 1999-11-03 00:00:00 |  81.62 |  83.25 | 81    |   81.5  |           0.6287 | 2.9327e+06 |                 0 |                   1 |
| 1999-11-04 00:00:00 |  82.06 |  85.37 | 80.62 |   83.62 |           0.6451 | 3.3847e+06 |                 0 |                   1 |
| 1999-11-05 00:00:00 |  84.62 |  88.37 | 84    |   88.31 |           0.6813 | 3.7215e+06 |                 0 |                   1 |
| ... |  ... |  ... | ...    |   ... |           ... | ... |                 ... |                   ... |

</small></small></center>


<div align="right"> <a href="#F2">To index</a> </div>

------

#### <i>iex\_intraday( ticker, api\_token, start\_date = None, end\_date = None )</i>

<ul>
<li></li>
<li></li>
</ul>


<i> Example </i>

```python
iex_intraday('AAPL', <api_token>)
```

<i> Output </i>

<center><small><small>

|                     | date       | label    |   high |    low |   average |   volume |         notional |   numberOfTrades |   marketHigh |   marketLow |   marketAverage |   marketVolume |   marketNotional |   marketNumberOfTrades |    open |   close |   marketOpen |   marketClose |   changeOverTime |   marketChangeOverTime |
|:--------------------|:-----------|:---------|-------:|-------:|----------:|---------:|-----------------:|-----------------:|-------------:|------------:|----------------:|---------------:|-----------------:|-----------------------:|--------:|--------:|-------------:|--------------:|-----------------:|-----------------------:|
| 2019-04-02 15:59:00 | 2019-04-02 | 3:59 PM  | 286.07 | 285.94 |   286.021 |    20335 |      5.81624e+06 |              118 |       286.08 |     285.93  |         286.01  |         848987 |      2.42818e+08 |                   3245 | 286.07  |  285.94 |      286.07  |        285.98 |      0.000132875 |           -2.09778e-05 |
| 2019-04-02 11:33:00 | 2019-04-02 | 11:33 AM | 285.65 | 285.64 |   285.64  |      618 | 176526           |                6 |       285.66 |     285.625 |         285.644 |          69117 |      1.97429e+07 |                    330 | 285.64  |  285.64 |      285.65  |        285.65 |     -0.00119937  |           -0.00130063  |
| 2019-04-02 11:34:00 | 2019-04-02 | 11:34 AM | 285.66 | 285.59 |   285.643 |     1303 | 372193           |               15 |       285.67 |     285.59  |         285.646 |          78564 |      2.24415e+07 |                    375 | 285.655 |  285.59 |      285.65  |        285.6  |     -0.00118888  |           -0.00129363  |
| 2019-04-02 11:35:00 | 2019-04-02 | 11:35 AM | 285.62 | 285.56 |   285.599 |      755 | 215627           |                9 |       285.63 |     285.55  |         285.583 |          76670 |      2.18956e+07 |                    466 | 285.62  |  285.56 |      285.6   |        285.55 |     -0.00134274  |           -0.0015139   |
| 2019-04-02 11:36:00 | 2019-04-02 | 11:36 AM | 285.53 | 285.49 |   285.512 |      784 | 223841           |               12 |       285.56 |     285.48  |         285.506 |          80973 |      2.31183e+07 |                    412 | 285.525 |  285.52 |      285.555 |        285.52 |     -0.00164695  |           -0.00178312  |
| ... | ... | ... | ... | ... |   ... |      ... | ...           |               ... |       ... |    ...  |         ... |          ... |      ... |                    ... | ... | ... |      ... |        ... |     ...  |           ...  |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>



-----


#### <i>tingo\_prices( ticker, api\_token, start\_date = None, end\_date = None, freq = '1min' )</i>

<ul>
<li></li>
<li></li>
</ul>

<i> Example </i>

```python
tingo_prices('AAPL', <api_key>)
```

<i> Output </i>

<center><small><small>

| date                      |   close |    high |     low |    open |
|:--------------------------|--------:|--------:|--------:|--------:|
| 2017-01-03 14:30:00+00:00 | 115.885 | 115.9   | 115.58  | 115.8   |
| 2017-01-03 14:31:00+00:00 | 116.24  | 116.24  | 115.9   | 115.9   |
| 2017-01-03 14:32:00+00:00 | 116.3   | 116.3   | 116.26  | 116.26  |
| 2017-01-03 14:33:00+00:00 | 116.06  | 116.165 | 116.05  | 116.16  |
| 2017-01-03 14:34:00+00:00 | 116.14  | 116.18  | 116.115 | 116.115 |
| ... | ...  | ...  | ... | ... |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

----

<br>

###	 <div id="A21"> <li> Option prices <hr style="border:0.5px solid gray"> </hr> </li> </div>
<div align="right"><a href="#0">Back to top</a> </div>


#### <i>yahoo\_option_chain( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
calls, puts = yahoo_option_chain('AAPL')
```

<i> Output </i>


<i>Call options chain</i>
<center><small><small>

|    | Contract_Name       | Last\_Trade\_Date        |   Strike |   Last\_Price |   ... |
|---:|:--------------------|:-----------------------|---------:|-------------:|------:|
|  0 | AAPL200828C00190000 | 2020-08-25 3:40PM EDT  |      190 |       310.29 |     ... |
|  1 | AAPL200828C00195000 | 2020-08-25 12:36PM EDT |      195 |       300.7  |     ... |
|  2 | AAPL200828C00200000 | 2020-08-25 12:13PM EDT |      200 |       294.8  |     ... |
|  3 | AAPL200828C00205000 | 2020-08-06 3:07PM EDT  |      205 |       249.54 |     ... |
|  ... | ... | ...  |      ... |       ... |     ... |

</small></small></center>

<i>Put options chain</i>
<center><small><small>

|    | Contract_Name       | Last_Trade_Date        |   Strike |   Last_Price |   Bid |
|---:|:--------------------|:-----------------------|---------:|-------------:|------:|
|  0 | AAPL200828P00190000 | 2020-08-24 2:05PM EDT  |      190 |         0.01 |     ... |
|  1 | AAPL200828P00195000 | 2020-08-10 10:38AM EDT |      195 |         0.02 |     ... |
|  2 | AAPL200828P00200000 | 2020-08-24 1:36PM EDT  |      200 |         0.01 |     ... |
|  3 | AAPL200828P00205000 | 2020-08-24 10:08AM EDT |      205 |         0.02 |     ... |
|  ... | ... | ... |      ... |         ... |     ... |

</small></small></center>



<div align="right"> <a href="#F2">To index</a> </div>




###	 <div id="A21"> <li> Futures prices <hr style="border:0.5px solid gray"> </hr> </li> </div>
<div align="right"><a href="#0">Back to top</a> </div>


#### <i>futures\_historical\_prices( date_range )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
futures_historical_prices(pd.date_range('2000-01-01', '2020-01-01'))
```

<i> Output </i>


<center><small><small>

</small></small></center>



<div align="right"> <a href="#F2">To index</a> </div>

----


#### <i>get\_futures\_prices( date )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
get_futures_prices('2020-09-01')
```

<i> Output </i>



<center><small><small>

</small></small></center>



<div align="right"> <a href="#F2">To index</a> </div>

------

## <div id="6">Economic data</div>

<div align="right"><a href="#0">Back to top</a> </div>


<br>


```python
from jippy.economic_data.oecd_data import *
```

<br>


## <li> OECD Composite Leading Indicators </li>

<div align="right"><a href="#0">Back to top</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_cli(country\_code = 'all', subject = 'amplitude')</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_cli(country_code = 'USA', subject = 'amplitude')
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                  | Country       | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-------------------------|:--------------|:------------|:--------|:------------|-----------------:|--------:|
| 1955-01-01 00:00:00 | LOLITOAA  | Amplitude adjusted (CLI) | United States | M           | 1955-01 | IDX         |                0 | 101.484 |
| 1955-02-01 00:00:00 | LOLITOAA  | Amplitude adjusted (CLI) | United States | M           | 1955-02 | IDX         |                0 | 101.838 |
| 1955-03-01 00:00:00 | LOLITOAA  | Amplitude adjusted (CLI) | United States | M           | 1955-03 | IDX         |                0 | 102.131 |
| 1955-04-01 00:00:00 | LOLITOAA  | Amplitude adjusted (CLI) | United States | M           | 1955-04 | IDX         |                0 | 102.337 |
| 1955-05-01 00:00:00 | LOLITOAA  | Amplitude adjusted (CLI) | United States | M           | 1955-05 | IDX         |                0 | 102.454 |
| ... | ...  | ... | ... | ...           | ... | ...         |                ... | ...  |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_cci(country\_code = 'all')</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_cci(country_code = 'USA')
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                               | Country       | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:----------------------------------------------------------------------|:--------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | CSCICP03  | OECD Standardised CCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1960-01 | IDX         |                0 | 101.498 |
| 1960-02-01 00:00:00 | CSCICP03  | OECD Standardised CCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1960-02 | IDX         |                0 | 101.243 |
| 1960-03-01 00:00:00 | CSCICP03  | OECD Standardised CCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1960-03 | IDX         |                0 | 101.023 |
| 1960-04-01 00:00:00 | CSCICP03  | OECD Standardised CCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1960-04 | IDX         |                0 | 100.902 |
| 1960-05-01 00:00:00 | CSCICP03  | OECD Standardised CCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1960-05 | IDX         |                0 | 100.933 |
| ... | ...  | ... | ... | ...           | ... | ...         |                ... | ...  |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_bci(country\_code = 'all')</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_bci(country_code = 'USA')
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                               | Country       | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:----------------------------------------------------------------------|:--------------|:------------|:--------|:------------|-----------------:|--------:|
| 1950-01-01 00:00:00 | BSCICP03  | OECD Standardised BCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1950-01 | IDX         |                0 | 101.071 |
| 1950-02-01 00:00:00 | BSCICP03  | OECD Standardised BCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1950-02 | IDX         |                0 | 101.59  |
| 1950-03-01 00:00:00 | BSCICP03  | OECD Standardised BCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1950-03 | IDX         |                0 | 102.282 |
| 1950-04-01 00:00:00 | BSCICP03  | OECD Standardised BCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1950-04 | IDX         |                0 | 103.267 |
| 1950-05-01 00:00:00 | BSCICP03  | OECD Standardised BCI, Amplitude adjusted (Long term average=100), sa | United States | M           | 1950-05 | IDX         |                0 | 104.26  |
| ... | ...  | ... | ... | ...           | ... | ...         |                ... | ...  |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

## <li> OECD Main Economic Indicators </li>

<div align="right"><a href="#0">Back to top</a> </div>


<br>

### 

###	 <div id=""> <li> Financial indicators <hr style="border:0.5px solid gray"> </hr> </li> </div>
<div align="right"><a href="#0">Back to top</a> </div>


#### <i>monetary\_aggregates\_m1( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
monetary_aggregates_m1( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                                                         | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:------------------------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-06-01 00:00:00 | MANMM101  | Monetary aggregates and their components > Narrow money and components > M1 and components > M1 | Australia | M           | 1960-06 | AUD         |                9 |   3.518 |
| 1960-07-01 00:00:00 | MANMM101  | Monetary aggregates and their components > Narrow money and components > M1 and components > M1 | Australia | M           | 1960-07 | AUD         |                9 |   3.464 |
| 1960-08-01 00:00:00 | MANMM101  | Monetary aggregates and their components > Narrow money and components > M1 and components > M1 | Australia | M           | 1960-08 | AUD         |                9 |   3.459 |
| 1960-09-01 00:00:00 | MANMM101  | Monetary aggregates and their components > Narrow money and components > M1 and components > M1 | Australia | M           | 1960-09 | AUD         |                9 |   3.468 |
| 1960-10-01 00:00:00 | MANMM101  | Monetary aggregates and their components > Narrow money and components > M1 and components > M1 | Australia | M           | 1960-10 | AUD         |                9 |   3.514 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>monetary\_aggregates\_m3( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
monetary_aggregates_m3( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                                         | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:--------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1959-01-01 00:00:00 | MABMM301  | Monetary aggregates and their components > Broad money and components > M3 > M3 | Australia | M           | 1959-01 | AUD         |                9 |   6.608 |
| 1959-02-01 00:00:00 | MABMM301  | Monetary aggregates and their components > Broad money and components > M3 > M3 | Australia | M           | 1959-02 | AUD         |                9 |   6.668 |
| 1959-03-01 00:00:00 | MABMM301  | Monetary aggregates and their components > Broad money and components > M3 > M3 | Australia | M           | 1959-03 | AUD         |                9 |   6.728 |
| 1959-04-01 00:00:00 | MABMM301  | Monetary aggregates and their components > Broad money and components > M3 > M3 | Australia | M           | 1959-04 | AUD         |                9 |   6.696 |
| 1959-05-01 00:00:00 | MABMM301  | Monetary aggregates and their components > Broad money and components > M3 > M3 | Australia | M           | 1959-05 | AUD         |                9 |   6.638 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>interbank\_rates( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
interbank_rates( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                                         | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:--------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1990-08-01 00:00:00 | IRSTCI01  | Interest Rates > Immediate rates (< 24 hrs) > Call money/interbank rate > Total | Australia | M           | 1990-08 | PC          |                0 |   14    |
| 1990-09-01 00:00:00 | IRSTCI01  | Interest Rates > Immediate rates (< 24 hrs) > Call money/interbank rate > Total | Australia | M           | 1990-09 | PC          |                0 |   14    |
| 1990-10-01 00:00:00 | IRSTCI01  | Interest Rates > Immediate rates (< 24 hrs) > Call money/interbank rate > Total | Australia | M           | 1990-10 | PC          |                0 |   13.43 |
| 1990-11-01 00:00:00 | IRSTCI01  | Interest Rates > Immediate rates (< 24 hrs) > Call money/interbank rate > Total | Australia | M           | 1990-11 | PC          |                0 |   13    |
| 1990-12-01 00:00:00 | IRSTCI01  | Interest Rates > Immediate rates (< 24 hrs) > Call money/interbank rate > Total | Australia | M           | 1990-12 | PC          |                0 |   12.58 |'
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>short\_term\_rates( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
short_term_rates( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                                  | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1968-01-01 00:00:00 | IR3TBB01  | Interest Rates > 3-month or 90-day rates and yields > Bank bills > Total | Australia | M           | 1968-01 | PC          |                0 |    5.1  |
| 1968-02-01 00:00:00 | IR3TBB01  | Interest Rates > 3-month or 90-day rates and yields > Bank bills > Total | Australia | M           | 1968-02 | PC          |                0 |    5.15 |
| 1968-03-01 00:00:00 | IR3TBB01  | Interest Rates > 3-month or 90-day rates and yields > Bank bills > Total | Australia | M           | 1968-03 | PC          |                0 |    5.15 |
| 1968-04-01 00:00:00 | IR3TBB01  | Interest Rates > 3-month or 90-day rates and yields > Bank bills > Total | Australia | M           | 1968-04 | PC          |                0 |    5.15 |
| 1968-05-01 00:00:00 | IR3TBB01  | Interest Rates > 3-month or 90-day rates and yields > Bank bills > Total | Australia | M           | 1968-05 | PC          |                0 |    5.3  |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>long\_term\_rates( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
long_term_rates( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                                                  | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-----------------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1969-07-01 00:00:00 | IRLTLT01  | Interest Rates > Long-term government bond yields > 10-year > Main (including benchmark) | Australia | M           | 1969-07 | PC          |                0 |    5.8  |
| 1969-08-01 00:00:00 | IRLTLT01  | Interest Rates > Long-term government bond yields > 10-year > Main (including benchmark) | Australia | M           | 1969-08 | PC          |                0 |    5.79 |
| 1969-09-01 00:00:00 | IRLTLT01  | Interest Rates > Long-term government bond yields > 10-year > Main (including benchmark) | Australia | M           | 1969-09 | PC          |                0 |    5.81 |
| 1969-10-01 00:00:00 | IRLTLT01  | Interest Rates > Long-term government bond yields > 10-year > Main (including benchmark) | Australia | M           | 1969-10 | PC          |                0 |    5.83 |
| 1969-11-01 00:00:00 | IRLTLT01  | Interest Rates > Long-term government bond yields > 10-year > Main (including benchmark) | Australia | M           | 1969-11 | PC          |                0 |    5.85 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>


_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>all\_share\_prices( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
all_share_prices( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                         | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1958-01-01 00:00:00 | SPASTT01  | Share Prices > All shares/broad > Total > Total | Australia | M           | 1958-01 | IDX         |                0 | 2.46886 |
| 1958-02-01 00:00:00 | SPASTT01  | Share Prices > All shares/broad > Total > Total | Australia | M           | 1958-02 | IDX         |                0 | 2.55808 |
| 1958-03-01 00:00:00 | SPASTT01  | Share Prices > All shares/broad > Total > Total | Australia | M           | 1958-03 | IDX         |                0 | 2.56718 |
| 1958-04-01 00:00:00 | SPASTT01  | Share Prices > All shares/broad > Total > Total | Australia | M           | 1958-04 | IDX         |                0 | 2.55626 |
| 1958-05-01 00:00:00 | SPASTT01  | Share Prices > All shares/broad > Total > Total | Australia | M           | 1958-05 | IDX         |                0 | 2.50163 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>share\_prices\_industrials( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
share_prices_industrials( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                    | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1955-01-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-01 | IDX         |                0 | 2.38957 |
| 1955-02-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-02 | IDX         |                0 | 2.29226 |
| 1955-03-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-03 | IDX         |                0 | 2.34632 |
| 1955-04-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-04 | IDX         |                0 | 2.36795 |
| 1955-05-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-05 | IDX         |                0 | 2.27063 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>share\_prices\_industrials( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
share_prices_industrials( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                    | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1955-01-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-01 | IDX         |                0 | 2.38957 |
| 1955-02-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-02 | IDX         |                0 | 2.29226 |
| 1955-03-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-03 | IDX         |                0 | 2.34632 |
| 1955-04-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-04 | IDX         |                0 | 2.36795 |
| 1955-05-01 00:00:00 | SPINTT01  | Share Prices > Industrials > Total > Total | Norway    | M           | 1955-05 | IDX         |                0 | 2.27063 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>usd\_exchange\_rates\_spot( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
usd_exchange_rates_spot( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>



| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>usd\_exchange\_rates\_average( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
usd_exchange_rates_average( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                                                   | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |    Value |
|:--------------------|:----------|:------------------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|---------:|
| 1957-01-01 00:00:00 | CCUSMA02  | Currency Conversions > US$ exchange rate > Average of daily rates > National currency:USD | Australia | M           | 1957-01 | AUD         |                0 | 0.598516 |
| 1957-02-01 00:00:00 | CCUSMA02  | Currency Conversions > US$ exchange rate > Average of daily rates > National currency:USD | Australia | M           | 1957-02 | AUD         |                0 | 0.598015 |
| 1957-03-01 00:00:00 | CCUSMA02  | Currency Conversions > US$ exchange rate > Average of daily rates > National currency:USD | Australia | M           | 1957-03 | AUD         |                0 | 0.599125 |
| 1957-04-01 00:00:00 | CCUSMA02  | Currency Conversions > US$ exchange rate > Average of daily rates > National currency:USD | Australia | M           | 1957-04 | AUD         |                0 | 0.599988 |
| 1957-05-01 00:00:00 | CCUSMA02  | Currency Conversions > US$ exchange rate > Average of daily rates > National currency:USD | Australia | M           | 1957-05 | AUD         |                0 | 0.599556 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>rer\_overall( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
rer_overall( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                                      | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-----------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1972-01-01 00:00:00 | CCRETT01  | Currency Conversions > Real effective exchange rates > Overall Economy > CPI | Australia | M           | 1972-01 | IDX         |                0 | 110.762 |
| 1972-02-01 00:00:00 | CCRETT01  | Currency Conversions > Real effective exchange rates > Overall Economy > CPI | Australia | M           | 1972-02 | IDX         |                0 | 109.613 |
| 1972-03-01 00:00:00 | CCRETT01  | Currency Conversions > Real effective exchange rates > Overall Economy > CPI | Australia | M           | 1972-03 | IDX         |                0 | 108.894 |
| 1972-04-01 00:00:00 | CCRETT01  | Currency Conversions > Real effective exchange rates > Overall Economy > CPI | Australia | M           | 1972-04 | IDX         |                0 | 109.391 |
| 1972-05-01 00:00:00 | CCRETT01  | Currency Conversions > Real effective exchange rates > Overall Economy > CPI | Australia | M           | 1972-05 | IDX         |                0 | 108.884 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>



<br>

###	 <div id=""> <li> Trade indicators <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>


#### <i>exports\_value( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
exports_value( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                               | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1955-01-01 00:00:00 | XTEXVA01  | International Trade > Exports > Value (goods) > Total | Australia | M           | 1955-01 | AUD         |                9 |  0.1287 |
| 1955-02-01 00:00:00 | XTEXVA01  | International Trade > Exports > Value (goods) > Total | Australia | M           | 1955-02 | AUD         |                9 |  0.1358 |
| 1955-03-01 00:00:00 | XTEXVA01  | International Trade > Exports > Value (goods) > Total | Australia | M           | 1955-03 | AUD         |                9 |  0.1642 |
| 1955-04-01 00:00:00 | XTEXVA01  | International Trade > Exports > Value (goods) > Total | Australia | M           | 1955-04 | AUD         |                9 |  0.1164 |
| 1955-05-01 00:00:00 | XTEXVA01  | International Trade > Exports > Value (goods) > Total | Australia | M           | 1955-05 | AUD         |                9 |  0.1368 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>imports\_value( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
exports_value( country_code = 'all', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                               | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1955-01-01 00:00:00 | XTIMVA01  | International Trade > Imports > Value (goods) > Total | Australia | M           | 1955-01 | AUD         |                9 |  0.1495 |
| 1955-02-01 00:00:00 | XTIMVA01  | International Trade > Imports > Value (goods) > Total | Australia | M           | 1955-02 | AUD         |                9 |  0.1367 |
| 1955-03-01 00:00:00 | XTIMVA01  | International Trade > Imports > Value (goods) > Total | Australia | M           | 1955-03 | AUD         |                9 |  0.152  |
| 1955-04-01 00:00:00 | XTIMVA01  | International Trade > Imports > Value (goods) > Total | Australia | M           | 1955-04 | AUD         |                9 |  0.1444 |
| 1955-05-01 00:00:00 | XTIMVA01  | International Trade > Imports > Value (goods) > Total | Australia | M           | 1955-05 | AUD         |                9 |  0.1547 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>


_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


<br>

###	 <div id=""> <li> Labour market indicators <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>


#### <i>unemployment\_rate( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
unemployment_rate( country_code = 'all', freq = 'M' )
```

<i> Output </i>

<center><small><small>

| TIME                | SUBJECT   | Subject                                                                                               | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:------------------------------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1978-02-01 00:00:00 | LRHUTTTT  | Labour Force Survey - quarterly rates > Harmonised unemployment - monthly rates > Total > All persons | Australia | M           | 1978-02 | PC          |                0 | 6.64535 |
| 1978-03-01 00:00:00 | LRHUTTTT  | Labour Force Survey - quarterly rates > Harmonised unemployment - monthly rates > Total > All persons | Australia | M           | 1978-03 | PC          |                0 | 6.30344 |
| 1978-04-01 00:00:00 | LRHUTTTT  | Labour Force Survey - quarterly rates > Harmonised unemployment - monthly rates > Total > All persons | Australia | M           | 1978-04 | PC          |                0 | 6.26811 |
| 1978-05-01 00:00:00 | LRHUTTTT  | Labour Force Survey - quarterly rates > Harmonised unemployment - monthly rates > Total > All persons | Australia | M           | 1978-05 | PC          |                0 | 6.21017 |
| 1978-06-01 00:00:00 | LRHUTTTT  | Labour Force Survey - quarterly rates > Harmonised unemployment - monthly rates > Total > All persons | Australia | M           | 1978-06 | PC          |                0 | 6.30418 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


<br>

###	 <div id=""> <li> Price indices <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>

#### <i>cpi\_total( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
unemployment_rate( country_code = 'all', freq = 'M' )
```

<i> Output </i>

<center><small><small>


| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>cpi\_city\_total( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
cpi_city_total( country_code = 'all', freq = 'M' )
```

<i> Output </i>

<center><small><small>

| TIME                | SUBJECT   | Subject                                                    | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-----------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1961-01-01 00:00:00 | CPALCY01  | Consumer Price Index > All items > All items: City > Total | Canada    | M           | 1961-01 | IDX         |                0 | 13.4288 |
| 1961-02-01 00:00:00 | CPALCY01  | Consumer Price Index > All items > All items: City > Total | Canada    | M           | 1961-02 | IDX         |                0 | 13.4288 |
| 1961-03-01 00:00:00 | CPALCY01  | Consumer Price Index > All items > All items: City > Total | Canada    | M           | 1961-03 | IDX         |                0 | 13.3779 |
| 1961-04-01 00:00:00 | CPALCY01  | Consumer Price Index > All items > All items: City > Total | Canada    | M           | 1961-04 | IDX         |                0 | 13.3439 |
| 1961-05-01 00:00:00 | CPALCY01  | Consumer Price Index > All items > All items: City > Total | Canada    | M           | 1961-05 | IDX         |                0 | 13.259  |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>cpi\_non\_food\_non_energy( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
cpi_non_food_non_energy( country_code = 'all', freq = 'M' )
```

<i> Output </i>

<center><small><small>

| TIME                | SUBJECT   | Subject                                                                    | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:---------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1966-01-01 00:00:00 | CPGRLE01  | Consumer Price Index > OECD Groups > All items non-food non-energy > Total | Austria   | M           | 1966-01 | IDX         |                0 | 18.3463 |
| 1966-02-01 00:00:00 | CPGRLE01  | Consumer Price Index > OECD Groups > All items non-food non-energy > Total | Austria   | M           | 1966-02 | IDX         |                0 | 18.3966 |
| 1966-03-01 00:00:00 | CPGRLE01  | Consumer Price Index > OECD Groups > All items non-food non-energy > Total | Austria   | M           | 1966-03 | IDX         |                0 | 18.4262 |
| 1966-04-01 00:00:00 | CPGRLE01  | Consumer Price Index > OECD Groups > All items non-food non-energy > Total | Austria   | M           | 1966-04 | IDX         |                0 | 18.4286 |
| 1966-05-01 00:00:00 | CPGRLE01  | Consumer Price Index > OECD Groups > All items non-food non-energy > Total | Austria   | M           | 1966-05 | IDX         |                0 | 18.4671 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>cpi\_energy( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
cpi_energy( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                                                            | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-----------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1966-01-01 00:00:00 | CPGREN01  | Consumer Price Index > OECD Groups > Energy (Fuel, electricity & gasoline) > Total | Austria   | M           | 1966-01 | IDX         |                0 | 17.8956 |
| 1966-02-01 00:00:00 | CPGREN01  | Consumer Price Index > OECD Groups > Energy (Fuel, electricity & gasoline) > Total | Austria   | M           | 1966-02 | IDX         |                0 | 17.9295 |
| 1966-03-01 00:00:00 | CPGREN01  | Consumer Price Index > OECD Groups > Energy (Fuel, electricity & gasoline) > Total | Austria   | M           | 1966-03 | IDX         |                0 | 17.9295 |
| 1966-04-01 00:00:00 | CPGREN01  | Consumer Price Index > OECD Groups > Energy (Fuel, electricity & gasoline) > Total | Austria   | M           | 1966-04 | IDX         |                0 | 17.9295 |
| 1966-05-01 00:00:00 | CPGREN01  | Consumer Price Index > OECD Groups > Energy (Fuel, electricity & gasoline) > Total | Austria   | M           | 1966-05 | IDX         |                0 | 17.8277 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


<br>

###	 <div id=""> <li> Business tendency and consumer opinion <hr style="border:0.5px solid gray"> </hr> </li> </div>
 
<div align="right"><a href="#0">Back to top</a> </div>


#### <i>business\_tendency\_survey( sector, country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
business_tendency_survey('retail', 'all', freq = 'M')
```

<i> Output </i>

<center><small><small>

| TIME                | SUBJECT   | Subject                                                                                                      | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-------------------------------------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1996-01-01 00:00:00 | BRCICP02  | Business tendency surveys (retail trade) > Confidence indicators > Composite indicators > National indicator | Austria   | M           | 1996-01 | PC          |                0 |   -19.4 |
| 1996-02-01 00:00:00 | BRCICP02  | Business tendency surveys (retail trade) > Confidence indicators > Composite indicators > National indicator | Austria   | M           | 1996-02 | PC          |                0 |   -15.1 |
| 1996-03-01 00:00:00 | BRCICP02  | Business tendency surveys (retail trade) > Confidence indicators > Composite indicators > National indicator | Austria   | M           | 1996-03 | PC          |                0 |   -13.4 |
| 1996-04-01 00:00:00 | BRCICP02  | Business tendency surveys (retail trade) > Confidence indicators > Composite indicators > National indicator | Austria   | M           | 1996-04 | PC          |                0 |    -7   |
| 1996-05-01 00:00:00 | BRCICP02  | Business tendency surveys (retail trade) > Confidence indicators > Composite indicators > National indicator | Austria   | M           | 1996-05 | PC          |                0 |   -20.3 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>consumer\_opinion\_survey( country\_code = 'all', measure = 'national', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
consumer_opinion_survey( 'all', freq = 'M' )
```

<i> Output </i>

<center><small><small>

| TIME                | SUBJECT   | Subject                                                                                      | Country   | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:---------------------------------------------------------------------------------------------|:----------|:------------|:--------|:------------|-----------------:|--------:|
| 1974-09-01 00:00:00 | CSCICP02  | Consumer opinion surveys > Confidence indicators > Composite indicators > National indicator | Australia | M           | 1974-09 | PC          |                0 |      -9 |
| 1974-10-01 00:00:00 | CSCICP02  | Consumer opinion surveys > Confidence indicators > Composite indicators > National indicator | Australia | M           | 1974-10 | PC          |                0 |      -9 |
| 1974-11-01 00:00:00 | CSCICP02  | Consumer opinion surveys > Confidence indicators > Composite indicators > National indicator | Australia | M           | 1974-11 | PC          |                0 |      -8 |
| 1974-12-01 00:00:00 | CSCICP02  | Consumer opinion surveys > Confidence indicators > Composite indicators > National indicator | Australia | M           | 1974-12 | PC          |                0 |      -8 |
| 1975-01-01 00:00:00 | CSCICP02  | Consumer opinion surveys > Confidence indicators > Composite indicators > National indicator | Australia | M           | 1975-01 | PC          |                0 |       0 |
| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
 
<br>

###	 <div id=""> <li> National accounts <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>


#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>


| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>


| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _



#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>


| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _



#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>


| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _



#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>


| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _



#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>


| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _



#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>


| ... | ...  | ... | ... | ...           | ...| ...         |                ... |   ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _




<br>

###	 <div id=""> <li> Production and sales <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>


#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


<br>


## <li> OECD Business Tendency Survey </li>

<div align="right"><a href="#0">Back to top</a> </div>



#### <i>oecd\_survey\_economic\_situation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_economic_situation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject         | Country       | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:----------------|:--------------|:------------|:--------|:------------|-----------------:|--------:|
| 1978-01-01 00:00:00 | CSESFT    | Future tendency | United States | M           | 1978-01 | PC          |                0 |       8 |
| 1978-02-01 00:00:00 | CSESFT    | Future tendency | United States | M           | 1978-02 | PC          |                0 |      11 |
| 1978-03-01 00:00:00 | CSESFT    | Future tendency | United States | M           | 1978-03 | PC          |                0 |      -3 |
| 1978-04-01 00:00:00 | CSESFT    | Future tendency | United States | M           | 1978-04 | PC          |                0 |       3 |
| 1978-05-01 00:00:00 | CSESFT    | Future tendency | United States | M           | 1978-05 | PC          |                0 |      -1 |
| ... | ...    | ... | ... | ...           | ... | ...          |                ... |      ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_survey\_consumer\_confidence( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_consumer_confidence( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject            | Country       | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-------------------|:--------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | CSCICP02  | National indicator | United States | M           | 1960-01 | PC          |                0 | 107.594 |
| 1960-02-01 00:00:00 | CSCICP02  | National indicator | United States | M           | 1960-02 | PC          |                0 | 105.191 |
| 1960-03-01 00:00:00 | CSCICP02  | National indicator | United States | M           | 1960-03 | PC          |                0 | 102.788 |
| 1960-04-01 00:00:00 | CSCICP02  | National indicator | United States | M           | 1960-04 | PC          |                0 | 100.385 |
| 1960-05-01 00:00:00 | CSCICP02  | National indicator | United States | M           | 1960-05 | PC          |                0 | 101.784 |
| ... | ...  | ... | ... | ...          | ... | ...          |                ... | ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_survey\_consumer\_price_inflation( country\_code = 'all', freq = 'M' )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_survey_consumer_price_inflation( country_code = 'USA', freq = 'M' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject         | Country       | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:----------------|:--------------|:------------|:--------|:------------|-----------------:|--------:|
| 1978-01-01 00:00:00 | CSINFT    | Future tendency | United States | M           | 1978-01 | PC          |                0 |     6.1 |
| 1978-02-01 00:00:00 | CSINFT    | Future tendency | United States | M           | 1978-02 | PC          |                0 |     8.5 |
| 1978-03-01 00:00:00 | CSINFT    | Future tendency | United States | M           | 1978-03 | PC          |                0 |     7.5 |
| 1978-04-01 00:00:00 | CSINFT    | Future tendency | United States | M           | 1978-04 | PC          |                0 |     8   |
| 1978-05-01 00:00:00 | CSINFT    | Future tendency | United States | M           | 1978-05 | PC          |                0 |     8.9 |
| ... | ...    | ... | ... | ...         | ...| ...          |                ... |     ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>


## <li> OECD Balance of Payments </li>

<div align="right"><a href="#0">Back to top</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


### <i>Current account</i>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_current_account(country\_code = 'all', percent\_of\_gdp = False)</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_current_account(country_code = 'USA', percent_of_gdp = True)
```

<i> Output </i>

<center><small><small>

| TIME                | SUBJECT   | Subject                             | Country       | MEASURE   | Measure                  | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |    Value |
|:--------------------|:----------|:------------------------------------|:--------------|:----------|:-------------------------|:------------|:--------|:------------|-----------------:|---------:|
| 1960-01-01 00:00:00 | B6BLTT02  | Current account balance as % of GDP | United States | STSA      | Indicators in percentage | Q           | 1960-Q1 | PC          |                0 | 0.257994 |
| 1960-04-01 00:00:00 | B6BLTT02  | Current account balance as % of GDP | United States | STSA      | Indicators in percentage | Q           | 1960-Q2 | PC          |                0 | 0.391809 |
| 1960-07-01 00:00:00 | B6BLTT02  | Current account balance as % of GDP | United States | STSA      | Indicators in percentage | Q           | 1960-Q3 | PC          |                0 | 0.612899 |


</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>oecd\_goods\_balance(country\_code, xm = 'balance')</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_goods_balance(country_code = 'USA', xm = 'exports')
```

<i> Output </i>


<center><small><small>


| TIME                | SUBJECT   | Subject                  | Country       | MEASURE   | Measure             | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-------------------------|:--------------|:----------|:--------------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | B6CRTD01  | Goods, credits (exports) | United States | CXCU      | US-Dollar converted | Q           | 1960-Q1 | USD         |                6 |    4664 |
| 1960-04-01 00:00:00 | B6CRTD01  | Goods, credits (exports) | United States | CXCU      | US-Dollar converted | Q           | 1960-Q2 | USD         |                6 |    5058 |
| 1960-07-01 00:00:00 | B6CRTD01  | Goods, credits (exports) | United States | CXCU      | US-Dollar converted | Q           | 1960-Q3 | USD         |                6 |    4736 |
| 1960-10-01 00:00:00 | B6CRTD01  | Goods, credits (exports) | United States | CXCU      | US-Dollar converted | Q           | 1960-Q4 | USD         |                6 |    5192 |
| 1961-01-01 00:00:00 | B6CRTD01  | Goods, credits (exports) | United States | CXCU      | US-Dollar converted | Q           | 1961-Q1 | USD         |                6 |    5062 |
| ... | ...  | ... | ... | ...      | ... | ...           | ... | ...         |                ... |    ... |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>oecd\_services\_balance(country\_code, xm = 'balance')</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_goods_balance(country_code = 'USA', xm = 'balance')
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject           | Country       | MEASURE   | Measure             | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:------------------|:--------------|:----------|:--------------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | B6BLSE01  | Services, balance | United States | CXCU      | US-Dollar converted | Q           | 1960-Q1 | USD         |                6 |    -239 |
| 1960-04-01 00:00:00 | B6BLSE01  | Services, balance | United States | CXCU      | US-Dollar converted | Q           | 1960-Q2 | USD         |                6 |    -205 |
| 1960-07-01 00:00:00 | B6BLSE01  | Services, balance | United States | CXCU      | US-Dollar converted | Q           | 1960-Q3 | USD         |                6 |    -758 |
| 1960-10-01 00:00:00 | B6BLSE01  | Services, balance | United States | CXCU      | US-Dollar converted | Q           | 1960-Q4 | USD         |                6 |    -183 |
| 1961-01-01 00:00:00 | B6BLSE01  | Services, balance | United States | CXCU      | US-Dollar converted | Q           | 1961-Q1 | USD         |                6 |    -306 |
| ... | ...  | ... | ... | ...      | ...| ...           | ... | ...         | ... |    ... |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


### <i>Financial account</i>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_financial\_account(country\_code = 'all', currency = 'dollar', assets\_or\_liabs = None)</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_financial_account(country_code = 'USA', currency = 'dollar')
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                | Country       | MEASURE   | Measure             | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-----------------------|:--------------|:----------|:--------------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | B6FATT01  | Financial account, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q1 | USD         |                6 |     358 |
| 1960-04-01 00:00:00 | B6FATT01  | Financial account, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q2 | USD         |                6 |     414 |
| 1960-07-01 00:00:00 | B6FATT01  | Financial account, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q3 | USD         |                6 |     159 |
| 1960-10-01 00:00:00 | B6FATT01  | Financial account, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q4 | USD         |                6 |     874 |
| 1961-01-01 00:00:00 | B6FATT01  | Financial account, net | United States | CXCU      | US-Dollar converted | Q           | 1961-Q1 | USD         |                6 |    1131 |
| ... | ...  | ... | ... | ...      | ... | ...           | ... | ...         |                ... |    ... |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>oecd\_direct\_investment(country\_code = 'all', currency = 'dollar', assets\_or\_liabs = None):</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_direct_investment(country_code = 'USA', currency = 'dollar', assets_or_liabs = None)
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                | Country       | MEASURE   | Measure             | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:-----------------------|:--------------|:----------|:--------------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | B6FADI01  | Direct investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q1 | USD         |                6 |     591 |
| 1960-04-01 00:00:00 | B6FADI01  | Direct investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q2 | USD         |                6 |     560 |
| 1960-07-01 00:00:00 | B6FADI01  | Direct investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q3 | USD         |                6 |     595 |
| 1960-10-01 00:00:00 | B6FADI01  | Direct investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q4 | USD         |                6 |     879 |
| 1961-01-01 00:00:00 | B6FADI01  | Direct investment, net | United States | CXCU      | US-Dollar converted | Q           | 1961-Q1 | USD         |                6 |     715 |
| ... | ...  | ... | ... | ...      | ... | ...           | ... | ...         |                ... |    ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>oecd\_portfolio\_investment(country\_code = 'all', currency = 'dollar', assets\_or\_liabs = None):</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_portfolio_investment(country_code = 'USA', currency = 'dollar', assets_or_liabs = None)
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                   | Country       | MEASURE   | Measure             | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:--------------------------|:--------------|:----------|:--------------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | B6FAPI10  | Portfolio investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q1 | USD         |                6 |      69 |
| 1960-04-01 00:00:00 | B6FAPI10  | Portfolio investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q2 | USD         |                6 |     139 |
| 1960-07-01 00:00:00 | B6FAPI10  | Portfolio investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q3 | USD         |                6 |     -27 |
| 1960-10-01 00:00:00 | B6FAPI10  | Portfolio investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q4 | USD         |                6 |     -91 |
| 1961-01-01 00:00:00 | B6FAPI10  | Portfolio investment, net | United States | CXCU      | US-Dollar converted | Q           | 1961-Q1 | USD         |                6 |      47 |
| ... | ...  | ... | ... | ...      | ... | ...           | ... | ...         |                ... |    ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>oecd\_other\_investment(country\_code = 'all', currency = 'dollar', assets\_or\_liabs = None):</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_other_investment(country_code = 'USA', currency = 'dollar', assets_or_liabs = None)
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject               | Country       | MEASURE   | Measure             | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:----------------------|:--------------|:----------|:--------------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | B6FAOI01  | Other investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q1 | USD         |                6 |    -143 |
| 1960-04-01 00:00:00 | B6FAOI01  | Other investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q2 | USD         |                6 |    -110 |
| 1960-07-01 00:00:00 | B6FAOI01  | Other investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q3 | USD         |                6 |     331 |
| 1960-10-01 00:00:00 | B6FAOI01  | Other investment, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q4 | USD         |                6 |    1157 |
| 1961-01-01 00:00:00 | B6FAOI01  | Other investment, net | United States | CXCU      | US-Dollar converted | Q           | 1961-Q1 | USD         |                6 |     740 |
| ... | ...  | ... | ... | ...      | ... | ...           | ... | ...         |                ... |    ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>oecd\_financial\_derivatives(country\_code = 'all', currency = 'dollar'):</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_direct_investment(country_code = 'USA', currency = 'dollar', assets_or_liabs = None)
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                    | Country       | MEASURE   | Measure             | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:---------------------------|:--------------|:----------|:--------------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | B6FAFD01  | Financial derivatives, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q1 | USD         |                6 |       0 |
| 1960-04-01 00:00:00 | B6FAFD01  | Financial derivatives, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q2 | USD         |                6 |       0 |
| 1960-07-01 00:00:00 | B6FAFD01  | Financial derivatives, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q3 | USD         |                6 |       0 |
| 1960-10-01 00:00:00 | B6FAFD01  | Financial derivatives, net | United States | CXCU      | US-Dollar converted | Q           | 1960-Q4 | USD         |                6 |       0 |
| 1961-01-01 00:00:00 | B6FAFD01  | Financial derivatives, net | United States | CXCU      | US-Dollar converted | Q           | 1961-Q1 | USD         |                6 |       0 |
| ... | ...  | ... | ... | ...      | ... | ...           | ... | ...         |                ... |    ... |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>oecd\_reserve\_assets(country\_code = 'all', currency = 'dollar'):</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
oecd_reserve_assets(country_code = 'USA', currency = 'dollar' )
```

<i> Output </i>


<center><small><small>

| TIME                | SUBJECT   | Subject                                             | Country       | MEASURE   | Measure             | FREQUENCY   | TIME    | Unit Code   |   PowerCode Code |   Value |
|:--------------------|:----------|:----------------------------------------------------|:--------------|:----------|:--------------------|:------------|:--------|:------------|-----------------:|--------:|
| 1960-01-01 00:00:00 | B6FARA01  | Reserve assets, net acquisition of financial assets | United States | CXCU      | US-Dollar converted | Q           | 1960-Q1 | USD         |                6 |    -159 |
| 1960-04-01 00:00:00 | B6FARA01  | Reserve assets, net acquisition of financial assets | United States | CXCU      | US-Dollar converted | Q           | 1960-Q2 | USD         |                6 |    -175 |
| 1960-07-01 00:00:00 | B6FARA01  | Reserve assets, net acquisition of financial assets | United States | CXCU      | US-Dollar converted | Q           | 1960-Q3 | USD         |                6 |    -740 |
| 1960-10-01 00:00:00 | B6FARA01  | Reserve assets, net acquisition of financial assets | United States | CXCU      | US-Dollar converted | Q           | 1960-Q4 | USD         |                6 |   -1071 |
| 1961-01-01 00:00:00 | B6FARA01  | Reserve assets, net acquisition of financial assets | United States | CXCU      | US-Dollar converted | Q           | 1961-Q1 | USD         |                6 |    -371 |
| ... | ...  | ... | ... | ...      | ... | ...           | ... | ...         |                ... |    ... |

</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

## <div id="7">News data</div>

<div align="right"><a href="#0">Back to top</a> </div>

<br>

# description

<br>

-----

#### <i>NewsScrape.barrons\_news( verbose = False ):</i>

<ul>
<li></li>
<li> </li>
</ul>

<i> Example </i>

```python
# retrieve news article for a given search term
ns = NewsScrape('XOM', 'exxon mobil')
df = ns.barrons_news()
# filter news articles with a keyword list
ns.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
data = ns.filter_data(data)
```

<i> Output </i>


<center><small><small>

|    | Link                                                                                                                                                   | Headline                                                                                                     | Date                    | Description                                                                                                                                                                                                                                                         | Newspaper       | Author          | Date_Retrieved             | Ticker   |   Comments |   Tag | Search_term   | ID                                                                                                                                                                                                                                                                                | Source   | Datetime   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:----------------|:---------------------------|:---------|-----------:|------:|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|
|  0 | https://www.barrons.com/articles/apples-market-cap-is-now-as-big-as-the-s-p-500-energy-utilities-and-materials-sectorscombined-51599057653             | Apple’s Market Cap Is Now as Big as the S&P 500 Energy, Utilities, and Materials Sectors—Combined            | Sep 2, 2020 10:40 AM ET | The energy sector, meanwhile, continues to fade and is just 2.3% of the index.                                                                                                                                                                                      | Barrons.com     | Andrew Bary     | 2020-09-03 15:29:45.797553 | XOM      |        nan |   nan | exxon mobil   | Barrons.comApple’s Market Cap Is Now as Big as the S&P 500 Energy, Utilities, and Materials Sectors—Combinedhttps://www.barrons.com/articles/apples-market-cap-is-now-as-big-as-the-s-p-500-energy-utilities-and-materials-sectorscombined-51599057653                            | barrons  | 02/09/2020 |\n|  1 | http://www.marketwatch.com/story/dirty-oil-companies-could-lead-low-carbon-transformation-new-goldman-report-says-11599042929                          | Unloved, dirty oil companies could lead low-carbon transformation, new Goldman report says                   | Sep 2, 2020 8:35 AM ET  | A new report says Big Oil companies can drive a low-carbon future.                                                                                                                                                                                                  | MarketWatch.com | Steve Goldstein | 2020-09-03 15:29:45.797553 | XOM      |        nan |   nan | exxon mobil   | MarketWatch.comUnloved, dirty oil companies could lead low-carbon transformation, new Goldman report sayshttp://www.marketwatch.com/story/dirty-oil-companies-could-lead-low-carbon-transformation-new-goldman-report-says-11599042929                                            | barrons  | 02/09/2020 |
|  2 | https://www.wsj.com/articles/summer-fuel-demand-disappoints-challenging-economy-11598952601                                                            | Summer Fuel Demand Disappoints, Challenging Economy                                                          | Sep 1, 2020             | After demand for gasoline surged from mid-April to late June, lingering caution among drivers and delayed office and school reopening plans are hindering the recovery in energy markets.                                                                           | WSJ.com         | Amrith Ramkumar | 2020-09-03 15:29:45.797553 | XOM      |        nan |   nan | exxon mobil   | WSJ.comSummer Fuel Demand Disappoints, Challenging Economyhttps://www.wsj.com/articles/summer-fuel-demand-disappoints-challenging-economy-11598952601                                                                                                                             | barrons  | 01/09/2020 |
|  3 | https://www.barrons.com/articles/top-pension-sold-cruise-stocks-carnival-royal-caribbean-bought-gm-exxon-stock-51598544141                             | A Top U.S. Pension Sold Off Cruise Stocks. Here’s What It Bought.                                            | Aug 31, 2020            | The South Dakota Investment Council manages the state’s pension, one of the best in the country based on funding status. It slashed positions in Carnival, Royal Caribbean, and Nowegian Cruise Lines in the second quarter. It bought up GM and Exxon Mobil stock. | Barrons.com     | Ed Lin          | 2020-09-03 15:29:45.797553 | XOM      |        nan |   nan | exxon mobil   | Barrons.comA Top U.S. Pension Sold Off Cruise Stocks. Here’s What It Bought.https://www.barrons.com/articles/top-pension-sold-cruise-stocks-carnival-royal-caribbean-bought-gm-exxon-stock-51598544141                                                                            | barrons  | 31/08/2020 |
|  4 | http://www.marketwatch.com/story/exxon-getting-booted-from-the-dow-jones-industrial-average-may-be-a-blessing-in-disguise-for-its-investors-2020-08-25 | Exxon’s getting booted from the Dow Jones Industrial Average may be a blessing in disguise for its investors | Aug 30, 2020            | Stocks deleted from an index often proceed to beat the additions                                                                                                                                                                                                    | MarketWatch.com | Mark Hulbert    | 2020-09-03 15:29:45.797553 | XOM      |        nan |   nan | exxon mobil   | MarketWatch.comExxon’s getting booted from the Dow Jones Industrial Average may be a blessing in disguise for its investorshttp://www.marketwatch.com/story/exxon-getting-booted-from-the-dow-jones-industrial-average-may-be-a-blessing-in-disguise-for-its-investors-2020-08-25 | barrons  | 30/08/2020 |
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>NewsScrape.bloomberg\_news( verbose = False ):</i>

<ul>
<li></li>
<li> </li>
</ul>

<i> Example </i>

```python
ns = NewsScrape('ticker', 'keywords')
df = ns.bloomberg_news()
```

<i> Output </i>


<center><small><small>

|    | Link                                                                                                                  | Headline                                                             | Date              | Description                                                                                                                                                                                                                                                                                                                           | Tag      |   Author | Date_Retrieved             | Ticker   |   Comments | Newspaper   | Search_term   | ID                                                                                                                                                                                                 | Source    | Datetime   |
|---:|:----------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|---------:|:---------------------------|:---------|-----------:|:------------|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|:-----------|
|  0 | https://www.bloomberg.com/news/articles/2020-09-01/canadian-oil-rises-after-spill-shuts-diluent-pipeline-in-alberta   | Exxon’s Imperial Shuts Oil-Sands Mine After Pipeline Spill           | September 2, 2020 | Exxon Mobil Corp.’s Imperial Oil shut down its oil-sands mine after a spill from a pipeline that supplies diluent to the operation, adding to the woes of Canada’s beleaguered energy industry.                                                                                                                                       | markets  |      nan | 2020-09-03 17:38:48.858715 | XOM      |        nan | Bloomberg   | exxon mobil   | BloombergExxon’s Imperial Shuts Oil-Sands Mine After Pipeline Spillhttps://www.bloomberg.com/news/articles/2020-09-01/canadian-oil-rises-after-spill-shuts-diluent-pipeline-in-alberta             | bloomberg | 02/09/2020 |
|  1 | https://www.bloomberg.com/news/articles/2020-09-02/papua-new-guinea-steps-up-fight-for-share-of-oil-mineral-wealth    | Papua New Guinea Steps Up Fight for Share of Oil, Mineral Wealth     | September 2, 2020 | Papua New Guinea is demanding a greater share of the country’s resource wealth, stepping up its battle with companies including Exxon Mobil Corp. and Barrick Gold Corp.                                                                                                                                                              | markets  |      nan | 2020-09-03 17:38:48.858715 | XOM      |        nan | Bloomberg   | exxon mobil   | BloombergPapua New Guinea Steps Up Fight for Share of Oil, Mineral Wealthhttps://www.bloomberg.com/news/articles/2020-09-02/papua-new-guinea-steps-up-fight-for-share-of-oil-mineral-wealth        | bloomberg | 02/09/2020 |
|  2 | https://www.bloomberg.com/view/articles/2020-08-30/as-exxon-mobil-is-removed-from-the-dow-is-this-the-end-for-big-oil | As Exxon Mobil Is Removed From the Dow, Is This the End for Big Oil? | August 30, 2020   | Exxon\'s departure from the Dow is just one symptom. The oil majors\' opportunities and reputations are in decline everywhere.                                                                                                                                                                                                          | opinion  |      nan | 2020-09-03 17:38:48.858715 | XOM      |        nan | Bloomberg   | exxon mobil   | BloombergAs Exxon Mobil Is Removed From the Dow, Is This the End for Big Oil?https://www.bloomberg.com/view/articles/2020-08-30/as-exxon-mobil-is-removed-from-the-dow-is-this-the-end-for-big-oil | bloomberg | 30/08/2020 |
|  3 | https://www.bloomberg.com/view/articles/2020-09-01/guyana-s-oil-bonanza-could-inflame-its-ethnic-divisions            | Guyana’s Oil Bonanza Could Inflame Its Ethnic Divisions              | September 1, 2020 | Even as more Guyanese identify as racially mixed, its politics are not, with ugly consequences for development.                                                                                                                                                                                                                       | opinion  |      nan | 2020-09-03 17:38:48.858715 | XOM      |        nan | Bloomberg   | exxon mobil   | BloombergGuyana’s Oil Bonanza Could Inflame Its Ethnic Divisionshttps://www.bloomberg.com/view/articles/2020-09-01/guyana-s-oil-bonanza-could-inflame-its-ethnic-divisions                         | bloomberg | 01/09/2020 |
|  4 | https://www.bloomberg.com/news/videos/2020-08-25/big-oil-needs-to-pivot-to-survive-kpmg-s-mayor-says-video            | Big Oil Needs to Pivot Portfolio to Survive, KPMG\'s Mayor Says       | August 25, 2020   | Regina Mayor, KPMG\'s global head of energy, says the removal of Exxon Mobil Corp. from the Dow Jones Industrial Average is a signal that large energy companies need to embrace an "energy transition" to remain relevant. She speaks with Bloomberg\'s Lisa Abramowicz and Tom Keene on "Bloomberg Surveillance." (Source: Bloomberg) | business |      nan | 2020-09-03 17:38:48.858715 | XOM      |        nan | Bloomberg   | exxon mobil   | BloombergBig Oil Needs to Pivot Portfolio to Survive, KPMG\'s Mayor Sayshttps://www.bloomberg.com/news/videos/2020-08-25/big-oil-needs-to-pivot-to-survive-kpmg-s-mayor-says-video                  | bloomberg | 25/08/2020 |
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>NewsScrape.cnbc\_news( verbose = False ):</i>

<ul>
<li></li>
<li> </li>
</ul>

<i> Example </i>

```python
ns = NewsScrape('ticker', 'keywords')
df = ns.cnbc_news()
```

<i> Output </i>


<center><small><small>

|    | Link                                                                                                                                                       | Headline                                                                                    | Date                 | Description                                                                                                                                                                          | Tag                  | Author          | Date_Retrieved             | Ticker   |   Comments | Newspaper   | Search_term   | ID                                                                                                                                                                                                                                                        | Source   | Datetime   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|:----------------|:---------------------------|:---------|-----------:|:------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|
|  0 | https://www.cnbc.com/2020/09/02/stocks-making-the-biggest-moves-in-the-premarket-macys-hr-block-peloton-exxon-more.html?&qsearchterm=exxon mobil           | Stocks making the biggest moves in the premarket: Macy’s, H&R Block, Peloton, Exxon & more  | 9/2/2020 2:35:12 PM  | Take a look at some of the biggest movers in the premarket:Macy’s (M) – The retailer lost 81 cents per share for its second quarter, ...                                             | Market Insider       | Peter Schacknow | 2020-09-03 18:22:04.839665 | XOM      |        nan | CNBC        | exxon mobil   | CNBCStocks making the biggest moves in the premarket: Macy’s, H&R Block, Peloton, Exxon & morehttps://www.cnbc.com/2020/09/02/stocks-making-the-biggest-moves-in-the-premarket-macys-hr-block-peloton-exxon-more.html?&qsearchterm=exxon mobil            | cnbc     | 02/09/2020 |
|  1 | https://www.cnbc.com/2020/08/31/dow-stocks-traders-see-one-company-as-best-catch-up-play-to-rally.html?&qsearchterm=exxon mobil                            | As Dow undergoes makeover, traders see one stock as best catch-up play to the rally         | 8/31/2020 8:00:39 PM | The Dow looks a little different Monday.Earlier, the blue-chip index traded out Exxon Mobil, Pfizer and Raytheon Technologies and cycled in Salesforce, Amgen and Honeywell.Even ... | Trading Nation       | Keris Lahiff    | 2020-09-03 18:22:04.839665 | XOM      |        nan | CNBC        | exxon mobil   | CNBCAs Dow undergoes makeover, traders see one stock as best catch-up play to the rallyhttps://www.cnbc.com/2020/08/31/dow-stocks-traders-see-one-company-as-best-catch-up-play-to-rally.html?&qsearchterm=exxon mobil                                    | cnbc     | 31/08/2020 |
|  2 | https://www.cnbc.com/2020/08/29/stocks-that-leave-the-dow-tend-to-outperform-after-their-exit-from-the-average-history-shows.html?&qsearchterm=exxon mobil | Stocks that leave the Dow tend to outperform after their exit from the average, history ... | 8/29/2020 2:15:24 PM | Exxon Mobil, Pfizer and Raytheon Technologies are on their way out of the Dow Jones Industrial Average. But their exit from the blue-chip club may ...                               | Pro: Pro Insight     | Fred Imbert     | 2020-09-03 18:22:04.839665 | XOM      |        nan | CNBC        | exxon mobil   | CNBCStocks that leave the Dow tend to outperform after their exit from the average, history ...https://www.cnbc.com/2020/08/29/stocks-that-leave-the-dow-tend-to-outperform-after-their-exit-from-the-average-history-shows.html?&qsearchterm=exxon mobil | cnbc     | 29/08/2020 |
|  3 | https://www.cnbc.com/2020/08/27/oil-markets-gulf-of-mexico-storm-shuts-output.html?&qsearchterm=exxon mobil                                                | Oil dips as Hurricane Laura hammers U.S. Gulf Coast                                         | 8/27/2020 7:47:15 AM | Oil prices fell on Thursday as a massive hurricane in the Gulf of Mexico made landfall in the heart of the U.S. oil industry, forcing ...                                            | Energy Commodities   | nan             | 2020-09-03 18:22:04.839665 | XOM      |        nan | CNBC        | exxon mobil   | CNBCOil dips as Hurricane Laura hammers U.S. Gulf Coasthttps://www.cnbc.com/2020/08/27/oil-markets-gulf-of-mexico-storm-shuts-output.html?&qsearchterm=exxon mobil                                                                                        | cnbc     | 27/08/2020 |
|  4 | https://www.cnbc.com/video/2020/08/25/salesforce-is-a-company-that-most-people-dont-know-what-it-does-jim-cramer.html?&qsearchterm=exxon mobil             | Salesforce is a company that most people don’t know what it does: Jim Cramer                | 8/25/2020 4:08:17 PM | CNBC’s Jim Cramer discusses the removal of Exxon Mobil, Pfizer and Raytheon Technologies from the Dow 30 and the new names added, including Salesforce.com, Amgen ...                | Squawk on the Street | nan             | 2020-09-03 18:22:04.839665 | XOM      |        nan | CNBC        | exxon mobil   | CNBCSalesforce is a company that most people don’t know what it does: Jim Cramerhttps://www.cnbc.com/video/2020/08/25/salesforce-is-a-company-that-most-people-dont-know-what-it-does-jim-cramer.html?&qsearchterm=exxon mobil                            | cnbc     | 25/08/2020 |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>NewsScrape.ft\_news( verbose = False ):</i>

<ul>
<li></li>
<li> </li>
</ul>

<i> Example </i>

```python
ns = NewScrape('ticker', 'keywords')
df = ns.ft_news()
```

<i> Output </i>


<center><small><small>

|    | Link                                          | Headline                                                         | Date          | Description                                                                                                                                                                                                                                                       | Tag                     | Date_Retrieved             | Ticker   |   Comments |   Author | Newspaper   | Search_term   | ID                                                                                                               | Source   | Datetime   |
|---:|:----------------------------------------------|:-----------------------------------------------------------------|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|:---------------------------|:---------|-----------:|---------:|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------|:---------|:-----------|
|  0 | /content/64d7e86e-079c-4502-a9a4-5ab7439c732f | Big Oil gets smaller as Chevron and Exxon losses mount to $9.4bn | July 31, 2020 | ...destruction in the second quarter was unprecedented in the history of modern oil markets,” Neil Chapman, Exxon senior vice-president, told analysts on an investor call.                                      | Oil & Gas industry      | 2020-09-03 15:52:40.383049 | XOM      |        nan |      nan | FT          | exxon mobil   | FTBig Oil gets smaller as Chevron and Exxon losses mount to $9.4bn /content/64d7e86e-079c-4502-a9a4-5ab7439c732f | ft       | 31/07/2020 |\n|    |                                               |                                                                  |               | \t\t\t\t\t\t\t\t                                                                                                                                                                                                         |                         |                            |          |            |          |             |               |                                                                                                                  |          |            |
|    |                                               |                                                                  |               | \t\t\t\t\t\t\t\t“To put it in context, absolute...                                                                                                                                                                       |                         |                            |          |            |          |             |               |                                                                                                                  |          |            |
|  1 | /content/c43ead81-5af3-44de-af1e-b108d6491354 | Exxon shareholders vote against splitting chair and CEO roles    | May 27, 2020  | ...Exxon, said the appointment of a lead director had helped improve oversight.                                                                                                                                                                                   | Oil & Gas industry      | 2020-09-03 15:52:40.383049 | XOM      |        nan |      nan | FT          | exxon mobil   | FTExxon shareholders vote against splitting chair and CEO roles/content/c43ead81-5af3-44de-af1e-b108d6491354     | ft       | 27/05/2020 |\n|    |                                               |                                                                  |               | \t\t\t\t\t\t\t\t                                                                                                                                                                                                                                                          |                         |                            |          |            |          |             |               |                                                                                                                  |          |            |
|    |                                               |                                                                  |               | \t\t\t\t\t\t\t\tA separate resolution calling for increased transparency about Exxon’s lobbying activity won 37.5 per cent support, a...                                                                                                                                  |                         |                            |          |            |          |             |               |                                                                                                                  |          |            |
|  2 | /content/c54ee229-f4e7-43c8-87a5-e383099542fb | Big Exxon shareholder to vote against chief                      | May 12, 2020  | ...company to disclose its lobbying activities, arguing it was falling behind global peers by failing to act on climate change.                                                                                  | Corporate governance    | 2020-09-03 15:52:40.383049 | XOM      |        nan |      nan | FT          | exxon mobil   | FTBig Exxon shareholder to vote against chief/content/c54ee229-f4e7-43c8-87a5-e383099542fb                       | ft       | 12/05/2020 |
|    |                                               |                                                                  |               | \t\t\t\t\t\t\t\t                                                                                                                                                                                                         |                         |                            |          |            |          |             |               |                                                                                                                  |          |            |
|    |                                               |                                                                  |               | \t\t\t\t\t\t\t\tWednesday’s move by LGIM, whose roughly $1bn stake makes it a top-20 Exxon...                                                                                                                            |                         |                            |          |            |          |             |               |                                                                                                                  |          |            |
|  3 | /content/0115d0ce-5e99-4801-9196-82375874f78b | Exxon slashes capital investment by $10bn                        | April 7, 2020 | ...Darren Woods on Tuesday. He added that Exxon was anticipating a 20-30 per cent short-term drop in global oil demand.                                                                                          | Exxon Mobil Corp        | 2020-09-03 15:52:40.383049 | XOM      |        nan |      nan | FT          | exxon mobil   | FTExxon slashes capital investment by $10bn\xa0/content/0115d0ce-5e99-4801-9196-82375874f78b                        | ft       | 07/04/2020 |
|    |                                               |                                                                  |               | \t\t\t\t\t\t\t\t                                                                                                                                                                                                         |                         |                            |          |            |          |             |               |                                                                                                                  |          |            |
|    |                                               |                                                                  |               | \t\t\t\t\t\t\t\tExxon said it could also reduce its planned spending next year as it navigated the...                                                                                                                    |                         |                            |          |            |          |             |               |                                                                                                                  |          |            |
|  4 | /content/bc398fca-c66d-4d0f-8e29-a1b0a6fee6bd | Biggest US energy groups lay out oil crash strategy              | May 1, 2020   | ...heavyweights will, though, continue to cut capital spending. Exxon is sticking with the 30 per cent reduction this year, to $23bn, that it announced last month. Chevron went deeper, lopping another $2bn... | US & Canadian companies | 2020-09-03 15:52:40.383049 | XOM      |        nan |      nan | FT          | exxon mobil   | FTBiggest US energy groups lay out oil crash strategy/content/bc398fca-c66d-4d0f-8e29-a1b0a6fee6bd               | ft       | 01/05/2020 |


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>NewsScrape.nyt\_news( verbose = False ):</i>

<ul>
<li></li>
<li> </li>
</ul>

<i> Example </i>

```python
ns = NewsScrape('ticker', 'keywords')
df = ns.nyt_news()
```

<i> Output </i>


<center><small><small>


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>NewsScrape.reuters\_news( verbose = False ):</i>

<ul>
<li></li>
<li> </li>
</ul>

<i> Example </i>

```python
ns = NewsScrape('ticker', 'keywords')
df = ns.reuters_news()
```

<i> Output </i>


<center><small><small>


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>NewsScrape.seeking\_alpha\_news( verbose = False ):</i>

<ul>
<li></li>
<li> </li>
</ul>

<i> Example </i>

```python
ns = NewsScrape('XOM', 'exxon mobil')
df = ns.seeking_alpha_news()
```

<i> Output </i>


<center><small><small>


|    | Link                                                                                                                                                                                                           | Headline                                                                      | Date               | Author   | Comments   | Date_Retrieved             | Ticker   |   Description |   Tag | Newspaper   | Search_term   | ID                                                                                                                                                                                                                                                                                                   | Source   | Datetime   |
|---:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|:-------------------|:---------|:-----------|:---------------------------|:---------|--------------:|------:|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------|
|  0 | /news/3611317-exxon-said-restarting-large-crude-unit-coker-beaumont-refinery?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:1               | Exxon said restarting large crude unit, coker at Beaumont refinery            | Yesterday, 6:58 PM | SA News  | 0 Comments | 2020-09-03 15:02:21.777207 | XOM      |           nan |   nan | SA - News   | exxon mobil   | SA - NewsExxon said restarting large crude unit, coker at Beaumont refinery/news/3611317-exxon-said-restarting-large-crude-unit-coker-beaumont-refinery?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:1                          | sa       | 02/09/2020 |
|  1 | /news/3611317-exxon-said-restarting-large-crude-unit-coker-beaumont-refinery?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Title\|lock\_status:No\|line:1                | Exxon said restarting large crude unit, coker at Beaumont refinery            | Yesterday, 6:58 PM | SA News  | 0 Comments | 2020-09-03 15:02:21.777207 | XOM      |           nan |   nan | SA - News   | exxon mobil   | SA - NewsExxon said restarting large crude unit, coker at Beaumont refinery/news/3611317-exxon-said-restarting-large-crude-unit-coker-beaumont-refinery?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Title\|lock\_status:No\|line:1                           | sa       | 02/09/2020 |
|  2 | /news/3611203-png-calls-out-exxon-barrick-in-stepping-up-case-for-share-of-resource-wealth?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:2 | PNG calls out Exxon, Barrick in stepping up case for share of resource wealth | Yesterday, 2:56 PM | SA News  | 0 Comments | 2020-09-03 15:02:21.777207 | XOM      |           nan |   nan | SA - News   | exxon mobil   | SA - NewsPNG calls out Exxon, Barrick in stepping up case for share of resource wealth/news/3611203-png-calls-out-exxon-barrick-in-stepping-up-case-for-share-of-resource-wealth?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:2 | sa       | 02/09/2020 |
|  3 | /news/3611203-png-calls-out-exxon-barrick-in-stepping-up-case-for-share-of-resource-wealth?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Title\|lock\_status:No\|line:2  | PNG calls out Exxon, Barrick in stepping up case for share of resource wealth | Yesterday, 2:56 PM | SA News  | 0 Comments | 2020-09-03 15:02:21.777207 | XOM      |           nan |   nan | SA - News   | exxon mobil   | SA - NewsPNG calls out Exxon, Barrick in stepping up case for share of resource wealth/news/3611203-png-calls-out-exxon-barrick-in-stepping-up-case-for-share-of-resource-wealth?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Title\|lock\_status:No\|line:2  | sa       | 02/09/2020 |
|  4 | /news/3611201-construction-resumes-kinder-morgan-pipeline-after-suspicious-package?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:3         | Construction resumes at Kinder Morgan pipeline after suspicious package       | Yesterday, 2:34 PM | SA News  | 0 Comments | 2020-09-03 15:02:21.777207 | XOM      |           nan |   nan | SA - News   | exxon mobil   | SA - NewsConstruction resumes at Kinder Morgan pipeline after suspicious package/news/3611201-construction-resumes-kinder-morgan-pipeline-after-suspicious-package?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:3               | sa       | 02/09/2020 |



</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#### <i>NewsScrape.wsj\_news( verbose = False ):</i>

<ul>
<li></li>
<li> </li>
</ul>

<i> Example </i>

```python
ns = NewsScrape('ticker', 'keywords')
df = ns.wsj_news()
```

<i> Output </i>


<center><small><small>


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


## <div id="8">Other data</div>


<div align="right"><a href="#0">Back to top</a> </div>

<br>


stock symbols
- world
- nasdaq
cik symbol
weather data
- heating and cooling degree days
- eia
- usda


<br>


## <div id="9"> Sources </div>

<li>Alpha-Vantage, www.alphavantage.co</li>
<li>Barrons, www.barrons.com</li>
<li>Bloomberg, www.bloomberg.com</li>
<li>CNBC, www.cnbc.com</li>
<li>Financial Times, www.ft.com</li>
<li>Finviz, www.finviz.com</li>
<li>Gurufocus, www.gurufocus.com</li>
<li>IEX Cloud, www.iexcloud.io</li>
<li>Investing.com, www.investing.com </li>
<li>MarketWatch, www.marketwatch.com </li>
<li>Moore Research Center, www.mrci.com </li>
<li>NASDAQ, www.nasdaq.com</li>
<li>OECD, www.oecd.org</li>
<li>Reuters, www.reuters.com</li>
<li>Seeking Alpha, www.seekingalpha.com</li>
<li>Tiingo, www.tiingo.com</li>
<li>Wall Street Journal, www.wsj.com</li>
<li>Yahoo Finance, www.finance.yahoo.com </li>

<br>

<li>SEC...?</li>
<li>CBOE...?</li>
<li>VixCentral...?</li>
<li>SeekingAlpha...?</li>


<div align="right"><a href="#0">Back to top</a> </div>

