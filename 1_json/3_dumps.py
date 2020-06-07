import json
py_data={"name":"ram","active":True}
json_string=json.dumps(py_data,indent=4)
print(json_string)
