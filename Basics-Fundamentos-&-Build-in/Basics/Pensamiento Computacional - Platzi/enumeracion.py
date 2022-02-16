
entrada = int(input('Introduce el numero: '))
resultado = 0
while resultado**2 < entrada:
    print(resultado)
    resultado +=1

if resultado**2 == entrada:
    print(f'La raiz cuadrada de {entrada} es {resultado}')
else:    
    print(f'{entrada} no tiene raiz exacta')
    
    
