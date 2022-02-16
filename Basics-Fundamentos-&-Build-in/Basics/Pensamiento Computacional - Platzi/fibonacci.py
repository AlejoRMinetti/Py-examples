def main():

    def fibonacci(n):
        # print(n)
        if n==0 or n==1:
            return 1
        return fibonacci(n-1)+fibonacci(n-2)

    print('Sucesion de fibonacci')
    numero = int(input('Introduce cuantos numeros de fibonacci quieres generar: '))

    for i in range(numero):
        print(i,fibonacci(i))

if __name__ == "__main__":
    main()