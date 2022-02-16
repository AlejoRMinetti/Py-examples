"""
Strings
"""

# String .format()
print('Monto total: ${:0,.2f}'.format(32581564456.365))

# get substring
a_string = "Hola Roberto mucho gusto"
print(a_string[5:12])
print(a_string[a_string.find("Hola ")+len("Hola "):a_string.find("mucho")])
print(a_string.split())

# ver mas https://www.geeksforgeeks.org/python-strings/

print(a_string.replace('H',''))

# split sitring num to int
NumerosStr = "123 54 23"
print(list(map(int,NumerosStr.split())))