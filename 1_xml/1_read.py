import xml.etree.ElementTree as ET
#to read xml from external file
tree=ET.parse('studentdetails.xml')

#getting root tag from complete tree or data
root=tree.getroot()
studentslist=root.findall('data/student')
print('name \t'+'branch \t'+'no \t'+'age')


for student in studentslist:
    print(student.find('name').text,end='\t')
    print(student.find('branch').text,end='\t')
    print(student.find('id').text,end='\t')
    print(student.find('age').text)
