#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 01:41:55 2022

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


#REGIME CHANGE DETECTIION 50 JOURS

dfBTC = df['PriceUSD'].loc['2020':'2021']

BTCMme50Jours = dfBTC.ewm(span=50).mean()

PrixBTC = 0
MME50 = 0
nbChangement = 0
listeChange50 = []
#prix50 = []
gainsTot50 = 0

for i in range(len(dfBTC)-1):
    PrixBTC = dfBTC.iloc[i]
    MME50 = BTCMme50Jours.iloc[i]
    
    PrixBTCD = dfBTC.iloc[i+1]
    MME50D = BTCMme50Jours.iloc[i+1]
    
    if PrixBTC > MME50 and PrixBTCD < MME50D:
        #print("changement de régime : BULL --> BEAR")
        #print("date", dfBTC.index[i+1])
        #print("prix", dfBTC[i+1])
        nbChangement += 1
        listeChange50.append(["Descente",dfBTC.index[i+1],dfBTC[i+1], "VENTE"])
        #prix50.append(dfBTC[i+1])
        gainsTot50 += dfBTC[i+1]
    elif PrixBTC < MME50 and PrixBTCD > MME50D:
        #print("changement de régime : BEAR --> BULL")
        #print("date", dfBTC.index[i+1])
        #print("prix", dfBTC[i+1])
        nbChangement += 1
        listeChange50.append(["Monte",dfBTC.index[i+1],dfBTC[i+1], "ACHAT"])
        #prix50.append(-dfBTC[i+1])
        gainsTot50 -= dfBTC[i+1]
        
print("nombre de changement : ", nbChangement)
print("gains totaux : ", gainsTot50)

#LISTE TRANSACTIONS 50
listeTransac50 = []
for i in range(0, len(listeChange50)-1, 2):
    p1 = listeChange50[i][2]
    p2 = listeChange50[i+1][2]
    listeTransac50.append(p2-p1)
    

#REGIME CHANGE DETECTIION 200 JOURS

BTCMme200Jours = dfBTC.ewm(span=200).mean()

PrixBTC = 0
MME200 = 0
nbChangement = 0
listeChange200 = []
gainsTot200 = 0

for i in range(len(dfBTC)-1):
    PrixBTC = dfBTC.iloc[i]
    MME200 = BTCMme200Jours.iloc[i]
    
    PrixBTCD = dfBTC.iloc[i+1]
    MME200D = BTCMme200Jours.iloc[i+1]
    
    if PrixBTC > MME200 and PrixBTCD < MME200D:
        #print("changement de régime : BULL --> BEAR")
        #print("date", dfBTC.index[i+1])
        #print("prix", dfBTC[i+1])
        nbChangement += 1
        listeChange200.append(["Descente",dfBTC.index[i+1],dfBTC[i+1], "VENTE"])
        gainsTot200 += dfBTC[i+1]
    elif PrixBTC < MME200 and PrixBTCD > MME200D:
        #print("changement de régime : BEAR --> BULL")
        #print("date", dfBTC.index[i+1])
        #print("prix", dfBTC[i+1])
        nbChangement += 1
        listeChange200.append(["Monte",dfBTC.index[i+1],dfBTC[i+1], "ACHAT"])
        gainsTot200 -= dfBTC[i+1]
        
print("nombre de changement : ", nbChangement)
print("gains totaux : ", gainsTot200)

#LISTE TRANSACTIONS 200
listeTransac200 = []
for i in range(0, len(listeChange200)-1, 2):
    p1 = listeChange200[i][2]
    p2 = listeChange200[i+1][2]
    listeTransac200.append(p2-p1)

#PLOT

fig, ax = plt.subplots(figsize = (15, 7))
ax.plot(dfBTC.loc['2020-04'], linestyle='-', linewidth=0.7, label='Daily')
ax.plot(BTCMme50Jours.loc['2020-04'], color = 'blue', linewidth=1.7, label='MME 50 Jours')
ax.legend();
