import urllib.request as ur
import json
url='http://py4e-data.dr-chuck.net/comments_42.json'
while True:
    data=ur.urlopen(url).read().decode()
    if data:
        break

root=json.loads(data)
#a=root['comments']
count=0

for d in root['comments']:
    count+=d['count']
    print(d['count'])
    
#print(root['count'])
print('total')
print(count)

