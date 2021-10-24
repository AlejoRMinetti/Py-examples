"""
 Examples of random generations
 https://realpython.com/python-random/
"""
import random
import numpy as np

random.seed(444)
random.random()

# ints
random.randint(0, 10)
random.randrange(1, 10)

# float with probability

random.uniform(20, 30)
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)


# items
items = ['one', 'two', 'three', 'four', 'five']
random.choice(items)
random.choices(items, k=2) # k selected

###########  usando Numpy
np.random.seed(444)
np.set_printoptions(precision=2)  # Output decimal fmt.
np.random.randn(5) # array

# `p` is the probability of choosing each element
np.random.choice([0, 1], p=[0.6, 0.4], size=(5, 4))

# NumPy's `randint` is [inclusive, exclusive), unlike `random.randint()
np.random.randint(0, 2, size=25, dtype=np.uint8).view(bool)