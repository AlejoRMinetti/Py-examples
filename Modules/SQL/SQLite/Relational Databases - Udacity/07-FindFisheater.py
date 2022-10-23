#
# Find the names of the individual animals that eat fish.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.
#

QUERY = '''
SELECT name  FROM animals a, diet d
WHERE a.species = d.species and d.food = "fish";
'''

# other ways to find the fish eater
"""
QUERY = '''
SELECT a.name, FROM animals a
INNER JOIN diet d ON (a.species=d.species)
WHERE d.food = "fish";

QUERY = '''
SELECT name FROM animals, diet
WHERE animals.species = diet.species and diet.food = "fish";
'''
'''


"""

