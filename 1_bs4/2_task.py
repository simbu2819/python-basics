import urllib.request as req
from bs4 import BeautifulSoup
address="http://py4e-data.dr-chuck.net/comments_150898.html"
while True:
    data=req.urlopen(address).read()
    if data:
        break



soup=BeautifulSoup(data,'html.parser')
al=soup('count')
coun=0
for b in al:
    print(b.find('td').text,end="\t")

    print(b.get_text(),end="\t")
    coun+=int(b.text)




#print("total",end='=')    
print(coun)
