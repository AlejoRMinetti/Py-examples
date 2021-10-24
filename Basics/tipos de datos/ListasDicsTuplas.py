# Dictionary van con {}, tuples van con () y listas con []

####################### Listas ####################################

# Metodos:
# https://www.programiz.com/python-programming/methods/list

# index & element
a = ["Hello", "World"]
print("\nPrinting each element and their index")
for i,e in enumerate(a):
  print("Index: {}, was: {}".format(i, e))

################## Dictionary - SoloLearn #########################
  
# key in a dictionary
nums = { 1: "one", 2: "two",  3: "three" }
print(1 in nums)
print("three" in nums)
print(4 not in nums)
#True
#False
#True

#usando get
pairs = {1: "apple",
"orange": [2, 3, 4], 
True: False, 
None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
#[2, 3, 4]
#None
#not in dictionary

# para evitar:
primary = {
"red": [255, 0, 0], 
"green": [0, 255, 0], 
"blue": [0, 0, 255], 
}
print(primary["red"])
#print(primary["yellow"])
#[255, 0, 0]
#KeyError: 'yellow'

# read from dict
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
# 24
# 42

#Only immutable objects can be used as keys to dictionaries
# bad_dict = { [1, 2, 3]: "one two three",}
#TypeError: unhashable type: 'list'

#add to dictionary
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)
#{1: 1, 2: 4, 3: 9, 4: 16, 8: 64}

# add list to dictionary
dicList = { "lista1": [1,2,3]}
dicList["lista2"] = [[4,5,6]]
print("add list to dictionary",dicList)

# mas ejemplos:
# https://www.w3schools.com/python/python_dictionaries.asp