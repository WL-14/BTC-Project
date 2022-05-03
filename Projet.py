# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:41:21 2022

@author: PHAM
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

btc_data=pd.read_csv('btc.csv',parse_dates=True)

#Exploring Dataframe
print(btc_data.head())
print(btc_data.shape)
print(btc_data.info())
btc_data['time']=pd.to_datetime(btc_data['time'])
btc_data['time'].dt.year.unique()
#btc_data=btc_data.loc['2017-01-01':'2022-04-01']
"""
#96à103 SplyAdrBal1in1K: La somme de toutes les unités natives détenues dans des 
adresses dont le solde était d'au moins un sur X de l'offre actuelle d'unités 
natives à la fin de la journée. Seules les unités natives sont prises en compte 
(par exemple, une adresse avec moins de X ETH mais avec plus de X dans les 
 jetons ERC-20 ne serait pas prise en compte). 
La comparaison est effectuée en utilisant une comparaison supérieure ou égale 
(une adresse possédant exactement 1/1000e de l'offre compte pour SplyAdrBal1in1K)
Pour un jour J, les soldes sont prélevés en fin de journée.
"""

print(btc_data['SplyAdrBal1in1K'].describe())
x = btc_data['SplyAdrBal1in1K']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#

print(btc_data['SplyAdrBal1in10K'].describe())
x = btc_data['SplyAdrBal1in10K']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#

print(btc_data['SplyAdrBal1in1M'].describe())
x = btc_data['SplyAdrBal1in1M']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBal1in10M'].describe())
x = btc_data['SplyAdrBal1in10M']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBal1in100M'].describe())
x = btc_data['SplyAdrBal1in100M']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBal1in1B'].describe())
x = btc_data['SplyAdrBal1in1B']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBal1in10B'].describe())
x = btc_data['SplyAdrBal1in10B']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Pour une adresse possédant exactement 1/1M ou moins de l'offre, la courbe est
#plus ou moins identique. Elle montre une évolution progressive de 2010 jusqu'à
#2022 jusqu'à atteindre 1,6*10^7 adresses possédant exactement 1/1Me de l'offre
#et un peu plus de 1,75 adresses possèdent exactement 1/[10M,100M,1B,10B]e de 
#l'offre. On remarque que quotidiennement, énormément d'adresses possèdent une
#infime partie de la somme de toutes les unités natives. On en déduit que ces
#unités ne sont pas concentrés par des particuliers mais au contraire, cette
#richesse est décentralisée.

"""
#104à114 SplyAdrBalNtv0,001: La somme de toutes les unités natives détenues 
dans des adresses dont le solde était égal ou supérieur à X unités natives à la 
fin de la journée. Seules les unités natives sont prises en compte 
(par exemple, une adresse avec moins de X ETH mais avec plus de X dans les 
 jetons ERC-20 ne serait pas prise en compte).
Cette métrique décompose l'offre d'un actif par le solde des adresses qui le possèdent.
La comparaison est effectuée en utilisant une comparaison supérieure ou égale 
(une adresse possédant exactement 1 unité native compte pour SplyAdrBalNtv1).
"""

print(btc_data['SplyAdrBalNtv0.001'].describe())
x = btc_data['SplyAdrBalNtv0.001']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalNtv0.01'].describe())
x = btc_data['SplyAdrBalNtv0.01']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalNtv0.1'].describe())
x = btc_data['SplyAdrBalNtv0.1']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalNtv1'].describe())
x = btc_data['SplyAdrBalNtv1']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalNtv10'].describe())
x = btc_data['SplyAdrBalNtv10']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Pour une adresse possédant exactement 0,001 ... 10 unités natives, la courbe est
#plus ou moins identique. Elle montre une évolution progressive de 2010 jusqu'à
#2022 jusqu'à atteindre [1,6;1,75]*10^7 adresses possédant exactement
#0.001/0.01/.../10 unités natives. Ces données sont similaires à ceux
#du SplyAdrBal1in10B (jusqu'à 1M). Elles semblent être corrélées.

