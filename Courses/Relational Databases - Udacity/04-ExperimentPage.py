"""
Intro to Relational DataBases - Udacity
https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287060923
"""

#
# Uncomment one of these QUERY variables at a time and use "Test Run" to run it.
# You'll see the results below.  Then try your own queries as well!
#

# name that starts nearest to Z
# QUERY = "select max(name) from animals;"

# 10 animals
# QUERY = "select * from animals limit 10;"

# Orangutans starting with the oldest
# QUERY = "select * from animals where species = 'orangutan' order by birthdate;"

# Orangutan starting with the youngest
# QUERY = "select name from animals where species = 'orangutan' order by birthdate desc;"

# names in alphabetic order from 20 to 30
# QUERY = "select name, birthdate from animals order by name limit 10 offset 20;"

# list of the oldest of each specie
# QUERY = "select species, min(birthdate) from animals group by species;"

"""
# count of names ordered by the most commun
QUERY = '''
    select name, count(*) as num from animals
    group by name
    order by num desc
    limit 5;'''
"""