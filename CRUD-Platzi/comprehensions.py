""" Python Comprehensions """

""" Las Comprehensions son constructos que nos permiten generar una secuencia a partir de otra secuencia.
Existen tres tipos de comprehensions: """

# List comprehensions
# [element for element in element_list if element_meets_condition]

# Dictionary comprehensions
# {key: element for element in element_list if element_meets_condition}

# Sets comprehensionsa
# {element for element in element_list if elements_meets_condition}

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y) # La función zip() regresa un iterador de tuplas.
print("lista de tuplas: {}".format(list(zipped)) ) # [(1, 4), (2, 5), (3, 6)]

# Diccionario a partir de listas
student_uid = [1, 2, 3]
students = ["Juan", "Pedro", "Robertito"]
student_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print("Creando diccionario: {} \nA partir de la lista de uid {} y la lista de los nombres {}".format(student_with_uid, student_uid, students))