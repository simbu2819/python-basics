import sqlite3
connect=sqlite3.connect("college.db")
cursor=connect.cursor()

query="select * from studentdetails"
cursor.execute(query)
for rows in cursor.fetchall():
    print(rows[1]+"|"+rows[2])

cursor.close()
connect.close()
