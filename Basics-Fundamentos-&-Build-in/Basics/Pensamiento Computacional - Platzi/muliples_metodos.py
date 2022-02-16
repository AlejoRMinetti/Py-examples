def main():

    import time
    def enumer_exaust(entrada):
        resultado = 0
        while resultado**2 < entrada:
            print(resultado)
            resultado +=1

        if resultado**2 == entrada:
            return resultado
        else:
            return -1
        
    def enumer_exaus_aprox(entrada):
        epsilon = 0.0001
        paso = epsilon**2
        resultado = 0.0

        while abs(resultado **2- entrada) >= epsilon and resultado <=entrada:
            print(abs(resultado **2- entrada),resultado)
            resultado += paso

        if abs(resultado**2 - entrada) >= epsilon:
            return -1
        else:
            return resultado

    def biseccion(entrada):
        def f(x,n):
            return x**2-n
        
        tolerancia = 0.0001
        lim_inf = 0
        lim_sup = entrada
        resultado = 0
        iter_max = 100 
        iter = 0
        while abs(f(resultado,entrada)) > tolerancia:
            resultado = (lim_inf + lim_sup) / 2
            print('iteracion:',iter)
            print(f(resultado,entrada),resultado)
            if f(resultado,entrada) < 0:
                lim_inf = resultado
            else:
                lim_sup = resultado
            iter += 1
            if iter == iter_max:
                break

        return resultado    

    print('Programa que saca la raiz cuadrada de un numero')
    metodo = """\nElija el metodo para sacar la raiz:
    1.Enumeracion Exhaustiva
    2.Enumeracion Exhaustiva con aproximacion
    3.Biseccion

    Opcion:"""
    opcion = input(metodo)

    if opcion == '1':
        numero = int(input('Introduzca el numero: '))
        tiempo_inicial = time.time()
        resultado = enumer_exaust(numero)
        if resultado == -1:
            print(f'{numero} no tiene raiz exacta')
        else:
            print(f'La raiz cuadrada de {numero} es {resultado}')
        print('Tiempo de ejecucion: %s segundos' % (time.time() - tiempo_inicial))
    elif opcion == '2':
        numero = int(input('Introduzca el numero: '))
        tiempo_inicial = time.time()
        resultado = enumer_exaus_aprox(numero)
        if resultado == -1:
            print('No se encontro la raiz cuadrada')
        else:
            print(f'La raiz cuadrada de {numero} es {resultado}')
        print('Tiempo de ejecucion: %s segundos' % (time.time() - tiempo_inicial))
    elif opcion == '3':
        numero = int(input('Introduzca el numero: '))
        tiempo_inicial = time.time()
        resultado = biseccion(numero)
        print(f'La raiz cuadrada de {numero} es : ',resultado)
        print('Tiempo de ejecucion: %s segundos' % (time.time() - tiempo_inicial))
    else:
        print(f'Rey, {opcion} no esta en las opciones!!!')

if __name__ == "__main__":
    main()