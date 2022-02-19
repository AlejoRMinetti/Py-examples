
def primera_letra(lista_palabras):
    primeras_letras = []

    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es str'
            assert len(palabra) > 0, 'No se permiten str vacios'
            
            primeras_letras.append(palabra[0])
        
        except AssertionError as e:
            print(e)
        
    return primeras_letras

lista = ['Angel','Armando','', 'E',26]

print('Lista: ',lista)
print('lista de primeras letras correctas: ',primera_letra(lista))
