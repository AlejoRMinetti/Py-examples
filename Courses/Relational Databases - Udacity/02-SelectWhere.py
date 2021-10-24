"""
Intro to Relational DataBases - Udacity
https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287000923
"""

# The query below finds the names and birthdates of all the gorillas.
# 
# Modify it to make it find the names of all the animals that are not
# gorillas and not named 'Max'.
#

QUERY = '''
select name from animals where not species = 'gorilla' and not name = "Max";
'''