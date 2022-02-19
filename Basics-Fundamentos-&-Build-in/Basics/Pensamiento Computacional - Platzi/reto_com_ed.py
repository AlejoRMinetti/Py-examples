
nombres = []
edades = []
nombres.append('')
edades.append(0)

for i in range(1,3):
    nombres.append(input(f'Introduce el nombre del usuario {i}: '))
    edades.append(input(f'Introduce la edad del usuario {i}: '))

if edades[1] > edades[2]:
    print(f'{nombres[1]} es mayor a {nombres[2]}')
elif edades[1] < edades[2]:
    print(f'{nombres[1]} es menor a {nombres[2]}')
else:
    print(f'{nombres[1]} y {nombres[2]} tienen la misma edad')
    


