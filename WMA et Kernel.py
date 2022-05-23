# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:41:21 2022

@author: PHAM
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt

df=pd.read_csv('btc.csv',parse_dates=True)
df['time'] = pd.to_datetime(df['time'])
df = df.set_index('time')

df2017 = df.loc['2019-02-01':'2019-04-30']
ts = df2017['PriceUSD']

#WMA
def wma(df, column='PriceUSD', n=180, add_col=False):
    weights= np.arange(1, n+1)
    wmas= df[column].rolling(n).apply(lambda x: np.dot(x,weights) / weights.sum(), raw=True)
    
    if add_col==True:
        df[f'{column}_WMA_{n}']= wmas
        return df
    else:
        return wmas


BTC_WMA=wma(df2017)
fig, ax = plt.subplots(figsize = (15, 7))
ax.plot(df2017["PriceUSD"], linestyle='-', linewidth=0.7, label='Daily')
ax.plot(BTC_WMA, color = 'red', linewidth=1.7, label='WMA n jours')
ax.legend();


PrixBTC = 0
MME50 = 0
nbChangement = 0
listeChange50 = []
#prix50 = []
gainsTot50 = 0

for i in range(len(ts)-1):
    PrixBTC = ts.iloc[i]
    WMA_BTC = BTC_WMA.iloc[i]
    
    PrixBTCD = ts.iloc[i+1]
    WMA_BTCD = BTC_WMA.iloc[i+1]
    
    if PrixBTC > WMA_BTC and PrixBTCD < WMA_BTCD:
        #print("changement de régime : BULL --> BEAR")
        #print("date", dfBTC.index[i+1])
        #print("prix", dfBTC[i+1])
        nbChangement += 1
        listeChange50.append(["Descente",ts.index[i+1],ts[i+1], "VENTE"])
        #prix50.append(dfBTC[i+1])
        gainsTot50 += ts[i+1]
    elif PrixBTC < WMA_BTC and PrixBTCD > WMA_BTCD:
        #print("changement de régime : BEAR --> BULL")
        #print("date", dfBTC.index[i+1])
        #print("prix", dfBTC[i+1])
        nbChangement += 1
        listeChange50.append(["Monte",ts.index[i+1],ts[i+1], "ACHAT"])
        #prix50.append(-dfBTC[i+1])
        gainsTot50 -= ts[i+1]
        
print("nombre de changement : ", nbChangement)
print("gains totaux : ", gainsTot50)

#LISTE TRANSACTIONS 50
listeTransac50 = []
for i in range(0, len(listeChange50)-1, 2):
    p1 = listeChange50[i][2]
    p2 = listeChange50[i+1][2]
    listeTransac50.append(p2-p1)


#RUPTURE
n_breaks = 20
y = np.array(ts.tolist())
model = rpt.KernelCPD(kernel="linear", min_size=2).fit(y)
breaks = model.predict(n_bkps=n_breaks-1)
breaks_rpt = []
for i in breaks:
    breaks_rpt.append(ts.index[i-1])
breaks_rpt = pd.to_datetime(breaks_rpt)
breaks_rpt

plt.plot(ts, label='data')
plt.title('PriceUSD')
print_legend = True
for i in breaks_rpt:
    if print_legend:
        plt.axvline(i, color='red',linestyle='dashed', label='breaks')
        print_legend = False
    else:
        plt.axvline(i, color='red',linestyle='dashed')
plt.grid()
plt.legend()
plt.show()
