import urllib.request as req
from bs4 import BeautifulSoup
address="http://py4e-data.dr-chuck.net/known_by_Kelso.html"
while True:
    data=req.urlopen(address).read()
    if data:
        break

soup=BeautifulSoup(data,'html.parser')
a=soup('a')

for hf in a:
    print(hf,end="")
        
      
