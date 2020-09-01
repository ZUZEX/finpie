

-------------



# jippy - simple library to download some financial data

<center><big>

<span style="color:red">For recreational use only. Made for finance students for personal educational purposes to have easier access to some financial data.</span>

</big></center>

#further description


## <div id="0">Documentation</div>

<ol>
<li>
<a href="#2">Installation</a>
</li>
<li>
<a href="#A2">Company fundamental data</a><ul>
	<li><a href="#A21">Valuation metrics and financial ratios</a></li>
	<li><a href="#A22">Financial statements</a></li>
	<li><a href="#A23">Earnings and revenue estimates</a></li>
	<li><a href = "">Insider transactions and analyst ratings</a></li>
	<li><a href = "">ESG data</a></li>
	<li><a href = "">Company profile</a></li>
	</ul>
</li>
<li>
<a href="#B2">Price data</a><ul>
	<li><a href="">Stock prices</a></li>
	<li><a href="">Option prices</a></li>
	<li><a href="#A23">Futures prices</a></li>
	</ul>

</li>
<li><a href="#D2">Economic data</a></li>
<li><a href="#E2">News data</a></li>
<li><a href="#EE2">Other data</a></li>
<li><a href="#F2">Index</a></li>
<li><a href="#G2">Sources</a></li>
</ol>

## <div id="2">Installation</div>

Python 3 is recommended. Pip install is available. Google Chrome version <code>84.\*.\*\*\*\*.\*\*\*</code> or higher required.

```python
$ pip install jippy
```

<div align="right"><a href="#0">Back to top</a> </div>


## <div id="A2"> Company Fundamental data</a>

```python
from jippy.fundamental_data.yahoo_fundamentals import *
```
<br>

##	 <div id="A21"> <li> Valuation metrics and financial ratios </li> </div>


#### <div id="f1"><i>get\_valuation\_metrics( ticker )</i></div>

<ul>
<li>The input is a valid company ticker.</li>
<li>Returns dataframe with valuation metrics for the last five quarters and for the current date including trailing P/E, PEG ratio, P/S, etc.</li>
</ul>

<i> Example </i>

```python
get_valuation_metrics('AAPL')
```

<i> Output </i>

<center><small><small>

|    | Date                  |   Market\_Cap\_(intraday) |   Forward\_PE |   PEG\_Ratio\_(5\_yr\_expected) |   PriceSales\_(ttm) |   PriceBook\_(mrq) |   ... |
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


#### <i>get\_ratios( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li>Returns dataframe with current twelve months trailing cashflow statement and the previous 4 annual cashflow statements.</li>
</ul>

<i> Example </i>

```python
get_ratios('AAPL')
```

<i> Output </i>

<center><small><small>

|    |   Payout\_Ratio |   Profit\_Margin |   Operating\_Margin\_(ttm) |   Return\_on\_Assets\_(ttm) |   Return\_on\_Equity\_(ttm) |   ...|
|---:|---------------:|----------------:|-------------------------:|-------------------------:|-------------------------:|----------------:|
|  0 |         0.2373 |          0.2133 |                   0.2452 |                   0.1312 |                   0.6925 |      ... |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

## <div id="A22"><li>Financial statements</li></div>

<div align="right"><a href="#0">Back to top</a> </div>

#### <i>get\_income\_statement( ticker )</i>
<ul>
<li>The input is a valid company ticker.</li>
<li>Returns dataframe with current twelve months trailing income statement and the previous 4 annual income statements.</li>
</ul>

<i> Example </i>

```python
get_income_statement('AAPL')
```

<i> Output </i>

<center><small><small>

