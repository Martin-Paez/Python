import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import graphviz
import pydot
    
x = tf.linspace(-2, 2, 784)
x = tf.cast(x, tf.float32)

def f(x): 
    return x**2 + 2*x - 5

y = f(x) + tf.random.normal(shape=[784], mean=0, stddev=1)

# Fijo la cantidad de entradas (es aconsejable)
# El tamaño del lote siempre se omite, ya que solo se especifica la forma de cada muestra.
inputs = keras.Input(shape=(784,))
print(inputs.shape)
print(inputs.dtype)

# Creo neuronas
dense = layers.Dense(64, activation="relu")
# Conecto capas
x = dense(inputs)

# Agrego y conecto 2 capas más
x = layers.Dense(64, activation="relu")(x)
outputs = layers.Dense(10)(x)

# Creo el modelo
model = keras.Model(inputs=inputs, outputs=outputs, name="mnist_model")
model.summary()

keras.utils.plot_model(model, "my_first_model.png")
keras.utils.plot_model(model, "my_first_model_with_shape_info.png", show_shapes=True)

"""
from tensorflow import keras
import pydot as pyd
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

model_to_dot.pydot = pyd

#Visualize Model

def visualize_model(model):
  return SVG(model_to_dot(model).create(prog='dot', format='svg'))
#create your model
#then call the function on your model
visualize_model(model)
"""