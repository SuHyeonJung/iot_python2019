# 목적: 교차검증(Cross Validation) 라이브러리 활용

import pandas as pd
from sklearn import svm, model_selection
# 붓꽃의 csv 데이터 읽어 들이기
csv = pd.read_csv('iris.csv')
# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하기
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]
# 머신 러닝 모델 생성
clf = svm.SVC()
# 크로스 밸리데이션하기
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean())