
z = 9
lst = [0, 1] * z
print(lst[:-1])


def help(x):
	return x % 2 == 0

lst = [i**2 for i in range(10)] 
lst = filter(help, lst) 
print(list(lst)[::2])

# palindrome with slice and lambda
palindrome = lambda string: string == string[::-1]
print(palindrome("neuquen"))