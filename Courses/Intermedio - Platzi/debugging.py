def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1: # corriendo el debug, se ve que == 0
            divisors.append(i)
    return divisors


def run():
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print("Terminó mi programa")
    

# Usando el debugger encontrar el error
if __name__ == '__main__':
    run()