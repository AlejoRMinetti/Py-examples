import time
start_time = time.time()

def f(x,n):
    return x**2-n

entrada = int(input('Introduce el numero: '))
resultado = 0
lim_inf = 0
lim_sup = entrada
tolerancia = 0.000000000001
start_time = time.time()

while abs(f(resultado,entrada)) > tolerancia:
    resultado = (lim_inf + lim_sup) / 2
    print(abs(f(resultado,entrada)),resultado)
    if f(resultado,entrada) < 0:
        lim_inf = resultado
    else:
        lim_sup = resultado
    
print(f'La raiz cuadrada de {entrada} es : ',resultado)
# print(start_time)
# print(time.time())
print('--- %s seconds ---' % (time.time() - start_time))

     

