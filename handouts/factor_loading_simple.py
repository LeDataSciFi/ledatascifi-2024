###############################################################################
# this .py file is here just so you can contrast it with the ipynb file 
# with the same name
###############################################################################


# # Estimating CAPM
# 
# - This file can estimate CAPM for any firms that Yahoo has ticker data for.
# - As written, it will estimate beta separately _for each calendar year_ in the date range you give it. But you can adjust it
# 
# - _Caveat: Yahoo Finance is more of a "quick and dirty" way to get return data. WRDS has more accurate return data._


#!pip install pandas_datareader # uncomment and run this ONE TIME ONLY to install pandas data reader

import pandas as pd
import numpy as np
import pandas_datareader as pdr # you might need to install this (see above)
from datetime import datetime


# ## Load asset return data 
# 
# Load your stock returns. This file uses yahoo finance.
# The returns don't even have to be firms! They can be any asset. (Portfolios, mutual funds, crypto, …)

# choose your firms and years 
stocks = ['SBUX','AAPL','MSFT']
start  = datetime(2016, 1, 1)
end    = datetime(2016, 12, 31)

# download stock prices 
# here, from yahoo: not my fav source, but quick. 
# we need to do some data manipulation to get the data ready 
stock_prices = pdr.get_data_yahoo(stocks, start=start, end=end)
stock_prices = stock_prices.filter(like='Adj Close') # reduce to just columns with this in the name
stock_prices.columns = stocks # put their tickers as column names
stock_prices # uncomment to print and see

# this is wide data... so if we want to create a new variable, 
# then we have to do it once for each firm...
# what if we have 1000 firms? seems tough to do...
# make long/tidy:
stock_prices = stock_prices.stack().swaplevel().sort_index().reset_index()
stock_prices.columns = ['Firm','Date','Adj Close']
stock_prices # print - now that is formatted nicely, like CRSP! 

# add return var = pct_change() function compares to prior row
# EXCEPT: don't compare for first row of one firm with last row of prior firm!
# MAKE SURE YOU CREATE THE VARIABLES WITHIN EACH FIRM - use groupby
stock_prices['ret'] = stock_prices.groupby('Firm')['Adj Close'].pct_change()
stock_prices['ret'] = stock_prices['ret'] *100 # convert to p.p. to match FF's convention on scaling (daily % rets)
stock_prices

# this shows that my "groupby" approach works, because 
# count of ret = count of adj close MINUS # of firms 
# meaning that the first day for each firm has no return data
stock_prices.describe() 


# ## Get the factor returns 
# 
# Above, we got the asset returns, $r_i$. 
# 
# To estimate $\alpha$ and $\beta$ in $r_i-r_f = \alpha + \beta (r_m-r_f)$, we need $(r_m-r_f)$ and $r_f$. Let's download those now.
# 
# Note: $(r_m-r_f)$ is the excess return on the market, which is _one_ "factor". Modern asset pricing typically uses 5 factors in tests.

# We need (r_mkt - rf), and rf
# the Fama French data library is a benchmark asset pricing dataset 
ff = pdr.get_data_famafrench('F-F_Research_Data_5_Factors_2x3_daily',start=start,end=end)[0] # the [0] is because the imported obect is a dictionary, and key=0 is the dataframe
ff = ff.reset_index().rename(columns={"Mkt-RF":"mkt_excess"})
ff


# ## Merge the asset and factor returns 

assets_and_factors = pd.merge(
    left=stock_prices,
    right=ff,
    on="Date",
    how="inner",
    indicator=True,
    validate="many_to_one",
)
assets_and_factors


# ## Estimate CAPM
# 
# So the data’s basically ready. _(We need to do two quick things below.)_
# 
# Again, the goal is to estimate, **for each** firm, **for each** year, alpha and beta, from the CAPM formula.
# 
# Well, as we've said, if you are doing a "for each" on a dataframe, that means you want to use groupby!
# 
# So, I have a dataframe, and **for each** firm, and **for each** year, I want to \<do stuff> (run regressions).
# 
# That almost directly translates to the code we need: `assets_and_factors.groupby([firm,year]).runregression()`. Except there is no "runregression" function that applies to pandas groupby objects. But we can write such a function and then `apply()` it. Meaning, our plan is to basically use this code: `assets_and_factors.groupby([firm,year]).apply(<our own reg fcn>)`.
# 
# We just need to write a reg function that works on groupby objects.

import statsmodels.api as sm


def reg_in_groupby(df, formula="ret_excess ~ mkt_excess + SMB + HML"):
    """
    Want to run regressions after groupby? E.g., repeat the regression 
    for each firm-year?
    
    This will do it! 
    
    Note: This defaults to a FF3 model assuming specific variable names. If you
    want to run any other regression, just specify your model.
    
    Usage: 
        df.groupby(<whatever>).apply(reg_in_groupby)
        df.groupby(<whatever>).apply(reg_in_groupby,formula=<whatever>)
    """
    return pd.Series(sm.formula.ols(formula, data=df).fit().params)

(
    assets_and_factors # grab the data
    
    # Two things before the regressions:
    # 1. need a year variable (to group on)
    # 2. the market returns in FF are excess returns, so 
    #    our stock returns need to be excess as well
    .assign(year = assets_and_factors.Date.dt.year,
            ret_excess = assets_and_factors.ret - assets_and_factors.RF)
    
    # ok, run the regs, so easy!
    .groupby(['Firm','year']).apply(reg_in_groupby,formula='ret_excess ~ mkt_excess')
    
    # and clean up - with better var names
    .rename(columns={'Intercept':'alpha','mkt_excess':'beta'})
    .reset_index()
)