print(btc_data['SplyAdrBalNtv100'].describe())
x = btc_data['SplyAdrBalNtv100']
y = btc_data['time']
plt.plot(y, x)
plt.show()
#

print(btc_data['SplyAdrBalNtv1K'].describe())
x = btc_data['SplyAdrBalNtv1K']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#SplyAdrBal1in10K

print(btc_data['SplyAdrBalNtv10K'].describe())
x = btc_data['SplyAdrBalNtv10K']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#SplyAdrBal1in1K
S
print(btc_data['plyAdrBalNtv100K'].describe())
x = btc_data['SplyAdrBalNtv100K']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#On va s'intéresser à cette courbe à partir de 2017.
#Il y a des pics descendants vers fin 2017, mi-2019 et début 2021.
#On remarque que ces pics descendants correspondent en fait à des pics du cours
#du Bitcoin soit en Décembre 2017, Juillet 2019 et la période Janvier-Avril 2021.
#Ce sont à ces périodes que les utilisateurs vendent leur BTC alors que ce dernier
#avait atteint des pics historiques. On remarque encore à travers ces données
#que le bitcoin n'est pas du tout centralisé et qu'il est réparti entre de
#milliards d'adresses. De plus, on remarque que ce sont les utilisateurs avec le
#plus d'unités qui font le plus d'échange.

print(btc_data['SplyAdrBalNtv1M'].describe())
x = btc_data['SplyAdrBalNtv1M']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Donnée nulle ==> Pas intéressante

"""
#115à123 SplyAdrBalUSD1: La somme de toutes les unités natives détenues dans 
des adresses dont le solde était de X $ ou plus à la fin de la journée. 
Seules les unités natives sont prises en compte (par exemple, une adresse avec 
moins de X ETH mais avec plus de X dans les jetons ERC-20 ne serait pas prise en compte).
Cette métrique décompose l'offre d'un actif par le solde en USD des adresses qui le possèdent.
Pour un jour J, les soldes sont prélevés à la fin de ce jour, le cours utilisé 
est le cours de clôture de ce jour également.
La comparaison est effectuée en utilisant une comparaison supérieure ou égale 
(une adresse possédant exactement 1 $ compte pour SplyAdrBalUSD1).
"""

print(btc_data['SplyAdrBalUSD1'].describe())
x = btc_data['SplyAdrBalUSD1']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalUSD10'].describe())
x = btc_data['SplyAdrBalUSD10']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalUSD100'].describe())
x = btc_data['SplyAdrBalUSD100']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalUSD1K'].describe())
x = btc_data['SplyAdrBalUSD1K']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalUSD10K'].describe())
x = btc_data['SplyAdrBalUSD10K']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalUSD100K'].describe())
x = btc_data['SplyAdrBalUSD100K']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#On remarquera les tendances sont fortements similaires à partir de 2017.
#Aussi, on en déduira des données précédentes que le nombre d'utilisateurs
#augmentent de plus en plus. Ces 3 données nous montrent une certaine
#corrélation entre elles.

print(btc_data['SplyAdrBalUSD1M'].describe())
x = btc_data['SplyAdrBalUSD1M']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrBalUSD10M'].describe())
x = btc_data['SplyAdrBalUSD10M']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Sur les 2 graphiques où les adresses possèdent plus de 1M$, on remarque des pics
#au mêmes moments que celui du cours du BitCoin. On peut donc assimiler la richesse
#de ces adresses à la variation du cours du BitCoin puisqu'elle baisse aussi de
#la même manière.

"""
#124 SplyAdrTop100: La somme de toutes les unités natives détenues par les 
100 adresses les plus riches à la fin de cet intervalle de temps.
#125&126 SplyAdrTop10Pct: La somme de toutes les unités natives détenues par 
les 1 % d'adresses supérieures par solde à la fin de cet intervalle de temps.

"""

