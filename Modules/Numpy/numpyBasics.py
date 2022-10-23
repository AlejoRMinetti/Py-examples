"""
Numpy basic use
 """
import numpy as np  # Make numpy available using np.

############## info from np.array #############

# Create a numpy array, and append an element
a = np.array(["Hello", "World"])
a = np.append(a, "!")
print("Current array: {}".format(a))
print("Printing each element")
for i in a:
  print(i)

print("\nPrinting each element and their index")
for i,e in enumerate(a):
  print("Index: {}, was: {}".format(i, e))

# Basic math
print("\nShowing some basic math on arrays")
b = np.array([0,1,4,3,2])
print("Max: {}".format(np.max(b)))
print("Average: {}".format(np.average(b)))
print("Max index: {}".format(np.argmax(b)))

print("\nYou can print the type of anything")
print("Type of b: {}, type of b[0]: {}".format(type(b), type(b[0])))

# Numpy creations
print("\nUse numpy to create a [3,2] dimension array with random number")
c = np.random.rand(3, 2)
print(c)

# numpy dimensions
print("\nYou can print the dimensions of arrays")
print("Shape of a: {}".format(a.shape))
print("Shape of b: {}".format(b.shape))
print("Shape of c: {}".format(c.shape))
print("...Observe, Python uses both [0,1,2] and (0,1,2) to specify lists")
print("Rows of c: {}".format(c.shape[0]))
print("Columns of c: {}".format(c.shape[1]))

# round up to int
print("Round up to int of c:",np.around(list(c[:,0])))
print("Con 2 decimales of c:",np.around(list(c[:,0]*100)))

################ np creations #######################

print( np.zeros( (3,4) ) )
print( np.ones( (2,3,4), dtype=np.int16 ) )
print( np.empty( (2,3) ) ) # uninitialized, output may vary
print( np.arange( 10, 30, 5 ) ) # inicial, final, step
print( np.arange( 0, 2, 0.3 ) )
print( np.linspace( 0, 2, 9 ) ) # 9 numbers from 0 to 2
from numpy import pi
print( x = np.linspace( 0, 2*pi, 100 ) # useful to 
# evaluate function at lots of points

#################### Operations #######################

print(np.arange(100).reshape(10,10))

# ver Manual numpy-user 