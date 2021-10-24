""" En Python, un name, también conocido como identifier, 
es simplemente una forma de otorgarle un nombre a un objeto. 
Mediante el nombre, podemos acceder al objeto. Vamos a ver un ejemplo: """

my_var = 5

id(my_var) # 4561204416
id(5) # 4561204416

""" En este caso, el identifier my_var es simplemente una forma de acceder a 
un objeto en memoria (en este caso el espacio identificado por el número 4561204416). 
Es importante recordar que un name puede referirse a cualquier tipo de objeto (aún las funciones). """

def echo(value):
    return value

a = echo

a(‘Billy’) # 3

""" Ahora que ya entendimos qué es un name podemos avanzar a los namespaces (espacios de nombres). 
Para ponerlo en palabras llanas, un namespace es simplemente un conjunto de names.

En Python, te puedes imaginar que existe una relación que liga a los nombres definidos 
con sus respectivos objetos (como un diccionario). Pueden coexistir varios namespaces en un momento dado, 
pero se encuentran completamente aislados. Por ejemplo, existe un namespace específico que agrupa 
todas las variables globales (por eso puedes utilizar varias funciones sin tener que importar los 
módulos correspondientes) y cada vez que declaramos una módulo o una función, dicho módulo o 
función tiene asignado otro namespace.

A pesar de existir una multiplicidad de namespaces, no siempre tenemos acceso a todos ellos desde 
un punto específico en nuestro programa. Es aquí donde el concepto de scope (campo de aplicación) 
entra en juego.

Scope es la parte del programa en el que podemos tener acceso a un namespace sin necesidad de prefijos.

En cualquier momento determinado, el programa tiene acceso a tres scopes:

El scope dentro de una función (que tiene nombres locales)
El scope del módulo (que tiene nombres globales)
El scope raíz (que tiene los built-in names)
Cuando se solicita un objeto, Python busca primero el nombre en el scope local, luego en el global, y por último, en el raíz. Cuando anidamos una función dentro de otra función, su scope también queda anidado dentro del scope de la función padre.
 """

def outer_function(some_local_name):
    def inner_function(other_local_name):
         # Tiene acceso a la built-in function print y al nombre local some_local_name
         print(some_local_name) 
        
         # También tiene acceso a su scope local
         print(other_local_name)

""" Para poder manipular una variable que se encuentra fuera del scope local podemos utilizar 
los keywords global y nonlocal.
 """

some_var_in_other_scope = 10

def some_function():
     global some_var_in_other_scope
     
     Some_var_in_other_scope += 1