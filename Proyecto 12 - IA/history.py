from klinesReq import KlinesDB as kdb
df_raw = kdb.KlinesDB('BTCUSDT', '4h')
from klinesReq import KlinesDB
df_raw = KlinesDB('BTCUSDT', '4h')
from klinesReq import KlinesDB
df_raw = KlinesDB.('BTCUSDT', '4h')
df_raw = KlinesDB.instantiate('BTCUSDT', '4h')

## ---(Tue Dec 20 15:46:39 2022)---

import pymysql
import sqlalchemy as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from klinesReq import KlinesDB

#plt.style.use('seaborn-darkgrid')

#leer datos
#df_raw = pd.read_cvs('BTCUSDT4h.csv')
df_raw = KlinesDB.instantiate('BTCUSDT', '4h')

import pymysql
import sqlalchemy as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from klinesReq import KlinesDB
cls

import pymysql
import sqlalchemy as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from klinesReq import KlinesDB
runfile('C:/Users/54911/.spyder-py3/klinesReq.py', wdir='C:/Users/54911/.spyder-py3')

import pymysql
import sqlalchemy as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from klinesReq import KlinesDB
df_raw = KlinesDB.instantiate('BTCUSDT', '4h')
df = df_raw[['Close_Timestamp','Close']]#.copy()
df_raw = KlinesDB.instantiate('BTCUSDT', '4h').read()
df = df_raw[['Close_Timestamp','Close']]

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
df = df_raw[['Close_Timestamp','Close']]#.copy()
df['Close_Timestamp'] = pd.to_numeric(df['Close_Timestamp'])
df['Close'] = pd.to_numeric(df['Close'])
df.set_index('Close_Timestamp', inplace=True)
df.plot()

#Calcular metricas (Bandas de Bollinger)
def b_bands(df,n):
    MA = pd.Series(pd.Series.rolling(df['Close'],n).mean())
    MSD = pd.Series(pd.Series.rolling(df['Close'],n).std())
    b1 = MA + (MSD*2)
    B1 = pd.Series(b1, name = 'BB_' + str(n))
    df = df.join(B1)
    b2 = MA - (MSD*2)
    B2 = pd.Series(b2, name = 'Bb_' + str(n))
    df = df.join(B2)
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()
cls

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
    MA = pd.Series(pd.Series.rolling(df['Close'],n).mean())
    MSD = pd.Series(pd.Series.rolling(df['Close'],n).std())
    b1 = MA + (MSD*2)
    B1 = pd.Series(b1, name = 'BB_' + str(n))
    df = df.join(B1)
    b2 = MA - (MSD*2)
    B2 = pd.Series(b2, name = 'Bb_' + str(n))
    df = df.join(B2)
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()


df_bb.iloc[-100:,:].plot()

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
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()

#Ejemplo
df_bb.iloc[-100:,:].plot()
cls

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
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()

#Ejemplo
df_bb.iloc[-100:,:].plot()
debugfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')

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
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()

#Zoom
df_bb.iloc[-100:,:].plot()

#Crear señales
df_bb['side'] = np.nan

long_signals = (df_bb['Close'] <= df_bb['Bb_26'])
short_signals = (df_bb['Close'] >= df_bb['BB_26'])

df_bb.loc[long_signals, 'side'] = 1
df_bb.loc[short_signals, 'side'] = -1

#Revisar carga de la estrategia
print(df_bb.side.value_counts())
cls

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
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()

#Zoom
df_bb.iloc[-100:,:].plot()

#Crear señales
df_bb['side'] = np.nan

long_signals = (df_bb['Close'] <= df_bb['Bb_26'])
short_signals = (df_bb['Close'] >= df_bb['BB_26'])

df_bb.loc[long_signals, 'side'] = 1
df_bb.loc[short_signals, 'side'] = -1
cls

print(df_bb.side.value_counts())

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
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()

#Zoom
df_bb.iloc[-100:,:].plot()

#Crear señales
df_bb['side'] = np.nan

long_signals = (df_bb['Close'] <= df_bb['Bb_26'])
short_signals = (df_bb['Close'] >= df_bb['BB_26'])

df_bb.loc[long_signals, 'side'] = 1
df_bb.loc[short_signals, 'side'] = -1

#Revisar carga de la estrategia
print(df_bb.side.value_counts())

#Agregar Lag a nuestra señal
df_bb['side'] = df_bb['side'].shift(1)

#calcular retornos
df_bb['Returns'] = np.log(df_bb['Close']).diff()
df_bb['Close'].plot()

df_bb['Returns'].plot()

np.log(df_bb['Close']).plot()