print(btc_data['SplyAdrTop100'].describe())
x = btc_data['SplyAdrTop100']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Correspond à SplyAdrBalNtv10K. Ceux ayant 10k ou plus d'unités natives 
#feraient partie du top100. 

print(btc_data['SplyAdrTop10Pct'].describe())
x = btc_data['SplyAdrTop10Pct']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['SplyAdrTop1Pct'].describe())
x = btc_data['SplyAdrTop1Pct']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#On remarque que l

"""
#127 SplyCur: La somme de toutes les unités natives jamais créées et actuellement 
visibles sur le grand livre (c'est-à-dire émises) à ce jour. Pour les protocoles 
basés sur des comptes, seuls les comptes avec des soldes positifs sont comptés.
Cette métrique peut également être qualifiée d'"offre totale émise" car elle 
capture la somme de toutes les unités natives visibles dans le grand livre 
jusqu'au point de calcul de la métrique.
Pour les chaînes de comptes, l'offre actuelle est la somme de tous les soldes de comptes.
"""

print(btc_data['SplyCur'].describe())
x = btc_data['SplyCur']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Il y a eu une augmentation progressive d'unités natives placées sur le marché de
#la cryptomonnaie atteingnant à ce jour environ 19M d'unités. Il semblerait que
#cette croissance continue après 2022.

"""
#128 SplyExpFut10yr: La somme de toutes les unités natives comptant l'offre 
actuelle et incluant toutes celles qui devraient être émises au cours des 
10 prochaines années à partir de ce jour si le calendrier d'émission continu 
connu actuel est suivi. Les futurs hard-forks attendus qui modifieront l'émission 
continue ne sont pas pris en compte avant le jour où ils sont activés/appliqués.
"""

print(btc_data['SplyExpFut10yr'].describe())
x = btc_data['SplyExpFut10yr']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#

"""
#129 SplyFF: La somme de toutes les unités natives jamais créées et visibles sur 
le grand livre, à l'exclusion des unités natives détenues étroitement par des 
initiés de l'entreprise, des investisseurs contrôlant et des détenteurs 
stratégiques à long terme à ce jour.Free Float Supply est une mesure de l'offre 
qui exclut les jetons détenus étroitement par les initiés de l'entreprise, 
les investisseurs contrôlant et les détenteurs stratégiques à long terme. 
Cela inclut les jetons d'entreprise, de fondation blockchain et de membre de 
l'équipe fondatrice qui peuvent ou non être soumis à des séquestres. 
En outre, Free Float Supply exclut également les grands portefeuilles de jetons 
brûlés et les fonds qui ont été manifestement perdus.
"""

print(btc_data['SplyFF'].describe())
x = btc_data['SplyFF']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#

"""
#130&131 SplyMiner0HopAllNtv/USD: La somme des soldes de toutes les entités minières/USD. 
Une entité minière est définie comme une adresse qui a été créditée à partir 
d'une transaction débitant les comptes 'FEES' ou 'ISSUANCE' conformément au modèle 
de données Universal Blockchain (UBDM) de Coin Metric.
"""

print(btc_data['SplyMiner0HopAllNtv'].describe())
x = btc_data['SplyMiner0HopAllNtv']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#On observe que le nombre d'entités minières augmentent fortement en 2010 jusqu'à
#2011 pour une quantité de 2,6M mais baisse cependant à hauteur de 2,1M vers fin 2011.
#On constate un pic maximum en 2012 qui pourrait être due au premier halving
#(réduction de moitié de la récompense de minage de Bitcoins) qui a eu lieu, 
#passant de 50 à 25 BTC.

print(btc_data['SplyMiner0HopAllUSD'].describe())
x = btc_data['SplyMiner0HopAllUSD']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Le marché du BTC à commencer à exploser vers fin 2017 avec un premier pic à 40Mi 
#où elle voit une perte de vitesse pour connaître une ascension fulgurante en 2019.
#Lors de la crise COVID, elle stagne un peu. Enfin, le halving du Bitcoin, 
#procédé qui divise par deux la récompense offerte pour le minage d’un bloc de 
#Bitcoin et qui se tient tous les quatre ans a fatalement des retombées économiques 
#importantes, menant généralement à une hausse massive du prix du BTC. 

