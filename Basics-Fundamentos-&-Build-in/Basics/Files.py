

# Open a file
fo = open("foo.txt", "r+")
str = fo.read()
print("Read String is : ", str) 

'''
# open, lee todo y siempre cierra
try:
   with open("filename.txt") as f:
    print(f.read())
finally:
   f.close()

# open como write borra archivo
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

# cantidad escrita
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

# leer como una lista separadas por lineas del txt
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close() 

# o con readlines
file = open("filename.txt", "r")
print(file.readlines())
file.close()

'''