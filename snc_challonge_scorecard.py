#!/usr/bin/python3

import urllib
from urllib import request
import csv
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
req = urllib.request.Request(
    url='https://challonge.com/wy8ezemk', headers=headers)
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page,features="html.parser")

rank = ""               # 排名
participant = ""        # 参赛者
matchinfo = ""          # 比赛比分 胜-负
#byes=""                #
score = ""              # 积分 胜积1分 负积0分
tb = ""                 # 小分 对阵相同积分对手胜场数
buchholz = ""           # 比赛分 所有胜场对手积分,去掉最大最小
#pts = ""               # 胜负差

table = soup.find('table')
f = open('table.csv', 'w', encoding='utf-8-sig')
cw = csv.writer(f)
cw.writerow(['排名', '参赛者', '比赛比分 W-L', '积分', '小分', '比赛分'])
for row in table.findAll("tr"):
    cell = row.findAll("td")

    if len(cell) == 8:
        rank = cell[0].find(text=True)
        participant = cell[1].find(text=True)

        matchinfo = cell[2].find(text=True)

        # byes=cell[3].find(text=True)
        score = cell[4].find(text=True)
        tb = cell[5].find(text=True)
        buchholz = cell[6].find(text=True)
        #pts = cell[7].find(text=True)

        participant = participant.replace('\n', '')
        matchinfo=matchinfo.replace(' ','')
        matchinfo = matchinfo[:3]

        cw.writerow([rank, participant, matchinfo, score, tb, buchholz])


f.close()
