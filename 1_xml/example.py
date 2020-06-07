import xml.etree.ElementTree

xml.etree.ElementTree.parse('studentdetails.xml').getroot().findall('data/student')
for student in xml.etree.ElementTree.parse('studentdetails.xml').getroot().findall('data/student'):
    print(student.find('name').text)
