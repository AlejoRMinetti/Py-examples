def mult_dos(n):
    return n * 2

def sum_dos(n):
    return n + 2

def ap_oper(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    print(resultados)

nums = [1, 2, 3]
print('Numeros: ', nums)
ap_oper(mult_dos, nums)
ap_oper(sum_dos, nums)


# Funciones lambda

sumar = lambda x, y: x + y
print('Funcion lambda: ',sumar(2, 3))


#funciones en estructuras de datos

def aplicar_operaciones(num):
    operaciones = [abs,float,str,mult_dos,sum_dos]
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    return resultado

print('funciones en estr de datos: ',aplicar_operaciones(-2))
