fh=open(r"C:\Users\exam\Desktop\16f61f0035\files\mybook.txt","r")


#data=fh.read()
#print(data)

"""for line in fh:
    print(line,end="")
"""
"""
count=0

for line in fh:
    count+=1
    if count==2:
        print(count,line)


"""

"""
fh.read()
    it read and return data from present cursor position
    return type string
fh.read()
    it read and return one line from present cursor position
    return type string 
fh.readline()
    it read and return all the lines from present cusor position
    return type list
"""

#fh.readline()
line2=fh.readline()
print(line2)
#print(fh.read())
print(fh.tell())
fh.close()
