import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
       	return con
    except Error:
        print(Error)
 
def sql_table(con):
 
	cursorObj = con.cursor()

	cursorObj.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

	cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")

	con.commit()


con = sql_connection()
 
sql_table(con)