df = pd.DataFrame({'numbers': list(range(0,1000))})
np.log(df).plot
df = pd.DataFrame({'numbers': list(range(0,1000))})
import pymysql
import sqlalchemy as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from klinesReq import KlinesDB
df = pd.DataFrame({'numbers': list(range(0,1000))})
np.log(df['numbers']).plot
df = pd.DataFrame({'numbers': list(range(1,1000))})
np.log(df['numbers']).plot
import pandas as pd
import numpy as np
df = pd.DataFrame({'numbers': list(range(1,1000))})
import matplotlib.pyplot as plt

# ... código para crear el marco de datos y calcular el logaritmo ...

plt.plot(np.log(df['numbers']))
plt.show()
df = pd.DataFrame({'numbers': list(range(1,1000))})
np.log(df['numbers']).plot()
cls

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
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()

#Zoom
df_bb.iloc[-100:,:].plot()

#Crear señales
df_bb['side'] = np.nan

long_signals = (df_bb['Close'] <= df_bb['Bb_26'])
short_signals = (df_bb['Close'] >= df_bb['BB_26'])

df_bb.loc[long_signals, 'side'] = 1
df_bb.loc[short_signals, 'side'] = -1

#Revisar carga de la estrategia
print(df_bb.side.value_counts())

#Agregar Lag a nuestra señal
df_bb['side'] = df_bb['side'].shift(1)

#calcular retornos
df_bb['Returns'] = np.log(df_bb['Close']).diff()

df_bb['Close'].plot()
np.log(df_bb['Close']).plot()
df_bb['Returns'].plot()

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
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()

#Zoom
df_bb.iloc[-100:,:].plot()

#Crear señales
df_bb['side'] = np.nan

long_signals = (df_bb['Close'] <= df_bb['Bb_26'])
short_signals = (df_bb['Close'] >= df_bb['BB_26'])

df_bb.loc[long_signals, 'side'] = 1
df_bb.loc[short_signals, 'side'] = -1

#Revisar carga de la estrategia
print(df_bb.side.value_counts())

#Agregar Lag a nuestra señal
df_bb['side'] = df_bb['side'].shift(1)

#calcular retornos
df_bb['Returns'] = np.log(df_bb['Close']).diff()
df_bb['Position_sum'] = df_bb['side'].fillna(0).cumsum()
df_bb['Position_sum'].plot()

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
    return df

#Calcular a 26 dias
df_bb = b_bands(df,26)
df_bb.plot()

#Zoom
df_bb.iloc[-100:,:].plot()
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
pip list
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/klinesReq.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
cls

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(16,)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(32))


model.compile(
    loss=tf.keras.losses.MSE,
    optimizer=tf.optimizers.SGD(learning_rate=0.01))

x = tf.linspace(-2, 2, 256)
x = tf.cast(x, tf.float32)

def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[256], mean=0, stddev=1)

x = x[:, tf.newaxis]
y = y[:, tf.newaxis]
x = tf.tile(x, [1, 16])
y = tf.tile(y, [1, 16])

print(x.shape)
print(y.shape)
history = model.fit(x, y,
                    epochs=100,
                    batch_size=16,
                    verbose=0)

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(16,)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(32))


model.compile(
    loss=tf.keras.losses.MSE,
    optimizer=tf.optimizers.SGD(learning_rate=0.01))

x = tf.linspace(-2, 2, 256)
x = tf.cast(x, tf.float32)

def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[256], mean=0, stddev=1)

x = x[:, tf.newaxis]
y = y[:, tf.newaxis]
x = tf.tile(x, [1, 32])
y = tf.tile(y, [1, 32])

print(x.shape)
print(y.shape)
history = model.fit(x, y,
                    epochs=100,
                    batch_size=16,
                    verbose=0)

plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylim([0, max(plt.ylim())])
plt.ylabel('Loss [Mean Squared Error]')
plt.title('Keras training progress');

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(16,)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(32))


model.compile(
    loss=tf.keras.losses.MSE,
    optimizer=tf.optimizers.SGD(learning_rate=0.01))

x = tf.linspace(-2, 2, 256)
x = tf.cast(x, tf.float32)

def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[256], mean=0, stddev=1)

x = x[:, tf.newaxis]
y = y[:, tf.newaxis]
x = tf.tile(x, [1, 32])
y = tf.tile(y, [1, 32])

print(x.shape)
print(y.shape)
history = model.fit(x, y,
                    epochs=100,
                    batch_size=32,
                    verbose=0)

plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylim([0, max(plt.ylim())])
plt.ylabel('Loss [Mean Squared Error]')
plt.title('Keras training progress');

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(16,)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(32))


model.compile(
    loss=tf.keras.losses.MSE,
    optimizer=tf.optimizers.SGD(learning_rate=0.01))

x = tf.linspace(-2, 2, 256)
x = tf.cast(x, tf.float32)

def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[256], mean=0, stddev=1)

x = x[:, tf.newaxis]
y = y[:, tf.newaxis]
x = tf.tile(x, [1, 16])
y = tf.tile(y, [1, 16])

print(x.shape)
print(y.shape)
history = model.fit(x, y,
                    epochs=100,
                    batch_size=32,
                    verbose=0)

plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylim([0, max(plt.ylim())])
plt.ylabel('Loss [Mean Squared Error]')
plt.title('Keras training progress');

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(16,)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(32))


model.compile(
    loss=tf.keras.losses.MSE,
    optimizer=tf.optimizers.SGD(learning_rate=0.01))

x = tf.linspace(-2, 2, 256)
x = tf.cast(x, tf.float32)

def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[256], mean=0, stddev=1)

#x = x[:, tf.newaxis]
#y = y[:, tf.newaxis]
x = tf.tile(x, [1, 16])
y = tf.tile(y, [1, 16])

print(x.shape)
print(y.shape)
history = model.fit(x, y,
                    epochs=100,
                    batch_size=316,
                    verbose=0)

plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylim([0, max(plt.ylim())])
plt.ylabel('Loss [Mean Squared Error]')
plt.title('Keras training progress');
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
runcell(0, 'C:/Users/54911/.spyder-py3/model.py')
cls
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
runcell(0, 'C:/Users/54911/.spyder-py3/model.py')
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/model.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')

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
    return df

#Calcular a 56hs
df_bb = b_bands(df,14)
df_bb.plot()

#Zoom
df_bb.iloc[-100:,:].plot()

#Crear señales
df_bb['side'] = np.nan

long_signals = (df_bb['Close'] <= df_bb['Bb_26'])
short_signals = (df_bb['Close'] >= df_bb['BB_26'])

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

#Seleccionar un periodo de prueba
df_test =   df_bb.iloc[-500:,:].copy()
df_test['Cum_prod'] = (1 + df_test['Returns']).cumprod()
df_test['Cum_prod'].plot()
df_test['side'] = df_test['side'].fillna(0)

#Plot Basico
df_test[['Close', 'Bb_26', 'BB_26']].plot()

#Crear un nuevo plot con señales
df_test['Buy_Signal'] = df_test.apply(lambda x: x.Close if x.side == 1 else np.nan, axis=1)
df_test['Sell_Signal'] = df_test.apply(lambda x: x.Close if x.side == -1 else np.nan, axis=1)

fig = plt.figure(figsize = (16,8))
ax1 = plt.subplot()
plt.plot(df_test.index, df_test.Close)
plt.plot(df_test.index, df_test.Bb_26)
plt.plot(df_test.index, df_test.BB_26)
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
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/klinesReq.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
cls
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
debugfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/bollinger.py', wdir='C:/Users/54911/.spyder-py3')
!pip install pydot
pip install graphviz
runfile('C:/Users/54911/.spyder-py3/keras.py', wdir='C:/Users/54911/.spyder-py3')
!pip install keras
runfile('C:/Users/54911/.spyder-py3/keras.py', wdir='C:/Users/54911/.spyder-py3')
!pip install tensorflow.keras
runfile('C:/Users/54911/.spyder-py3/keras.py', wdir='C:/Users/54911/.spyder-py3')
!pip install tensorflow==1.14.0
!pip list
runfile('C:/Users/54911/.spyder-py3/keras.py', wdir='C:/Users/54911/.spyder-py3')
pip install tensorflow[keras]
runfile('C:/Users/54911/.spyder-py3/keras.py', wdir='C:/Users/54911/.spyder-py3')
pip list
pip uninstall tensorflow
pip uninstall keras
pip install tensorflow[keras]
pip uninstall tensorflow

## ---(Thu Dec 22 13:05:07 2022)---
runfile('C:/Users/54911/.spyder-py3/keras.py', wdir='C:/Users/54911/.spyder-py3')
pip list

## ---(Thu Dec 22 13:08:23 2022)---
pip list
runfile('C:/Users/54911/.spyder-py3/keras.py', wdir='C:/Users/54911/.spyder-py3')

## ---(Thu Dec 22 14:40:39 2022)---
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
conda install tensorflow
runfile('C:/Users/54911/.spyder-py3/untitled0.py', wdir='C:/Users/54911/.spyder-py3')
runfile('C:/Users/54911/.spyder-py3/kkeras.py', wdir='C:/Users/54911/.spyder-py3')

## ---(Thu Dec 22 14:55:55 2022)---
runfile('C:/Users/54911/.spyder-py3/kkeras.py', wdir='C:/Users/54911/.spyder-py3')

## ---(Thu Dec 22 14:58:34 2022)---
runfile('C:/Users/54911/.spyder-py3/kkeras.py', wdir='C:/Users/54911/.spyder-py3')
pip list | findstr keras
runfile('C:/Users/54911/.spyder-py3/kkeras.py', wdir='C:/Users/54911/.spyder-py3')

## ---(Thu Dec 22 15:38:26 2022)---
runfile('C:/Users/54911/.spyder-py3/kkeras.py', wdir='C:/Users/54911/.spyder-py3')
pip list
!pip list