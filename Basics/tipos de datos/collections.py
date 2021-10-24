# https://docs.hektorprofe.net/python/modulos-y-paquetes/modulo-collections/

from collections import Counter

# devuelve un disccionario con la cantidad de apariciones

l = [1,2,3,4,1,2,3,1,2,1]
count_l = Counter(l)
print("Counter de: ",l," : ",count_l)

count_palabra = Counter("palabra")
print("Counter de palabra: ",count_palabra)

animales = "gato perro canario perro canario perro"
c = Counter(animales.split())
print("Cantidad animales en: ",animales)
print(c)