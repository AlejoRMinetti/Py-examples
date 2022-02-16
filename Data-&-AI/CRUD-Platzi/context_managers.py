""" Los context managers son objetos de Python que proveen información contextual 
adicional al bloque de código. Esta información consiste en correr una función 
(o cualquier callable) cuando se inicia el contexto con el keyword with; al igual 
que correr otra función cuando el código dentro del bloque with concluye. 
Por ejemplo: """

with open(‘some_file.txt’) as f:
    lines = f.readlines()

""" Si estás familiarizado con este patrón, sabes que llamar la función open de 
esta manera, garantiza que el archivo se cierre con posterioridad. Esto disminuye 
la cantidad de información que el programador debe manejar directamente y facilita 
la lectura del código.

Existen dos formas de implementar un context manager: con una clase o con un 
generador. Vamos a implementar la funcionalidad anterior para ilustrar el punto:
 """

class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()

""" Esta es simplemente una clase de Python con dos métodos adicionales: enter y exit. 
Estos métodos son utilizados por el keyword with para determinar las acciones de inicialización, entrada y salida del contexto.

El mismo código puede implementarse utilizando el módulo contextlib que forma parte 
de la librería estándar de Python.
 """

from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()

""" El código anterior funciona exactamente igual que cuando 
lo escribimos con una clase. La diferencia es que el código 
se ejecuta al inicializarse el contexto y retorna el control 
cuando el keyword yield regresa un valor. Una vez que termina 
el bloque with, el context manager toma de nueva cuenta el control 
y ejecuta el código de limpieza. """