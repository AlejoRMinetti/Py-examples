"""
Naive Forcasting
Intro to TensorFlow for Deep Learning
https://classroom.udacity.com/courses/ud187

Colab:
https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l08c03_moving_average.ipynb#scrollTo=BLt-pLiZ0nfB
"""
print(__doc__)

############## setup
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from forecastUtil import * 

keras = tf.keras

############# Trend and Seasonality

time = np.arange(4 * 365 + 1)

slope = 0.05
baseline = 10
amplitude = 40
series = baseline + trend(time, slope) + seasonality(time, period=365, amplitude=amplitude)

noise_level = 5
noise = white_noise(time, noise_level, seed=42)

series += noise

print("Data:")
plt.figure(figsize=(10, 6))
plot_series(time, series)
plt.show()

# Naive Forecast
split_time = 1000
time_train = time[:split_time]
x_train = series[:split_time]
time_valid = time[split_time:]
x_valid = series[split_time:]

naive_forecast = series[split_time - 1:-1]
print("Naive forecast:")
plt.figure(figsize=(10, 6))
plot_series(time_valid, x_valid, start=0, end=150, label="Series")
plot_series(time_valid, naive_forecast, start=1, end=151, label="Forecast")
plt.show()

mae = keras.metrics.mean_absolute_error(x_valid, naive_forecast).numpy()
print("Mean squared error for naive forecast:",mae)

"""
def moving_average_forecast(series, window_size):
  '''Forecasts the mean of the last few values.
     If window_size=1, then this is equivalent to naive forecast'''
  forecast = []
  for time in range(len(series) - window_size):
    forecast.append(series[time:time + window_size].mean())
  return np.array(forecast)
"""
#################### Moving Average
def moving_average_forecast(series, window_size):
  """Forecasts the mean of the last few values.
     If window_size=1, then this is equivalent to naive forecast
     This implementation is *much* faster than the previous one"""
  mov = np.cumsum(series)
  mov[window_size:] = mov[window_size:] - mov[:-window_size]
  return mov[window_size - 1:-1] / window_size

print("Moving Average:")
moving_avg = moving_average_forecast(series, 30)[split_time - 30:]
plt.figure(figsize=(10, 6))
plot_series(time_valid, x_valid, label="Series")
plot_series(time_valid, moving_avg, label="Moving average (30 days)")
plt.show()

mae = keras.metrics.mean_absolute_error(x_valid, moving_avg).numpy()
print("MAE for Moving Average:",mae)

print("Seasonality: Subtracting the value at time t – 365 from the value at time t:")
diff_series = (series[365:] - series[:-365])
diff_time = time[365:]

plt.figure(figsize=(10, 6))
plot_series(diff_time, diff_series, label="Series(t) – Series(t–365)")
plt.show()

print("Focusing on the validation period:")
plt.figure(figsize=(10, 6))
plot_series(time_valid, diff_series[split_time - 365:], label="Series(t) – Series(t–365)")
plt.show()

print("Moving Average for seasonality Diff:")
diff_moving_avg = moving_average_forecast(diff_series, 50)[split_time - 365 - 50:]
plt.figure(figsize=(10, 6))
plot_series(time_valid, diff_series[split_time - 365:], label="Series(t) – Series(t–365)")
plot_series(time_valid, diff_moving_avg, label="Moving Average of Diff")
plt.show()

print("Now let's bring back the trend and seasonality by adding the past values from t – 365:")
diff_moving_avg_plus_past = series[split_time - 365:-365] + diff_moving_avg
plt.figure(figsize=(10, 6))
plot_series(time_valid, x_valid, label="Series")
plot_series(time_valid, diff_moving_avg_plus_past, label="Forecasts")
plt.show()

mae = keras.metrics.mean_absolute_error(x_valid, diff_moving_avg_plus_past).numpy()
print("MAE for Moving Average on diff seasonality:",mae)

print("diff_moving_avg_plus_smooth_past:")
diff_moving_avg_plus_smooth_past = moving_average_forecast(series[split_time - 370:-359], 11) + diff_moving_avg

plt.figure(figsize=(10, 6))
plot_series(time_valid, x_valid, label="Series")
plot_series(time_valid, diff_moving_avg_plus_smooth_past, label="Forecasts")
plt.show()

mae = keras.metrics.mean_absolute_error(x_valid, diff_moving_avg_plus_smooth_past).numpy()
print("MAE for diff_moving_avg_plus_smooth_past:",mae)