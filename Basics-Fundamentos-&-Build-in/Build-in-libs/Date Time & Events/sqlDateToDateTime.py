######### example sqlDatetoDatetime
import sqlite3

from datetime import datetime

# connect to database
def sql_connection():
    try:
        db = sqlite3.connect('trading.db')
        return db
    except:
        print("Error al intentar abrir trading.db")

db = sql_connection()

"""
## para crear la tabla
cursorObj = db.cursor()
cursorObj.execute("CREATE TABLE IF NOT EXISTS ZZeurusd10M( Date datetime PRIMARY KEY, ZZval decimal)")
cursorObj.execute("INSERT INTO ZZeurusd10M VALUES('2016-01-04', 1.1)")
cursorObj.execute("INSERT INTO ZZeurusd10M VALUES('2016-01-08', 1.2)")
db.commit()
"""

startDateStr = "2016.07.08 00:00"
startDate = datetime.strptime(startDateStr, '%Y.%m.%d %H:%M')
# getting previos zigzagValues
cursorSql = db.cursor()
cursorSql.execute("""SELECT Date, ZZval FROM ZZeurusd10M
    WHERE Date <= date(?) limit 3""", (startDate.strftime("%Y-%m-%d %H:%M"),) ) 
zzVals = cursorSql.fetchall()
for zzVal in zzVals:
    print(type(zzVal[0]))
    print(zzVal[0])
    date = datetime.strptime(zzVal[0], '%Y-%m-%d')
    print(type(date))
    print(date)
