# -*- coding: utf-8 -*-

def protected(func):

    def wrapper(password):

        if password == 'platzi':
            return func()
        else:
            print('La contrasenia es incorrecta')

    return wrapper

# decorator:
@protected
def protected_func():
    print('Tu contrasenia es correcta.')


if __name__ == '__main__':
    password = str(input('Ingresa tu contrasenia: '))

    protected_func(password)