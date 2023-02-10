import numpy as np
import pandas as pd
import tensorflow as tf
from keras.utils import to_categorical
from keras.models import load_model
import json
from sklearn.preprocessing import LabelEncoder

# Ejemplo de aplicacion de NN (neural networks) :

# Dada una lista de destinos, el algoritmo asigna paquetes a choferes

# Interpretacoin :
    
# Discretizar el problema, y despues, focalizar donde usar NN. En este caso,
# se usa NN para elegir cual es el "mejor siguiente destino". 

# Luego, la red ya entrenada se embebe detro de un programa. Como la salida de
# la red es uno de los nodos de entrada: por un lado, se elimina de la lista de
# entrada; y, por el otro, se guarda la salida en la lista individual del 
# del chofer seleccionado por NN.

# Carga de datos
# Normalizacion
# Ratio n_tarin / n_test
# Crear el modelo de red neuronal
    # En este caso:
        # Potencias de dos
        # De mayor a menor, simil especializacion
        # Relu por ser eficiente
        # input_shape=(2,) porque la entrada en x eh y
        
# Cargar los datos de entrega
delivery_data = pd.read_csv("recorridos.csv")    

# Mezclar los datos
delivery_data = delivery_data.sample(frac=1).reset_index(drop=True)

# Mapear strings a int
le = LabelEncoder()
delivery_data['zone'] = le.fit_transform(delivery_data['zone'])
delivery_data['day'] = le.fit_transform(delivery_data['day'])

# Seleccionar los parametros de entrada de la NN
params = delivery_data[['x', 'y', 'date']]

# Normalizar las ubicaciones de los puntos de entrega
mean = params.mean()
std = params.std()
params = (params - mean) / std

# One-hot
delivery_data['driver'] = delivery_data['driver'].astype('category')
driver_codes = delivery_data['driver'].cat.codes
num_categories = len(delivery_data['driver'].cat.categories)
drivers = to_categorical(driver_codes, num_categories)

# Dividir los datos en conjuntos de entrenamiento y prueba
x_train = params[:int(0.8 * len(params))]      # 80%
y_train = drivers[:int(0.8 * len(drivers))]
x_test = params[int(0.8 * len(params)):]       # 20%
y_test = drivers[int(0.8 * len(drivers)):]

# Crear el modelo de red neuronal
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, activation='relu', input_shape=(3,)))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(8, activation='softmax'))

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(x_train, y_train, epochs=100, batch_size=32,
                    validation_data=(x_test, y_test))

# Evaluar el modelo
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print('Test loss:', test_loss)
print('Test accuracy:', test_accuracy)

fileName = 'x_y_nDriver_date_day_balanced'
modelFile = fileName +  '.h5'
model.save(modelFile)
model = load_model(modelFile)

_delivery_data = pd.read_csv("test.csv")    
_delivery_data = _delivery_data.sample(frac=1).reset_index(drop=True)
_delivery_data['zone'] = le.fit_transform(_delivery_data['zone'])
_delivery_data['day'] = le.fit_transform(_delivery_data['day'])
x_test = _delivery_data[['x', 'y', 'date']]
x_test = (x_test - mean) / std

# Hacer predicciones con el modelo
predictions = model.predict(x_test)

# Guardar en un json los resultados
drivers = delivery_data['driver'].cat.categories[np.argmax(predictions, axis=1)]
_loc = _delivery_data[['x', 'y']]
_x = _loc[int(0 * len(_loc)):]  
df = pd.DataFrame({'x': _x['x'],
                   'y': _x['y'],
                   'prediction': drivers})
df_json = df.to_json(orient='records')
df_dict = json.loads(df_json)
unique_drivers = np.unique(drivers)
df_dict = {'records': df_dict, 'unique_drivers': unique_drivers.tolist()}
df_json = json.dumps(df_dict)
with open(fileName + '.json', 'w') as f:
    f.write(df_json)


data = pd.read_csv("recorridos.csv")   
df = pd.DataFrame({'x': data['x'],
                   'y': data['y'],
                   'prediction': data['driver']})
df_json = df.to_json(orient='records')
df_dict = json.loads(df_json)
unique_drivers = np.unique(data['driver'])
df_dict = {'records': df_dict, 'unique_drivers': unique_drivers.tolist()}
df_json = json.dumps(df_dict)
with open('recorridos.json', 'w') as f:
    f.write(df_json)
