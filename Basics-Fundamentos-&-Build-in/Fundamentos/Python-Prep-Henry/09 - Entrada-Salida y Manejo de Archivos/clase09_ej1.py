import sys
# Comprobación de seguridad, ejecutar sólo si se recibe 3 argumentos
if len(sys.argv) == 4:
    print("El primer parámetro es:",sys.argv[1])
    print("El segundo parámetro es:",sys.argv[2])
    print("El tercer parámetro es:",sys.argv[3])
    print("El argumento 0 es el nombre del script:",sys.argv[0])
else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py 1 2 3')