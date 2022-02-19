import matplotlib.pyplot as plt   # librería para graficar
import numpy as np                # librería para manejo de vectores y utilidades matemáticas
from math import pi

N = 100 # número de puntos

def f(x):
  return np.sin(x)

x = np.linspace(-2*pi, 2*pi, N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()