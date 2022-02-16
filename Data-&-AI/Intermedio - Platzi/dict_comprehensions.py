def run():
    my_dict = {}
    for i in range(1,101):
        my_dict[i] = i**3
    print(my_dict)

    my_dict = {}
    for i in range(1,101):
        my_dict[i] = i**3
    print(my_dict)

    my_dict = {i: i**3 for i in range(1,101) if 1 % 3 != 0}
    print(my_dict)

    #challenge
    import math
    my_dict = {i: math.sqrt(i) for i in range(1,1001) }
    print(my_dict)

if __name__ == '__main__':
    run()