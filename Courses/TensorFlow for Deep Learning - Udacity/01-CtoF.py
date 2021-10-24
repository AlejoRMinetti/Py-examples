"""
Celsius to Fahrenheit
TensorFlow free course - Udacity
The Basics: Training Your First Model
"""
import tensorflow as tf
import numpy as np
# for logging 
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# data
celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)
# print data
for i,c in enumerate(celsius_q):
  print("{} degrees Celsius = {} degrees Fahrenheit".format(c, fahrenheit_a[i]))

# build a layer
l0 = tf.keras.layers.Dense(units=1, input_shape=[1])

# Assemble layers into the model
model = tf.keras.Sequential([l0])

# Compile the model, with loss and optimizer functions
# The loss function (mean squared error) and the optimizer (Adam) used here are
# standard for simple models like this one, learning rate = 0.1 in Adam(0.1)
# the range is usually within 0.001 (default), and 0.1
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

# Train the model
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")

# Display training statistics
# We trained it with 3500 examples (7 pairs, over 500 epochs)
import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])

# Use the model to predict values
print(model.predict([100.0]))

# multiple test:
testVals = [2.1, 10., 20.1, 50.5, 100.2, 200.1, 500.]
for val in testVals:
  print("----------------")
  print("Test val:"+str(val))
  print(model.predict([val]))
  print("By formula: "+str(val*1.8+32))

# Looking at the layer weights
print("These are the layer variables: {}".format(l0.get_weights()))

# A little experiment
print("A little experiment: 3 layers")
l0 = tf.keras.layers.Dense(units=4, input_shape=[1])
l1 = tf.keras.layers.Dense(units=4)
l2 = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([l0, l1, l2])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")
print(model.predict([100.0]))
print("Model predicts that 100 degrees Celsius is: {} degrees Fahrenheit".format(model.predict([100.0])))
print("These are the l0 variables: {}".format(l0.get_weights()))
print("These are the l1 variables: {}".format(l1.get_weights()))
print("These are the l2 variables: {}".format(l2.get_weights()))
