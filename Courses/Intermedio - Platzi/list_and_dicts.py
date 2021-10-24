def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "GarcÃ­a"}

    super_list = [
        {"firstname": "Facundo", "lastname": "GarcÃ­a"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "JosÃ©", "lastname": "Fernandez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    for key, value in super_dict.items():
        print(key, ">", value)

    for element in super_list:
        print(element)

    listaCienAlCuadrado = [num**2 for num in range(0,100)];
    print(listaCienAlCuadrado)

if __name__ == '__main__':
    run()