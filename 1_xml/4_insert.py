import xml.etree.ElementTree as ET
tree=ET.parse('studentdetails.xml')
root=tree.getroot()
studentslist=root.findall('data/student')
for student in studentslist:
    grade=ET.SubElement(student,'grade')
    grade.text='A'
    student.attrib['key']='hi'



tree.write('output.xml')
