try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
   #raise NameError("Levantando otra exception")
   raise
finally:
   print("This code will run no matter what")