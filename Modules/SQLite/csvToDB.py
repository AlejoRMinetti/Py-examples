import sqlite3
import csv
import codecs

from sqlite3 import Error
from datetime import datetime
 
def sql_connection(dbName):
	try:
		con = sqlite3.connect(dbName)
		return con
	except Error:
		print(Error)



def sql_createTable(SqlDBCon, tablaName, Columns):
	cursorObj = SqlDBCon.cursor()
	# creando tabla de velas
	cursorObj.execute("CREATE TABLE IF NOT EXISTS "+tablaName+"( "+Columns+" )")



def sql_csvToDB(SqlDBCon, csvFile, tablaName):
	cursorObj = SqlDBCon.cursor()
	with codecs.open(csvFile, 'rU', 'utf-16') as csv_file:
		csv_reader = csv.reader(csv_file)
		line_count = 0
		Columns = ""
		for row in csv_reader:
			if line_count == 0:
				Columns = f'{", ".join(row)}'
				print(f'Column names are: {Columns}')
				
			else:
				date = datetime.strptime(row[0], '%Y.%m.%d %H:%M')
				row[0] = date.strftime("%Y-%m-%d %H:%M")
				cursorObj.execute("INSERT INTO "+tablaName+"("+Columns+")VALUES(?,?)", row)
				#print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
			line_count += 1
	
	con.commit()
	print(f'Lineas porcesadas: {line_count}')



if __name__ == '__main__':
	# connect to dataBase and create table
	con = sql_connection('trading.db')
	sql_createTable(con, "ZZEurUsd4H", 
		"Date datetime PRIMARY KEY, ZZval decimal")
	# recorrer csv y agregar a la db
	sql_csvToDB(con, 'ZZEurUsd4H12,6,3.csv', "ZZEurUsd4H")

