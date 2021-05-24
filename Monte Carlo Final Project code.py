# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:19:15 2021

@author: tmali
"""

import pandas as pd
import numpy as np
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style 

style.use("ggplot")

start = dt.datetime(2020, 2, 15)
end = dt.datetime(2021, 4, 25)

prices = web.DataReader('BA', 'yahoo', start, end)["Close"]
returns = prices.pct_change()
last_price = prices[-1]

num_trials = 1000
num_days = 252 

simulation_df = pd.DataFrame()

for x in range(num_trials):
    count = 0
    daily_vol = returns.std()
    price_series = []
    
    price = last_price *(1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
        
    simulation_df[x] = price_series
    
fig = plt.figure()
fig.suptitle("Monte Carlo Simulation: BA ")
plt.plot(simulation_df)
plt.axhline( y= last_price, color = 'b', linestyle='-')
plt.xlabel('day')
plt.ylabel('price')
plt.show()
