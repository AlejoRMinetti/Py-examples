# ejemplo de clase

"""
Métodos especiales

cmp(self,otro)
Método llamado cuando utilizas los operadores de 
comparación para comprobar si tu objeto es menor, 
mayor o igual al objeto pasado como parámetro.

len(self)
Método llamado para comprobar la longitud del objeto. 
Lo usas, por ejemplo, cuando llamas la función len(obj) 
sobre nuestro código. Como es de suponer el método te 
debe devolver la longitud del objeto.

init(self,otro)
Es un constructor de nuestra clase, es decir, es un 
“método especial” que se llama automáticamente cuando
creas un objeto.
"""

class Estudiante(object):
	"""docstring for Estudiante"""
	def __init__(self, nombre_r,edad_r):
		super(Estudiante, self).__init__()
		self.nombre = nombre_r
		self.edad = edad_r

	def hola(self):
		return "Mi nombre es %s y tengo %i años" % (self.nombre, self.edad) 

e = Estudiante("Alejo", 32)
print(e.hola())