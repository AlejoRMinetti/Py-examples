import datetime

# actual datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) # Tuesday

# set datetime
x = datetime.datetime(2020, 5, 17)
print(x.strftime("%d-%m-%Y")) # 17-05-2020

# print format
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) # others in:  
# https://www.w3schools.com/python/python_datetime.asp

# Para hacer operaciones usar: timedelta
# https://www.programiz.com/python-programming/datetime

# datetime in string format for may 25 1999
input = '25/05/2021'
  
# format
format = '%d/%m/%Y'
  
# convert from string format to datetime format
datetime = datetime.datetime.strptime(input, format)
  
# print for mySQL format
print(datetime.strftime('%Y-%m-%d'))