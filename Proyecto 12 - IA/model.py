import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = [9, 6]
import tensorflow as tf

x = tf.linspace(-2, 2, 256)
x = tf.cast(x, tf.float32)

def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[256], mean=0, stddev=1)

#plt.plot(x.numpy(), y.numpy(), '.', label='Data')
#plt.plot(x, f(x),  label='Ground truth')
#plt.legend()
#plt.show()

class Model(tf.keras.Model):
  def __init__(self, units):
    super().__init__()
    self.dense1 = tf.keras.layers.Dense(units=units,
                                        activation=tf.nn.relu,
                                        kernel_initializer=tf.random.normal,
                                        bias_initializer=tf.random.normal)
    self.dense2 = tf.keras.layers.Dense(1)

  def call(self, x, training=True):
    #print(x)
    # For Keras layers/models, implement `call` instead of `_call_`.
    x = x[:, tf.newaxis]
    #print(x)
    x = self.dense1(x)
    x = self.dense2(x)
    return tf.squeeze(x, axis=1)

model = Model(64)
#plt.plot(x.numpy(), y.numpy(), '.', label='data')
#plt.plot(x, f(x),  label='Ground truth')
#plt.plot(x, model(x), label='Untrained predictions')
#plt.title('Before training')
#plt.legend();
#plt.show()


model(x)

variables = model.variables

optimizer = tf.optimizers.SGD(learning_rate=0.01)

for step in range(1000):
  with tf.GradientTape() as tape:
    prediction = model(x)
    error = (y-prediction)**2
    mean_error = tf.reduce_mean(error)
  gradient = tape.gradient(mean_error, variables)
  optimizer.apply_gradients(zip(gradient, variables))

  #if step % 100 == 0:
    #print(f'Mean squared error: {mean_error.numpy():0.3f}')


plt.plot(x.numpy(),y.numpy(), '.', label="data")
plt.plot(x, f(x),  label='Ground truth')
plt.plot(x, model(x), label='Trained predictions')
plt.title('After training')
plt.legend()
plt.show()




model = tf.keras.models.Sequential()
#model.add(tf.keras.Input(shape=(256,)))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(1))


model.compile(
    loss=tf.keras.losses.MSE,
    optimizer=tf.optimizers.SGD(learning_rate=0.01))

"""
x0 = x #para tile en vez de reshape
y0 = y #para tile en vez de reshape
x = x[:, tf.newaxis]
y = y[:, tf.newaxis]
x = tf.tile(x, [1, 16])
y = tf.tile(y, [1, 16])

x = tf.reshape(x,[16,16])
y = tf.reshape(y,[16,16])
"""

x1 = x[:, tf.newaxis]
y1 = y[:, tf.newaxis]
#x1 = tf.expand_dims(x, axis=0)
#y1 = tf.expand_dims(y, axis=0)
"""
x1 = x[:, tf.newaxis]
x1 = tf.tile(x1, [1, 16])
y1 = y[:, tf.newaxis]
y1 = tf.tile(y1, [1, 16])"""

print(f'x1: {x1.shape}')
print(f'y1: {y1.shape}')

history = model.fit(x1, y1,
                    epochs=1000,
                    batch_size=64,
                    verbose=0)

plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylim([0, max(plt.ylim())])
plt.ylabel('Loss [Mean Squared Error]')
plt.title('Keras training progress');
plt.show()


m = model(x1)
#m = m[:,0] #Para layerOut = 16
print(f'm: {m.shape}')

xp = x[:,tf.newaxis]
#xp = x
print(f'xp: {xp.shape}')

#x1 = tf.reshape(x,[256,1])
#x1 = x0 #para tile en vez de reshape
#print(f'x1: {x1.shape}')
#y1 = tf.reshape(y,[256,1])
#y1 = y0 #para tile en vez de reshape
#print(f'y1: {y1.shape}')

plt.plot(x.numpy(),y.numpy(), '.', label="data")
plt.plot(x, f(x),  label='Ground truth')
plt.plot(xp, m, label='Trained predictions')
plt.title('After training')
plt.legend()
plt.show()



model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(16,)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(1))


model.compile(
    loss=tf.keras.losses.MSE,
    optimizer=tf.optimizers.SGD(learning_rate=0.01))

"""
x0 = x #para tile en vez de reshape
y0 = y #para tile en vez de reshape
x = x[:, tf.newaxis]
y = y[:, tf.newaxis]
x = tf.tile(x, [1, 16])
y = tf.tile(y, [1, 16])
"""
x = tf.reshape(x,[16,16])
y = tf.reshape(y,[16,16])

print(f'x: {x.shape}')
print(f'y: {y.shape}')
history = model.fit(x, y,
                    epochs=1000,
                    batch_size=16,
                    verbose=0)

plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylim([0, max(plt.ylim())])
plt.ylabel('Loss [Mean Squared Error]')
plt.title('Keras training progress');
plt.show()


m = model(x)
#m = m[:,0] #Para layerOut = 16
print(f'm: {m.shape}')
xp = tf.transpose(x)[0]
xp = xp[:,tf.newaxis]
print(f'xp: {xp.shape}')

x1 = tf.reshape(x,[256,1])
#x1 = x0 #para tile en vez de reshape
print(f'x1: {x1.shape}')
y1 = tf.reshape(y,[256,1])
#y1 = y0 #para tile en vez de reshape
print(f'y1: {y1.shape}')

plt.plot(x1.numpy(),y1.numpy(), '.', label="data")
plt.plot(x1, f(x1),  label='Ground truth')
plt.plot(xp, m, label='Trained predictions')
plt.title('After training')
plt.legend()
plt.show()

#fitAndPlot(model, x, y)

