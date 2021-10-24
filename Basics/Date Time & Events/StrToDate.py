############## String to dateTime
from datetime import datetime

d1 = '09/19/18 13:55:26'

datetime_object = datetime.strptime(d1, '%m/%d/%y %H:%M:%S')

# datetime to String
print("Año d1: ",datetime_object.strftime("%Y"))

print(type(datetime_object))
print(datetime_object)  # printed in default format

# en otro formato:
d2 = '2016.01.04 22:10'

datetime_object = datetime.strptime(d2, '%Y.%m.%d %H:%M')

print(type(datetime_object))
print(datetime_object)  # printed in default format


# Comparing the dates will return 
# either True or False 
print("d1 is greater than d2 : ", d1 > d2) 
print("d1 is less than d2 : ", d1 < d2) 
print("d1 is not equal to d2 : ", d1 != d2)
print("d1 is equal to d2 : ", d1 == d2) 

