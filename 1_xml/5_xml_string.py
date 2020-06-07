import xml.etree.ElementTree as ET
xml_data='''
<students_info>
	<info>This is simple and sample Students details </info>
	<data>
		<student active="True">
			<name> Sai </name>
			<branch> CSE </branch>
			<id> 1 </id>
		</student>

		<student active="False">
			<name> Ram </name>
			<branch> IT </branch>
			<id> 2 </id>
		</student>
	</data>
</students_info>
'''
#fromstring(stringTypeofXMLdata)
root=ET.fromstring(xml_data)
studentlist=root.findall('data/student')
for student in studentlist:
    print(student.find('name').text)






xml_out_string=ET.tostring(root).decode()
print(xml_out_string)
fh=open('1_out.xml','w')
fh.write(xml_out_string)
fh.close()
