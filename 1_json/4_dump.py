import json
py_1={"name":'sai',"marks":[50,60,70,80,90],"active":True,"work":"simbu"}

fh=open('check.json','w')
b=json.dump(py_1,fh,indent=4)






fh.close()          
