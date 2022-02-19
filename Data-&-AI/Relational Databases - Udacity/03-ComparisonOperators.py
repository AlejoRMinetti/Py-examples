"""
Intro to Relational DataBases - Udacity
https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287030923#
"""

# Find all the llamas born between January 1, 1995 and December 31, 1998.
# Fill in the 'where' clause in this query.

QUERY = '''
select name from animals where species = "llama" and birthdate >= '1995-01-01' and birthdate <= '1998-12-31'
'''