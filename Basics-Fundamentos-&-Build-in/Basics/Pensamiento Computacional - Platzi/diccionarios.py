dicc = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50
}

print(dicc)

print(dicc['David'])

# print(dicc['Erik'])
# Imprime este error en consola:
# Traceback (most recent call last):
#   File "diccionarios.py", line 11, in <module>
#     print(dicc['Erik'])
# KeyError: 'Erik'

dicc.get('Juan', 30)

dicc.get('David',30)

dicc['Jaime'] = 20

print(dicc)

dicc['Pedro'] = 70

print(dicc)

del dicc['Jaime']

print(dicc)

print('\nIterando en las llaves del diccionario:\n')
for llave in dicc.keys():
    print(llave)

print('\nIterando en los valores del diccionario:\n')     
for valor in dicc.values():
    print(valor)

print('\nIterando en los elementos del diccionario:\n')
for llave,valor in dicc.items():
    print(llave,valor)
     
     
print('David in diccionario: ','David' in dicc)
print('Tom in diccionario: ','Tom' in dicc)


## Delete all elements in the dictionary
# a.clear()
# print(a)

# # Delete the dictionary
# del a 
# print(a)