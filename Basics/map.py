# map examples

def to_upper_case(s):
    return str(s).upper()

def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

print("map() with string using to_upper_case of abc")
map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)

print("map() with tuple")
map_iterator = map(to_upper_case, (1, 'a', 'abc'))
print_iterator(map_iterator)

print("map() with list")
map_iterator = map(to_upper_case, ['x', 'a', 'abc'])
print_iterator(map_iterator)

print("Converting map to list, tuple, set")
map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_list = list(map_iterator)
print(my_list)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_set = set(map_iterator)
print(my_set)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_tuple = tuple(map_iterator)
print(my_tuple)

print("map() with lambda lambda x: x * 2 to [1, 2, 3, 4]")
list_numbers = [1, 2, 3, 4]
map_iterator = map(lambda x: x * 2, list_numbers)
print_iterator(map_iterator)

print("map() multiple iterable arguments")
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print_iterator(map_iterator)

print("with multiple iterable arguments of different sizes")
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8, 9, 10)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print_iterator(map_iterator)

map_iterator = map(lambda x, y: x * y, tuple_numbers, list_numbers)
print_iterator(map_iterator)