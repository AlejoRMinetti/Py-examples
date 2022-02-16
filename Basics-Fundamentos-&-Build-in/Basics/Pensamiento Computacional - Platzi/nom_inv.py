def nombre_inverso(nombre,apellido,inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

print(nombre_inverso('Angel','Estrada'))
print(nombre_inverso('Angel','Estrada',inverso=True))
print(nombre_inverso(apellido='Estrada',nombre='Angel'))