|    | Breakdown   |   Total\_Revenue |   Cost\_of\_Revenue |   Gross\_Profit |   Operating\_Expense |   Operating\_Income |   ... |
|---:|:------------|----------------:|------------------:|---------------:|--------------------:|-------------------:|--------------------------------------------:|
|  0 | ttm         |       273857000 |         169277000 |      104580000 |            37442000 |           67138000 |                                     ... |
|  1 | 9/30/2019   |       260174000 |         161782000 |       98392000 |            34462000 |           63930000 |                                     ... |
|  2 | 9/30/2018   |       265595000 |         163756000 |      101839000 |            30941000 |           70898000 |                                     ... |
|  3 | 9/30/2017   |       229234000 |         141048000 |       88186000 |            26842000 |           61344000 |                                     ... |
|  4 | 9/30/2016   |       215639000 |         131376000 |       84263000 |            24239000 |           60024000 |                                     ... |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>get\_balance\_sheet( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li>Returns dataframe with current twelve months trailing balance sheet and the previous 4 annual balance sheets.</li>
</ul>

<i> Example </i>

```python
get_balance_sheet('AAPL')
```

<i> Output </i>

<center><small><small>

|    | Breakdown   |   Total\_Assets |   Total\_Liabilities\_Net\_Minority\_Interest |   Total\_Equity\_Gross\_Minority\_Interest |   Total\_Capitalization |   ... |
|---:|:------------|---------------:|------------------------------------------:|---------------------------------------:|-----------------------:|----------------------:|
|  0 | 9/30/2019   |      338516000 |                                 248028000 |                               90488000 |              182295000 |              ... |
|  1 | 9/30/2018   |      365725000 |                                 258578000 |                              107147000 |              200882000 |             ... |
|  2 | 9/30/2017   |      375319000 |                                 241272000 |                              134047000 |              231254000 |             ... |
|  3 | 9/30/2016   |      321686000 |                                 193437000 |                              128249000 |              203676000 |             ... |


</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>get\_cashflow\_statement( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li>Returns dataframe with current twelve months trailing cashflow statement and the previous 4 annual cashflow statements.</li>
</ul> 

<i> Example </i>

```python
get_cashflow_statement('AAPL')
```

<i> Output </i>

<center><small><small>

|    | Breakdown   |   Operating\_Cash\_Flow |   Investing\_Cash\_Flow |   Financing\_Cash\_Flow |   End\_Cash\_Position |   ... |
|---:|:------------|----------------------:|----------------------:|----------------------:|--------------------:|------------------------------------:|
|  0 | ttm         |              80008000 |             -10618000 |             -86502000 |            35039000 |                            ... |
|  1 | 9/30/2019   |              69391000 |              45896000 |             -90976000 |            50224000 |                            ... |
|  2 | 9/30/2018   |              77434000 |              16066000 |             -87876000 |            25913000 |                            ... |
|  3 | 9/30/2017   |              63598000 |             -46446000 |             -17347000 |            20289000 |                            ... |
|  4 | 9/30/2016   |              65824000 |             -45977000 |             -20483000 |            20484000 |                            ... |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>get\_statements( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li>Returns <code>get_income_statement(ticker)</code>, <code>get_balance_sheet(ticker)</code> and <code>get_cashflow_statement(ticker)</code> for the given company.</li>
</ul> 

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

## <div id="A23"><li>Earnings and revenue estimates</li></div>

<div align="right"><a href="#0">Back to top</a> </div>

#### <i>get\_earnings\_estimates( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li>Returns earnings estimates for the given company.</li>
</ul>

<i> Example </i>

```python
get_earnings_estimates('AAPL')
```
<i> Output </i>
<center><small><small>

|    | Date                    |   No.\_of\_Analysts |   Avg.\_Estimate |   Low\_Estimate |   High\_Estimate |   Year\_Ago\_EPS |
|---:|:------------------------|------------------:|----------------:|---------------:|----------------:|---------------:|
|  1 | Current Qtr. (Sep 2020) |                28 |            2.8  |           2.18 |            3.19 |           3.03 |
|  2 | Next Qtr. (Dec 2020)    |                24 |            5.45 |           4.76 |            6.82 |           4.99 |
|  3 | Current Year (2020)     |                35 |           12.97 |          12.36 |           13.52 |          11.89 |
|  4 | Next Year (2021)        |                35 |           15.52 |          12.67 |           18    |          12.97 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>get\_earnings\_estimate\_trends( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
get_earnings_estimate_trend('AAPL')
```

<i> Output </i>

<center><small><small>

|    | Date                    |   Current\_Estimate |   7\_Days\_Ago |   30\_Days\_Ago |   60\_Days\_Ago |   90\_Days\_Ago |
|---:|:------------------------|-------------------:|-------------:|--------------:|--------------:|--------------:|
|  1 | Current Qtr. (Sep 2020) |               2.8  |         2.84 |          2.79 |          2.82 |          2.8  |
|  2 | Next Qtr. (Dec 2020)    |               5.45 |         5.44 |          5.22 |          5.21 |          5.22 |
|  3 | Current Year (2020)     |              12.97 |        13    |         12.41 |         12.39 |         12.32 |
|  4 | Next Year (2021)        |              15.52 |        15.54 |         14.94 |         14.86 |         14.73 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>get\_earnings\_history( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
get_earnings_history('AAPL')
```

<i> Output </i>

<center><small><small>

|    | Date       |   EPS\_Est. |   EPS\_Actual |   Difference |   Surprise\_% |
|---:|:-----------|-----------:|-------------:|-------------:|-------------:|
|  1 | 9/29/2019  |       2.84 |         3.03 |         0.19 |        0.067 |
|  2 | 12/30/2019 |       4.55 |         4.99 |         0.44 |        0.097 |
|  3 | 3/30/2020  |       2.26 |         2.55 |         0.29 |        0.128 |
|  4 | 6/29/2020  |       2.04 |         2.58 |         0.54 |        0.265 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>get\_revenue\_estimates( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
get_revenue_estimates('AAPL')
```

<i> Output </i>

<center><small><small>

|    | Date                    |   No.\_of\_Analysts |   Avg.\_Estimate |   Low\_Estimate |   High\_Estimate |   Year\_Ago\_Sales |   Sales\_Growth\_(yearest) |
|---:|:------------------------|------------------:|----------------:|---------------:|----------------:|-----------------:|-------------------------:|
|  1 | Current Qtr. (Sep 2020) |                26 |      6.351e+10  |     5.255e+10  |      6.85e+10   |       6.404e+10  |                   -0.008 |
|  2 | Next Qtr. (Dec 2020)    |                24 |      1.0036e+11 |     8.992e+10  |      1.157e+11  |       8.85e+10   |                    0.134 |
|  3 | Current Year (2020)     |                33 |      2.7338e+11 |     2.6236e+11 |      2.8089e+11 |       2.6017e+11 |                    0.051 |
|  4 | Next Year (2021)        |                33 |      3.0734e+11 |     2.7268e+11 |      3.3153e+11 |       2.7338e+11 |                    0.124 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>get\_growth\_estimates( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
get_growth_estimates('AAPL')
```

<i> Output </i>

<center><small><small>

|    | Date      |   Current\_Qtr. |   Next\_Qtr. |   Current\_Year |   Next\_Year |   Next\_5\_Years\_(per\_annum) |   Past\_5\_Years\_(per\_annum) |
|---:|:----------|---------------:|------------:|---------------:|------------:|---------------------------:|---------------------------:|
|  1 | AAPL      |         -0.076 |       0.092 |          0.091 |       0.197 |                     0.1246 |                     0.0842 |
|  2 | Industry  |        nan     |     nan     |        nan     |     nan     |                   nan      |                   nan      |
|  3 | Sector(s) |        nan     |     nan     |        nan     |     nan     |                   nan      |                   nan      |
|  4 | S&P 500   |        nan     |     nan     |        nan     |     nan     |                   nan      |                   nan      |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

## <li> ESG data </li>


<div align="right"><a href="#0">Back to top</a> </div>

<br>


```python
from jippy.esg.yahoo_esg import *
```

#### <i>get\_esg\_data( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
get_esg_data('AAPL')
```

<i> Output </i>

<center><small><small>

|    | date       |   total\_esg\_risk_score | risk\_category   | risk\_percentile   |   environment\_risk_score |   social\_risk\_score |   ... |
|---:|:-----------|-----------------------:|:----------------|:------------------|-------------------------:|--------------------:|------------------------:|
|  0 | 2020-08-25 |                     24 | Medium          | 33rd              |                      0.5 |                  13 |                    ... | 

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>


#### <i>get\_corporate\_governance\_score( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
get_corporate_governance_score('AAPL')
```

<i> Output </i>

<center><small><small>

|    |   audit |   board |   shareholder\_rights |   compensation |   quality\_score | ticker   | date       |
|---:|--------:|--------:|---------------------:|---------------:|----------------:|:---------|:-----------|
|  0 |       1 |       1 |                    1 |              3 |               1 | AAPL     | 2020-08-25 |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>



## <li> Company info </li>



<div align="right"><a href="#0">Back to top</a> </div>


#### <i>get\_profile( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
get_profile('AAPL')
```

<i> Output </i>

<center><small><small>

|    | company\_name   | sector     | industry             |   number\_of\_employees | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ticker   |
|---:|:---------------|:-----------|:---------------------|----------------------:|:----------|:---------|
|  0 | Apple Inc.     | Technology | Consumer Electronics |                137000 | Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide...  | AAPL     |

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


#### <i>get\_executives_info( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li> </li>
</ul>

<i> Example </i>

```python
get_executives_info('AAPL')
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

## <div id="B2"> Price data </div>

<div align="right"><a href="#0">Back to top</a> </div>


### <u>Yahoo Finance price data</u>
```python
from jippy.price_data.yahoo_price_data import *
```

#### <i>get\_yahoo\_prices( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
get_yahoo_prices('AAPL')
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

</small></small></center>

<div align="right"> <a href="#F2">To index</a> </div>


#### <i>get\_yahoo\_option_chain( ticker )</i>

<ul>
<li>The input is a valid company ticker.</li>
<li></li>
</ul>

<i> Example </i>

```python
calls, puts = get_yahoo_option_chain('AAPL')
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


<div align="right"><a href="#0">Back to top</a> </div>

### <u>Investing.com price data</u>
```python
from jippy.price_data.investing_com_price_data import *
```

#### <i>get\_investing\_com( url )</i>

<ul>
<li></li>
<li></li>
</ul>

<div align="right"> <a href="#F2">To index</a> </div>


<div align="right"><a href="#0">Back to top</a> </div>

### <u>Price data APIs</u>
```python
from jippy.price_data.price_data_apis import *
```

#### <i>get\_alpha\_vantage\_ts( ticker, api_key )</i>

<ul>
<li></li>
<li></li>
</ul>

<div align="right"> <a href="#F2">To index</a> </div>


#### <i>get\_quandl( ticker, api_key )</i>

<ul>
<li></li>
<li></li>
</ul>

<div align="right"> <a href="#F2">To index</a> </div>

#### <i>get\_iex\_prices( ticker, api_key )</i>

<ul>
<li></li>
<li></li>
</ul>

<div align="right"> <a href="#F2">To index</a> </div>


## <div id="D2">Economic data</div>

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


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

<br>

## <li> OECD Main Economic Indicators </li>

<div align="right"><a href="#0">Back to top</a> </div>


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
oecd_goods_balance(country_code = 'USA', xm = 'balance')
```

<i> Output </i>


<center><small><small>




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


</small></small></center>

<div align = "right">  <a href="#F2">To index</a> </div>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

## <div id="E2">News data</div>


<div align="right"><a href="#0">Back to top</a> </div>

<br>


_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

## <div id="EE2">Other data</div>


<div align="right"><a href="#0">Back to top</a> </div>

<br>



## <div id="F2"> Index </div>

<ul><b>Company fundamentals</b>
<li> <a href='#f1'> get_valuation_metrics( ticker ) </a> </li>
<li> get_ratios( ticker )</li>
<li> get_income_statement( ticker )</li>
<li> get_balance_sheet( ticker )</li>
<li> get_cashflow_statement( ticker )</li>
<li> get_statements( ticker )</li>
<li> get_earnings_estimates( ticker )</li>
<li> get_earnings_estimate_trends( ticker )</li>
<li> get_earnings_history( ticker )</li>
<li> get_revenue_estimates( ticker )</li>
<li> get_growth_estimates( ticker )</li>
<b>ESG data</b>
<li> get_esg_data( ticker )</li>
<li> get_corporate_governance_score( ticker )</li>
<b>Company profile</b>
<li> get_profile( ticker )</li>
<li> get_executives_info( ticker )</li>
<b>Price data</b>
<li> get_yahoo_prices( ticker )</li>
<li> get_investing_com( url )</li>
<li> get_alpha_vantage_ts( ticker )</li>
<li> get_quandl( ticker )</li>
<li> get_iex_prices( ticker )</li>
<b>Economic data</b>
<li> </li>
<li> </li>
<b>News data</b>
<li> </li>
<li> </li>
<b>Other data</b>
<li> </li>
<li> </li>
</ul>

<div align="right"><a href="#0">Back to top</a> </div>

## <div id="G2"> Sources </div>
<li>Yahoo Finance, www.finance.yahoo.com </li>
<li>Investing.com, www.investing.com </li>
<li>MarketWatch, marketwatch.com </li>
<li>Finviz, finviz.com</li>
<li>Moore Research Center, www.mrci.com </li>
<li>OECD, data.oecd.org </li>
<li>NASDAQ, www.nasdaq.com</li>
<li>Gurufocus, www.gurufocus.com</li>
<li></li>
<li>Newspapers...</li>
<li>SEC...?</li>
<li>CBOE...?</li>
<li>VixCentral...?</li>


<div align="right"><a href="#0">Back to top</a> </div>

