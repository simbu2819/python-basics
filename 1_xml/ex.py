import xml.etree.ElementTree as ET
add="http://py4e-data.dr-chuck.net/comments_145802.xml"

tree=ET.parse(add)
root=tree.getroot()

studentslist=root.findall('data/student/branch'.text='mca')
tree.write('output.xml')
