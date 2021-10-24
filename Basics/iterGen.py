# Iterators and generators

for i in range(10):
    print(i)

"""
En este caso, la función range es un iterable que regresa un nuevo 
valor en cada ciclo. Para crear un objeto que sea un iterable, y 
por lo tanto, implemente el protocolo de iteración, debemos hacer 
tres cosas:

    Crear una clase que implemente los métodos iter y next
    iter debe regresar el objeto sobre el cual se iterará
    next debe regresar el siguiente valor y aventar la excepción 
    StopIteration cuando ya no hayan elementos sobre los cual iterar.

Por su parte, los generators son simplemente una forma rápida de 
crear iterables sin la necesidad de declarar una clase que implemente
el protocolo de iteración. Para crear un generator simplemente declaramos
una función y utilizamos el keyword yield en vez de return para regresar
el siguiente valor en una iteración. Por ejemplo,
"""

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

fib1 = fibonacci(20)
fib_nums = [num for num in fib1]

# double_fib_nums = [num * 2 for num in fib1] # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacci(30)] # sí funciona