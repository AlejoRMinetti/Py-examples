import sys


def save_to_csv(temperatura,humedad,lluvia):
    """
    Save to lluvia.csv timestamp,temperatura,humedad,lluvia(True or False)
    """
    import datetime
    import os
    marca_de_tiempo = datetime.datetime.now()
    marca_de_tiempo = int(datetime.datetime.timestamp(marca_de_tiempo))
    linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    logs_lluvia = open('lluvia.csv', 'a')
    logs_lluvia.write(linea+'\n')
    logs_lluvia.close()


# Comprobación de seguridad, ejecutar sólo si se recibe 3 argumentos
if len(sys.argv) == 4:
    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    try:
        assert sys.argv == "True" or sys.argv == "False", "lluvia debe ser True o False"
        lluvia = sys.argv[3]
    except:
        lluvia = input("ingrese si llovio como True or False:")
    save_to_csv(temperatura,humedad,lluvia)

elif len(sys.argv) == 2:
    lluvia = sys.argv[1]
    temperatura = input('Ingrese la temperatura en grados centígrados')
    humedad = input('Ingrese el porcentaje de humedad')
    save_to_csv(temperatura,humedad,lluvia)

else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>')

