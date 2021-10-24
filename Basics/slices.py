def q3():
	z = 9
	lst = [0, 1] * z
	print(lst[:-1])

def q4():
	def help(x):
		return x % 2 == 0

	lst = [i**2 for i in range(10)] 
	lst = filter(help, lst) 
	print(list(lst)[::2]) 