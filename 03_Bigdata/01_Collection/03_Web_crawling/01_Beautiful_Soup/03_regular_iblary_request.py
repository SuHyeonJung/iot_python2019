import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

tag = soup.findAll('tr')
title = re.compile('[>].*</a>')
title1 = title.findall(str(tag))
print(title1)
rank = re.compile('[alt="]\d\d["]')
rank1 = rank.findall(str(tag))
print(rank1)

data = []
# for tr in tag:
#     title = re.compile('[>].*</a>')
#     title1 = title.match(tr)
#     if title1:
#         print(title1)
    # title = tr.find('div', {'class': 'tit3'})
    # rank = tr.find('img')
    # up_down = tr.find('td', {'class': 'range ac'})
    # if rank:
    #     rank1 = rank.attrs.get('alt')
    #     print(rank.attrs.get('alt'))
    #     data.append(rank1)
    # if title:
    #     print(title.a.text)
    #     data.append(title.a.text)
    # if up_down:
    #     print(up_down.text)
    #     data.append(up_down.text)
# print(data)
# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv파일을 생성하세요.

