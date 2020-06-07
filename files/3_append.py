fh=open("mybook2.txt","a")




data=input("enter content: \n " )
fh.write("\n")
fh.write(data)
fh.close()





fh=open("mybook2.txt","r")
print(fh.read())
fh.close()
