import urllib.request as ur
import xml.etree.ElementTree as et

url='http://py4e-data.dr-chuck.net/comments_150900.xml'
while True:
    data=ur.urlopen(url).read().decode()
    if data:
        break



root=et.fromstring(data)
studentlist=root.findall('comments/comment')
print('total',end="=")
'''
for student in studentlist:
    print(student.find('name').text,end='\t\t\t')
    print(student.find('count').text)


total1=0
for num in studentlist:
        total=num.find('count').text
        total1+=int(total)
      
print("\n\n\t\t total=",total1)            

fh=open('task.txt','w')

fh.write(str(total1))

fh.close()


'''
total=[]
for num in studentlist:
    ab=num.find('count').text
    value=int(ab)
    total.append(value)
    
    
print(sum(total))
