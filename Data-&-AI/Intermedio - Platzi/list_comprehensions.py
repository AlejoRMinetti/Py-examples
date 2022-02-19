def run():
    squares = []
    for i in range(1,101):
        squares.append(i**2)
    print(squares)

    squares = [num**2 for num in range(1,101)];
    print(squares)

    # filter with list comprehensions
    filteredSquares = [num**2 for num in range(1,101) if num % 3 !=0]
    print(filteredSquares)

    #challenge
    challengeList = [num for num in range(1,9999) if (num % 4 == 0 
    and num % 6 == 0 and num % 9 == 0) ]
    print(challengeList)


if __name__ == '__main__':
    run()