# -*- coding: utf-8 -*-
import pymysql
import sqlalchemy as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from klinesReq import KlinesDB

#plt.style.use('seaborn-darkgrid')

#leer datos
#df_raw = pd.read_cvs('BTCUSDT4h.csv')
df_raw = KlinesDB.instantiate('BTCUSDT', '4h').read()

#limpiarlos y dar formato
df = df_raw[['Close_Timestamp','Close']].copy()
df['Close_Timestamp'] = pd.to_numeric(df['Close_Timestamp'])
df['Close'] = pd.to_numeric(df['Close'])
df.set_index('Close_Timestamp', inplace=True)
df.plot()

#Calcular metricas (Bandas de Bollinger)
def b_bands(df,n):
    MA = pd.Series.rolling(df['Close'],n).mean()
    MSD = pd.Series.rolling(df['Close'],n).std()
    b1 = MA + (MSD*2)
    B1 = pd.Series(b1, name = 'BB_' + str(n))
    df = df.join(B1)
    b2 = MA - (MSD*2)
    B2 = pd.Series(b2, name = 'Bb_' + str(n))
    df = df.join(B2)
    MA = pd.Series(MA, name = 'MM_' + str(n))
    df = df.join(MA)
    return df

#Calcular a 56hs
n = 26
df_bb = b_bands(df,n)
df_bb.plot()

#Zoom
df_bb.iloc[-100:,:].plot()
plt.show()

#Crear señales
df_bb['side'] = np.nan

long_signals = (df_bb['Close'] <= df_bb['Bb_' + str(n)])
short_signals = (df_bb['Close'] >= df_bb['BB_' + str(n)])

df_bb.loc[long_signals, 'side'] = 1
df_bb.loc[short_signals, 'side'] = -1

#Revisar carga de la estrategia
print(df_bb.side.value_counts())

#Agregar Lag a nuestra señal
df_bb['side'] = df_bb['side'].shift(1)

#calcular retornos
df_bb['Returns'] = np.log(df_bb['Close']).diff()

#Calcular posiciones teoricas
df_bb['Position_sum'] = df_bb['side'].fillna(0).cumsum()
df_bb['Position_sum'].plot()
plt.show()

#Seleccionar un periodo de prueba
interval = 4
candles = int((24/4)*31)
df_test =   df_bb.iloc[:candles,:].copy()
df_test['Cum_prod'] = (1 + df_test['Returns']).cumprod()
df_test['Cum_prod'].plot()
df_test['side'] = df_test['side'].fillna(0)

#Plot Basico
df_test[['Close', 'Bb_' + str(n), 'BB_' + str(n)]].plot()

#Crear un nuevo plot con señales
df_test['Buy_Signal'] = df_test.apply(lambda x: x.Close if x.side == 1 else np.nan, axis=1)
df_test['Sell_Signal'] = df_test.apply(lambda x: x.Close if x.side == -1 else np.nan, axis=1)

fig = plt.figure(figsize = (16,8))
ax1 = plt.subplot()
plt.plot(df_test.index, df_test.Close)
plt.plot(df_test.index, df_test['Bb_' + str(n)])
plt.plot(df_test.index, df_test['BB_' + str(n)])
plt.scatter(x=df_test.index, y=df_test['Buy_Signal'], marker='^', color='g' )
plt.scatter(x=df_test.index, y=df_test['Sell_Signal'], marker='^', color='r' )
plt.legend()
plt.grid(True)
plt.title('Estrategia con Bandas de Bollinger par BTC-USDT')
plt.show()

#Valores iniciales de la estrategia
backtest = []
f_unidades = 1
f_tick = 'BTC'
tick = 'USDT'
initial_cash = 50000
initial_position = 0
initial_holdings = 0
initial_total = 50000

backtest.append([initial_cash, initial_position, df_test['Close'].iloc[0], 
                  initial_holdings, initial_total])
 
for idx,row in df_test.iterrows():
    #Reglas de lado
    precio = row['Close']
    if row['side'] == 0:
        backtest.append([initial_cash, initial_position, precio, 
                         initial_holdings, initial_total])
        continue
    
    elif row['side'] == 1:
        if initial_cash - (precio * f_unidades) < 0:
            print(f'USDT: {initial_cash},  BTC: {initial_position}')
            backtest.append([initial_cash, initial_position, precio, 
                             initial_holdings, initial_total])
            continue
        print('----------------------')
        print(f'COMPRANDO {f_unidades} de {f_tick} a precio {precio} {tick}')
        initial_cash = initial_cash - (precio * f_unidades)
        print(f'Actualizando Cash')
        print(f'Cash disponible: {initial_cash}')
        initial_position = initial_position + f_unidades
        print(f'Posicion acutal: {initial_position}')
        #Reglas de cash
        initial_holdings = (precio * initial_position)
        
        initial_total = initial_cash + initial_holdings
        backtest.append([initial_cash, initial_position, precio,
                        initial_holdings, initial_total])
    elif row['side'] == -1:
        if initial_position - f_unidades < 0 :
            print(f'USDT: {initial_cash},  BTC: {initial_position}.')
            backtest.append([initial_cash, initial_position, precio, 
                             initial_holdings, initial_total])
            continue
            
        print('----------------------')
        print(f'VENDIENDO {f_unidades} de {f_tick} a {precio} {tick}')
        initial_cash = initial_cash + (precio * f_unidades)
        print(f'Actualizado Cash')
        print(f'Cash disponible: {initial_cash}')
        initial_position = initial_position - f_unidades
        print(f'Posicion acutal: {initial_position}')
        #Reglas de cash
        initial_holdings = (precio * initial_position)
        
        initial_total = initial_cash + initial_holdings
        backtest.append([initial_cash, initial_position, precio,
                        initial_holdings, initial_total])
            
back_test = pd.DataFrame(backtest)
back_test.columns = ['Cash(USDT)', 'Posiciones', 'Precio Cierre',
                     'Valor Posiciones', 'Cash + Valor Pos']
back_test['Cash + Valor Pos'].plot()

print('----------------------')
#retorno = (back_test['Cash(USDT)'].iloc[-1] - 1) * 100
i = back_test['Cash + Valor Pos'].iloc[1]
print(f'Cash inicial: {i}')
f = back_test['Cash + Valor Pos'].iloc[-1]
print(f'Cash final: {f}')
retorno = ((f / i)-1) * 100
print(f'Retorno de la estrategia {retorno} %')

print('----------------------')
retorno_buy_hold = ((df_test['Close'].iloc[-1] / df_test['Close'].iloc[0])-1)*100
print(f'Retorno buy-hold: {retorno_buy_hold} %')


