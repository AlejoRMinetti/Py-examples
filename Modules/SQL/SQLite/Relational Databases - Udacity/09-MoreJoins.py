#
# List all the taxonomic orders, using their common names, sorted by the number of
# animals of that order that the zoo has.
#
# The animals table has (name, species, birthdate) for each individual.
# The taxonomy table has (name, species, genus, family, t_order) for each species.
# The ordernames table has (t_order, name) for each order.
#
# Be careful:  Each of these tables has a column "name", but they don't have the
# same meaning!  animals.name is an animal's individual name.  taxonomy.name is
# a species' common name (like 'brown bear').  And ordernames.name is the common
# name of an order (like 'Carnivores').

QUERY = '''
select o.name, COUNT(a.name) as NUM
from animals a, taxonomy t, ordernames o
where t.t_order = o.t_order and a.species = t.name
group by o.name
order by NUM desc
'''

# same query with explicit joins
QUERY = '''
select o.name, COUNT(a.name) as NUM
from animals a
join taxonomy t on a.species = t.name
join ordernames o on t.t_order = o.t_order
group by o.name
order by NUM desc
'''