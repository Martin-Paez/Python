import os
import tensorflow as tf

def Transpose(tf,x):
    print(x)
    print(tf.transpose(x)) 
    print(x @ tf.transpose(x))
#    1 * 1 + 2 * 2 + 3 * 3 = 1 + 4 + 9 = 14
#    1 * 4 + 2 * 5 + 3 * 6 = 4 + 10 + 18 = 32

def Concat(tf,x):
    print(f'\nx:\n{x}')
    # No modifica la dimension
    print(f'\ntf.concat([x, x, x], axis=0):\n {tf.concat([x, x, x], axis=0)}')
    print(f'\ntf.concat([x, x, x], axis=1):\n {tf.concat([x, x, x], axis=1)}')

def Softmax(tf,x):
    print(f'\nx:\n{x}')
    s1 = tf.nn.softmax(x, axis=1)
    print(f'\ntf.nn.softmax(x, axis=1): \n {s1}')
    s2 = tf.nn.softmax(x, axis=0)
    print(f'\ntf.nn.softmax(x, axis=0):\n {s2}')
    rx = tf.reduce_sum(s1[0])
    print(f'\ntf.reduce_sum(x[0]): {rx}')
    rty = tf.reduce_sum(tf.transpose(s2)[0])
    print(f'\ntf.reduce_sum(tf.transpose(s2)[0]): {rty}')

def Reduce(tf,x):
    print(tf.reduce_sum(x))
    print(tf.reduce_sum(x[0]))

#os.system('cls')

x = tf.constant([[1., 2., 3.],
                 [4., 6., 5.]])

a = 2

if a == 0:
    Transpose(tf,x)
elif a == 1:
    Concat(tf,x)
elif a == 2:
    Softmax(tf,x)
elif a == 3:
    Reduce(tf,x)

