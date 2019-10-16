import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

with open('processed.pickle', 'rb') as file:
    voca, features, labels = pickle.load(file)

# 학습 전용, 테스트 전용 데이터 분리
train_data, test_data, train_label, test_label = train_test_split(features, labels, test_size=0.3, random_state=1)


# 학습
clf = LogisticRegression()
clf.fit(train_data, train_label)

print('학습 accuracy: %4.4f' % clf.score(train_data, train_label))
print('테스트 accuracy: %4.4f' % clf.score(test_data, test_label))

weights = clf.coef_[0, :]
pair = []
for index, value in enumerate(weights):
    pair.append((abs(value), voca[index]))
pair.sort(key=lambda x: x[0], reverse=True)
for pr in pair[:20]:
    print('score %4.4f 단어: %s' % pr)
