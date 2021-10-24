# https://devcode.la/tutoriales/listas-python/
lista = [1, 2.5, 'DevCode', [5,6] ,4]

if 4 in lista:
    print('si esta el 4!')

# Acceso
print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # DevCode
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print(lista[1:3]) # [2.5, 'DevCode']
print(lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
print(lista[1:6:2]) # [2.5, [5, 6]]

print("mediante un for")
for element in lista:
    print(element)

# Geters

lista.index('DevCode') # 2

# Editarlas

lista.append(10) # [2, 5, 'DevCode', 1.2, 5, 10]
lista.append([2,5]) # [2, 5, 'DevCode', 1.2, 5, [2, 5]]

lista.extend([2,5]) # [2, 5, 'DevCode', 1.2, 5, 2, 5]

lista.remove(2) # [5, 'DevCode', 1.2, 5]

lista.reverse() # [5, 1.2, 'DevCode', 5, 2]