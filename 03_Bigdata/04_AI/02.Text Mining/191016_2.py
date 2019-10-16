import urllib.request
from bs4 import BeautifulSoup
import codecs
from konlpy.tag import Okt

html = urllib.request.urlopen('http://www.daum.net')
soup = BeautifulSoup(html, 'html.parser')

tag = soup.find('ol', {'class':'list_hotissue issue_row list_mini'})
data = []
count = 1
for tr in tag:
    if tr == '\n':
        continue
    tag_baby = tr.find('a')
    if tag_baby == -1:
        continue
    data.append(tag_baby.text)

# print(data)
txt_file = 'search_realtime.txt'
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
