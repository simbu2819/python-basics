import urllib.request as req
from bs4 import BeautifulSoup
address="http://www.dr-chuck.com/page2.html"
while True:
    data=req.urlopen(address).read()
    if data:
        break

soup=BeautifulSoup(data,'html.parser')
al=soup('a')
for b in al:
    print(b.get('href','not available'))
