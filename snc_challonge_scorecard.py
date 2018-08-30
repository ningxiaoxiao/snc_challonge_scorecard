import urllib
from urllib import request
import csv
from bs4 import BeautifulSoup



headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}  
req=urllib.request.Request(url='https://challonge.com/wy8ezemk',headers=headers)
page=urllib.request.urlopen(req)
soup=BeautifulSoup(page)

rank=""
participant=""
matchinfo=""
byes=""
score=""
tb=""
buchholz=""
pts=""

table=soup.find('table')
f=open('table.csv','w')
cw=csv.writer(f)
cw.writerow( ['rank','participant','matchinfo W-L','byes','score','tb','buchholz','pts'])
for row in table.findAll("tr"):
    cell=row.findAll("td")
    
    if len(cell) == 8:
        rank=cell[0].find(text=True)
        participant=cell[1].find(text=True)
        
        
        matchinfo=cell[2].find(text=True)

        byes=cell[3].find(text=True)
        score=cell[4].find(text=True)
        tb=cell[5].find(text=True)
        buchholz=cell[6].find(text=True)
        pts=cell[7].find(text=True)

        participant=participant.replace('\n','')
        matchinfo=matchinfo.replace(' ','')
        matchinfo=matchinfo[:3]
        
        cw.writerow([rank,participant,matchinfo,byes,score,tb,buchholz,pts])
        
    

f.close()