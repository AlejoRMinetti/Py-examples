num_1 = int(input('Escribe un numero: '))
num_2 = int(input('Escribe otro numero: '))

if num_1 > num_2:
    print(f'{num_1} es mayor que {num_2}')
elif num_1 < num_2:
    print(f'{num_1} es menor que {num_2}')
else:
    print('Ambos son iguales')