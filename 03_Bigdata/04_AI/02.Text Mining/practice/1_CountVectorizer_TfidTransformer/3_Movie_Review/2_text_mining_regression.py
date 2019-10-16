# 사용 모델: LogitsticRegression
# 고정 변수 항목 : review text에 쓰인 단어들,  단어 빈도
# 분석 목표(예측값) : 리뷰가 긍정인지 부정인지 판별
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

with open('pre_movie_review.pickle', 'rb') as file:
    label, voca, features = pickle.load(file)

# 학습 전용, 테스트 전용 데이터 분리
train_data, test_data, train_label, test_label = train_test_split(features, label)

# 학습
clf = LogisticRegression()
clf.fit(train_data, train_label)

print('학습 데이터 정확도\t: %.4f' % clf.score(train_data, train_label))
print('테스트 데이터 정확도\t: %.4f' % clf.score(test_data, test_label))

weights = clf.coef_[0, :]
pair = []
for index, value in enumerate(weights):
    pair.append((abs(value), voca[index]))
pair.sort(key=lambda x: x[0], reverse=True)
for pr in pair[:20]:
    print('영향도 : %4.4f, 단어: %s' % pr)
