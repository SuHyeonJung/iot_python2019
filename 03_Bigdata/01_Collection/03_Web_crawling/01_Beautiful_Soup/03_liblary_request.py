import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.prettify())

tag = soup.findAll('tr')
# up_down = soup.find('img', attrs={'stc':
# 'http://imgmovie.naver.net/2007/img/common/icon_na_1.gif'})
data = []
def data_correction(org_text):
    if org_text == '\xa0':
        return 'N/A'
    return org_text
# rank = tag.find_all('td', {'class': 'ac'})
# title = tag.find_all('div', {'class':'tit3'})
# up_down = tag.find_all('td', {'class':'range ac'})

for tr in tag:
    title = tr.find('div', {'class': 'tit3'})
    if title:
        print(title.a.text)
    # for td in tds:
    #     if td.find('alt'):
    #         point = data_correction(td.find('alt').text)
    #     if td.find('a'):
    #         cloud = data_correction(td.find('a').text)
    #     if td.find('range ac'):
    #         u_d = data_correction(td.find('range ac').text)
    #     else: pass
    #     data.append([point, cloud, u_d])
# print(data)
# print(data)
# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv파일을 생성하세요.

