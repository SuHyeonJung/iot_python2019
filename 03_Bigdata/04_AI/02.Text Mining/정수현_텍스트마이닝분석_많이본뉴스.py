# 과제 수행 목표: 한글 text를 대상으로 한 텍스트마이닝 적용
# 데이터 출처: 웹크로링을 이용한 많이 본 뉴스를 txt로 저장
# 텍스트 데이터: 코드 실행 시 자동으로 생성
# 예측 항목: 주요 어휘 분석
# 어휘 분류 기준:많이 사용된 명사 출현 횟수

import urllib.request
from bs4 import BeautifulSoup
import codecs
from konlpy.tag import Okt

html = urllib.request.urlopen('https://media.daum.net/economic/')
soup = BeautifulSoup(html, 'html.parser')

tag = soup.find('ul', {'class':'tab_aside tab_media'})
tag_baby = tag.find('ol')

data = []
count = 1
for tr in tag_baby:
    if tr == '\n':
        continue
    tag_baby1 = tr.find('a')


    if tag_baby1 == -1:
        continue
    tag_baby1 = tag_baby1.text.strip()
    data.append(tag_baby1)
print(data)
txt_file = 'news_search.txt'
with open(txt_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(data))

fp = codecs.open(txt_file, 'r', encoding='utf-8')
text = fp.read()
okt = Okt()
word_dic = {}
lines = text.split("\r\n")
for line in lines:
    malist = okt.pos(line, norm=True, stem=True)
    for word in malist:
        if word[1] == 'Noun':
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
print('\nStep1] 주요 어휘 분석')
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count))
print()
