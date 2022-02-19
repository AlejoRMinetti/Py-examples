# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for entry in index:
        if keyword == entry[0]:
            return entry[1]
    return []


print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']

"""Para saber ancho de banda, googlear: speedtest
Para saber ping a una direccion web, con windows en cmd: tracert www.udacity.com"""