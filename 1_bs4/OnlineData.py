import urllib.request as req
from bs4 import BeautifulSoup
address="https://www.w3schools.com/default.asp"
while True:
    data=req.urlopen(address).read()
    if data:
        break

soup=BeautifulSoup(data,'html.parser')
al=soup('img')
for b in al:
    print(b.get('src'))
