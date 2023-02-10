import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
# BD Cripto
from klinesReq import KlinesDB
# Plot velas
import matplotlib.pyplot as plt
from mpl_finance import candlestick2_ohlc
import matplotlib.dates as mdates


# Carga de datos
#delivery_data = pd.read_csv("BTCUSDT4h.csv")
df = KlinesDB.instantiate('BTCUSDT', '4h').read()
delivery_data = df[['Open_Time', 'Open', 'High', 'Low', 'Close', 'Volume']]
# Para evitar el warning, asegura que df no sea una vista.
delivery_data = delivery_data.copy()

def plot(df):
    
    df.set_index('Open_Time', inplace=True)

    fig, ax = plt.subplots()
    candlestick2_ohlc(ax, df['Open'], df['High'], df['Low'], df['Close'], width=0.6, colorup='g', colordown='r')
   
    #candlestick_ohlc(ax, df[-1:-1].values, width=0.6, colorup="green", colordown="red", alpha=0.8)
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.xticks(rotation=45)
    plt.xlabel("Fecha")
    plt.ylabel("Precio (USD)")
    plt.title("Gráfico de velas de Bitcoin en Binance")
    plt.show()

plot(delivery_data)

"""

# Preprocesamiento de datos
mean = delivery_data.mean()
std = delivery_data.std()
delivery_data = (delivery_data - mean) / std

# Dividir los datos en entrenamiento y test
df_train = delivery_data[:int(0.8 * len(delivery_data))]
df_test = delivery_data[int(0.8 * len(delivery_data)):]

# Preparar los datos para la red neuronal
timesteps = 100 # Número de velas a considerar como entrada
num_features = 6 
pred_window = 15
x_train = []
y_train = []
for i in range(timesteps, len(df_train) - pred_window):
    x_train.append(df_train.iloc[i-timesteps:i,:].values)
    y_train.append(df_train.iloc[i + pred_window, -1])
x_train, y_train = np.array(x_train), np.array(y_train)
    
# Crear el modelo
model = Sequential()
model.add(LSTM(50, input_shape=(timesteps, num_features)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Preparar los datos de test para la red neuronal
x_test = []
y_test = []
for i in range(timesteps, len(df_test)):
    x_test.append(df_test[i-timesteps:i].values)
    y_test.append(df_test.iloc[i, -1])
x_test, y_test = np.array(x_test), np.array(y_test)

# Entrenar el modelo
model.fit(x_train, y_train, epochs=100, batch_size=32,
          validation_data=(x_test, y_test))

# Evaluar el modelo
test_loss = model.evaluate(x_test, y_test)
print('Test loss:', test_loss)
"""