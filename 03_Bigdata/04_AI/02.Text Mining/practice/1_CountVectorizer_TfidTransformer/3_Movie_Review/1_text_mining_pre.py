# 데이터 출처: https://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220982297456&redurect=Dlog&widgetTypeCall=true


import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

positive = '1\t'
negative = '0\t'
document = []
labels = []

with open('movie_review.txt', 'r', encoding='UTF8') as file:
    for line in file:
        # 각 줄에서 레이블 부분만 떼어내고 나머지를 documents에 넣는다.
        if line.startswith(positive):
            labels.append(1)
            document.append(line[len(positive):])
        elif line.startswith(negative):
            labels.append(0)
            document.append(line[len(negative):])

# CountVectorizer 클래스: 문서를 단어 단위로 쪼개서 각 단어가 몇 번 나왔는지 세어 단어 카운팅 피처를 만든다.
count_vector = CountVectorizer() # 단어 획수 피처를 만드는 클래스
word_counts = count_vector.fit_transform(document)
voca = count_vector.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# 단어 빈도(term frequency)가 생성
# TF: Term Frequency (문서상에 발견된 단어)/(전체 문서상의 단어)
# IDF: Inverse Document Frequency
#   (주요언어: is, of, that 같은 단어는 제외하고 빈도를 측정한다.)
tf_transformer = TfidfTransformer(use_idf=False).fit(word_counts)
features = tf_transformer.transform(word_counts)

# 처리된 파일을 저장합니다. 앞으로의 예제에서 사용될 예정입니다.
with open('pre_movie_review.pickle', 'wb') as file:
    pickle.dump((labels, voca, features), file)
