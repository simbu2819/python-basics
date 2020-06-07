import sqlite3
con=sqlite3.connect("college.db")
cursor=con.cursor()
rollno=input("entr rollnumber: ")
#name=input("enter name : ")
#branch=input("enter branch : ")
try:
    query="delete from studentdetails where RollNumber=?"
    
    cursor.execute(query,(rollno,))
    op=input("are you sure to delete record ? \n")
    if(op=='yes'):
        con.commit()
        print("delete..")
    else:
        print("cancel operation...")
   
except Exception as e:
    print(e)

cursor.close()
con.close()

