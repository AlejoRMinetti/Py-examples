"""
Intro to Relational DataBases - Udacity
https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287060923
"""

#
# Uncomment one of these QUERY variables at a time and use "Test Run" to run it.
# You'll see the results below.  Then try your own queries as well!
#

# name that starts nearest to Z
QUERY1 = "select max(name) from animals;"

# 10 animals
QUERY2 = "select * from animals limit 10;"

# Orangutans starting with the oldest
QUERY3 = "select * from animals where species = 'orangutan' order by birthdate;"

# Orangutan starting with the youngest
QUERY4 = "select name from animals where species = 'orangutan' order by birthdate desc;"

# names in alphabetic order from 20 to 30
QUERY5 = "select name, birthdate from animals order by name limit 10 offset 20;"

# list of the oldest of each specie
QUERY6 = "select species, min(birthdate) from animals group by species;"


# count of names ordered by the most commun
QUERY7 = '''
    select name, count(*) as num from animals
    group by name
    order by num desc
    limit 5;'''


#  SQL commands that were used to create those tables
"""
create table animals (  
       name text,
       species text,
       birthdate date);

create table diet (
       species text,
       food text);  

create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 

create table ordernames (
       t_order text,
       name text);
"""