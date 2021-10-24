"""
https://likegeeks.com/es/tutorial-de-python-sqlite3/
"""
import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
# Insertar en una tabla

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()
 
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
 
sql_insert(con, entities)

# Actualizar una tabla
def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    con.commit()
 
sql_update(con)

# Obtener todos los datos
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')
    
    rows = cursorObj.fetchall()
    
    for row in rows:
        print(row)
    print("Filas obtenidas: "+len(rows))
 
sql_fetch(con)

# listar tablas
def sql_fetch_tables(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
 
    print(cursorObj.fetchall())
 
sql_fetch_tables(con)

# SQLite3 datetime
import datetime
 
cursorObj = con.cursor()
cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')
data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]
cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data) # Executemany (Inserción por lotes)
con.commit()

# finalmente cerrar Db
con.close()