"""
#134&135 TxCnt/TxCntSec: Le nombre total de transactions ce jour-là. Les transactions représentent 
un ensemble d'actions destinées à modifier le registre initiées par un utilisateur 
(humain ou machine). À certaines occasions, les transactions sont comptabilisées, 
qu'elles entraînent ou non le transfert d'unités autochtones. 
Tant que ces transactions sont enregistrées sur la chaîne, elles seront incluses 
dans le calcul de cette métrique. Les modifications du registre mandatées de manière 
algorithmique par le protocole, telles que les transactions coinbase ou les nouvelles 
émissions post-lancement, ne sont pas incluses ici.
"""

print(btc_data['TxCnt'].describe())
x = btc_data['TxCnt']
y = btc_data['time']
plt.plot(y, x)
plt.show()
print(btc_data['TxCntSec'].describe())
x = btc_data['TxCntSec']
y = btc_data['time']
plt.plot(y, x)
plt.show()
#Same Comment

"""
#136 TxTfrCnt: Le nombre total de transferts de cet intervalle. Une transaction 
est composée d'un ou plusieurs transferts entre différentes entités. Une seule 
transaction peut contenir des dizaines de transferts distincts, qui représentent 
les mouvements d'unités natives d'une entité comptable vers une autre entité 
comptable distincte. Seuls les transferts qui ont une valeur positive (non nulle) 
sont comptabilisés. Les transferts sont familièrement appelés "paiements".
"""

print(btc_data['TxTfrCnt'].describe())
x = btc_data['TxTfrCnt']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#On remarque qu'entre 2017 et 2022, ce nombre de transferts fluctue entre 0.1 et 0.5.
#Cependant, des pics sont présents à la suite de la baisse du cours du BTC.

"""
#137&138 TxTfrValAdjUSD/Ntv: La valeur en USD/unité native de la somme des unités natives 
transférées ce jour-là en supprimant le bruit et certains artefacts.
"""

print(btc_data['TxTfrValAdjNtv'].describe())
x = btc_data['TxTfrValAdjNtv']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Bruit ? 

print(btc_data['TxTfrValAdjUSD'].describe())
x = btc_data['TxTfrValAdjUSD']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#

"""
#139&140 TxTfrValMeanNtv/USD: La valeur totale des unités natives/USD transférées 
divisée par le nombre de transferts (c'est-à-dire la taille moyenne d'un transfert) 
entre des adresses distinctes à cet intervalle.
"""

print(btc_data['TxTfrValMeanNtv'].describe())
x = btc_data['TxTfrValMeanNtv']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Non pertinent

print(btc_data['TxTfrValMeanUSD'].describe())
x = btc_data['TxTfrValMeanUSD']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Une concentration autour de fin 2021 - début 2022 dont une moyenne de transfert
#atteignant une taille de 500K en 2021. On peut supposer qu'il y a eu un nombre
#important de transfert d'unités natives.

"""
#141&142 TxTfrValMedNtv/USD: Le nombre médian d'unités natives/USD transférées par 
transfert (c'est-à-dire la "taille" médiane d'un transfert) ce jour-là.
"""

print(btc_data['TxTfrValMedNtv'].describe())
x = btc_data['TxTfrValMedNtv']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Non pertinent

print(btc_data['TxTfrValMedUSD'].describe())
x = btc_data['TxTfrValMedUSD']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#

"""
#143 VtyDayRet180d: La volatilité X jours, mesurée comme l'écart des rendements logarithmiques
"""

print(btc_data['VtyDayRet180d'].describe())
x = btc_data['VtyDayRet180d']
y = btc_data['time']
plt.plot(y, x)
plt.show()

#Le BTC est très volatile. Son prix varie brutalement. 