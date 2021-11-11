#
# Find the one food that is eaten by only one animal.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.
#

QUERY = '''
select food, COUNT(*) as num
from animals a, diet d
where a.species = d.species
group by d.food
having num = 1
'''

# who eats them?
"""
QUERY = '''
select food, a.species, COUNT(*) as num
from animals a, diet d
where a.species = d.species
group by d.food
having num = 1
'''
"""