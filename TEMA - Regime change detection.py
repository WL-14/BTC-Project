#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:09:16 2022

@author: william
"""

#INITIALISATION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns

df = pd.read_csv('/Users/william/Documents/ESME/Ingé2/Projet/btc.csv')
df['time'] = pd.to_datetime(df['time'])
#df['time'].dt.year.unique()
df = df.set_index('time')

dfBTC = df['PriceUSD'].loc['2020':'2021']

#REGIME CHANGE DETECTIION 50 JOURS

BTCMME = dfBTC.ewm(span=50).mean()

'''
#TRIX
    
TRIX = []
indexTRIX = []

for i in range(1, len(BTCMME)):
    TRIX.append((BTCMME[i] / BTCMME[i-1]) - 1)
    indexTRIX.append(BTCMME.index[i])

plt.figure(figsize = (15,7))   
plt.plot(indexTRIX, TRIX)
'''

#TEMA

EMA1 = dfBTC.ewm(span=50).mean()
EMA2 = EMA1.ewm(span=50).mean()
EMA3 = EMA2.ewm(span=50).mean()

TEMA = (3*EMA1)-(3*EMA2)+EMA3

fig, ax = plt.subplots(figsize = (15, 7))
ax.plot(dfBTC, linestyle='-', linewidth=0.7, label='Daily')
ax.plot(EMA1, color = 'red', linewidth=1.7, label='EMA')
ax.plot(TEMA, color = 'blue', linewidth=1.7, label='TEMA')
ax.legend();

plt.figure(2)
temaAngle = np.degrees(np.arctan(TEMA.diff()/50))
temaAngle.plot(figsize = (15, 7))

#Trouver angle TEMA avec tangente

