import xml.etree.ElementTree as ET
tree=ET.parse('studentdetails.xml')
root=tree.getroot()
studentslist=root.findall('data/student')
for student in studentslist:
    student.find('branch').text='mca'
    #print(student.find('branch').text)
    myDict=student.attrib
    myDict['active']="ok"


    
tree.write('output.xml')
