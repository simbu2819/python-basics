import json
fh=open('students_details.json')
py_data=json.load(fh)



a=py_data['students']
print("name\tbranch\tgrade \tid")

"""for sa in a:
    print(sa['name'],sa['branch'],sa['grade'],sa['id'],sep='\t')

"""
for sa in a:
    keys=sa.keys()
    for each in keys:
        print(sa[each],indent=4)
fh.close()
