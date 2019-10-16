import requests # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup # HTML을 파싱하는 모듈

# 웹 페이지를 가져온 뒤 BeautigulSoup 객체로 만듦
response = requests.get('https://www.daum.net/')
soup = BeautifulSoup(response.content, 'html.parser')

# <table class = "table_develop3">을 찾음
table = soup.find('ul', {'class': 'list_favorsch #searchword hide'})
data = []

def data_correction(org_text):
    if org_text == '\xa0':
        return 'N/A'
    return org_text

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = data_correction(td.find('a').text)
            cloud = data_correction(tds[1].text)
            visibility = data_correction(tds[2].text)
            temperature = data_correction(tds[5].text)
            wd_temp = data_correction(tds[7].text)
            data.append([point, cloud, visibility, temperature, wd_temp])
print(data)