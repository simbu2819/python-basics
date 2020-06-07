import sqlite3
con=sqlite3.connect("college.db")
cursor=con.cursor()
rollno=input("entr rollnumber: ")
name=input("enter name : ")
branch=input("enter branch : ")
try:
    query="insert into studentdetails(RollNumber,Name,Branch) values(?,?,?)"
    cursor.execute(query,(rollno,name,branch))

    con.commit()
    print("succefully inserted....!")
except Exception as e:
    print(e)

