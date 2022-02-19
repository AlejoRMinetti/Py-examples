def main():

    def factorial(n):
        """Calcula el factorial de n.
        Por definicion 0! = 1
        n int
        returns n!
        """
        print(n)
        if n == 0 or n == 1:
            return 1
        
        return n*factorial(n-1)

    n = int(input('Introduce un entero: '))

    print(factorial(n))

if __name__ =='__main__':
    main()