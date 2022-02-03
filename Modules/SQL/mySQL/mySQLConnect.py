import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.2",
  user="root",
  password="********",
  database="platziblog"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
