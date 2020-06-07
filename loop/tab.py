import time,webbrowser
tnb=3
breaks=0

print("Time :",time.ctime())
while(breaks<tnb):
    time.sleep(10)
    webbrowser.open("https://python.org")
    breaks+=1
