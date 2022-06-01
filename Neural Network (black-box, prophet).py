#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:53:53 2022

@author: william
"""

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/william/Documents/ESME/Ingé2/Projet/btc.csv')
df['time'] = pd.to_datetime(df['time'])
#df['time'].dt.year.unique()

df.rename(columns = {'time':'ds', 'PriceUSD':'y'}, inplace = True)

#df = df.set_index('ds')
i = df.loc[df['ds'] == '2020'].index[0]

dfBTC = df[['ds', 'y']].loc[i:]

dfBTC = dfBTC.dropna()

print(dfBTC.head())


#QUICK START

m = Prophet()
m.fit(dfBTC)

future = m.make_future_dataframe(periods=365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)

fig2 = m.plot_components(forecast)


#TREND CHANGEPOINTS

from prophet.plot import add_changepoints_to_plot
fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)

m = Prophet(changepoint_prior_scale=0.5)
forecast = m.fit(dfBTC).predict(future)
fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)


m = Prophet(changepoint_prior_scale=0.001)
forecast = m.fit(dfBTC).predict(future)
fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)


'''
m = Prophet(changepoints=['2014-01-01'])
forecast = m.fit(dfBTC).predict(future)
fig = m.plot(forecast)
'''