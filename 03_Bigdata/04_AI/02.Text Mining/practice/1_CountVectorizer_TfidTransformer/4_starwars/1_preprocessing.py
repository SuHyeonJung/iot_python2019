# 데이터 출처: https://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220982297456&redurect=Dlog&widgetTypeCall=true


import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

protagonist_header = ' LUKE'
document = []
labels = []

with open('sw_ep', 'r', encoding='UTF8') as file:
    for line in file:
        # 각 줄에서 레이블 부분만 떼어내고 나머지를 documents에 넣는다.
        if line.startswith(protagonist_header):
            labels.append(1)
            document.append(line[len(protagonist_header)+1:])
        else:
            cnt=0
            for line2 in line:
                cnt+=1
                if line2 == ',':
                    break
            labels.append(0)
            document.append(line[cnt:])

vectorizer = CountVectorizer() # 단어 획수 피처를 만드는 클래스
term_counts = vectorizer.fit_transform(document)
voca = vectorizer.get_feature_names()

tf_transformer = TfidfTransformer(use_idf=False).fit(term_counts)
features = tf_transformer.transform(term_counts)

# 처리된 파일을 저장합니다. 앞으로의 예제에서 사용될 예정입니다.
with open('processed.pickle', 'wb') as file:
    pickle.dump((voca, features, labels), file)
