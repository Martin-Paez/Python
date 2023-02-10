import matplotlib.pyplot as plt
from mpl_finance import candlestick2_ohlc
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

import datetime as dt

# crear un DataFrame con los datos de ejemplo
df = pd.DataFrame({'Open': [23000, 23100, 22000, 22100, 23200],
                   'High': [23100, 23200, 22100, 22200, 23300],
                   'Low': [22900, 22000, 21900, 22000, 22100],
                   'Close': [23000, 22100, 21900, 22100, 23200],
                   'Date': ['1980-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']})

# convertir la columna 'Date' a formato de fecha
df['Date'] = pd.to_datetime(df['Date'])

# establecer la columna 'Date' como el índice del DataFrame
df.set_index('Date', inplace=True)

# convertir los valores en milésimas
df = df/100000

# graficar los datos como velas
fig, ax = plt.subplots()

candlestick2_ohlc(ax, df['Open'], df['High'], df['Low'], df['Close'], width=0.6, colorup='g', colordown='r')

# Agrega etiquetas y títulos
plt.xlabel("Fecha")
plt.ylabel("Precio (USD)")
plt.title("Gráfico de velas de Bitcoin en Binance")

# mostrar la gráfica

plt.show()

np.random.seed(1)

N = 24
y = np.random.rand(N)

now = dt.datetime.now()
then = now + dt.timedelta(days=24)
days = mdates.drange(now,then,dt.timedelta(days=1))


fig = plt.figure()
ax = fig.add_subplot(111)
    
ax.plot(days,y)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=6))
ax.tick_params(axis='x', labelrotation=45)

plt.show()