import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 200000
    print(f"Factorial de {n}")
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f"Tiempo factorial por bucles {final - comienzo}s")

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f"Tiempo factorial recursivo {final - comienzo}s")