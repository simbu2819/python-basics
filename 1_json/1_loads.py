import json
json_data_string='''
{
 "name"  :"rama",
 "branch":"mca",
 "id"    :1,
 "active":true,
 "marks":[60,56,83]


}

'''
py_data=json.loads(json_data_string)


#print(py_data['marks'])
#py_data.pop('id')
#py_data['grade']='A'




print(py_data)
