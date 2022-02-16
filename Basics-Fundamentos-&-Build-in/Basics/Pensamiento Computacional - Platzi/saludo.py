#Reto clase 8: Cadenas y entradas
#Crear un programa que reciba el nombre del usuario
# y que retorne un saludo, ademas que agregue 
#La longitud de la cadena total de saludo + nombre

nombre = input('¿Como te llamas?: \n')
saludo = f'Hola {nombre}, ¿Como estas?'
longitud = len(saludo)
print(saludo)
print(f'Tamaño de cadena: {longitud}')