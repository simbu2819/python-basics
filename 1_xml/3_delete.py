import xml.etree.ElementTree as ET
tree=ET.parse('studentdetails.xml')
root=tree.getroot()
studentslist=root.findall('data/student')
for student in studentslist:
    #parent.remove(childTagAddressorObject)
   student.remove(student.find('id'))
   myDict=student.attrib
   myDict.pop('active')

    
tree.write('output.xml')
