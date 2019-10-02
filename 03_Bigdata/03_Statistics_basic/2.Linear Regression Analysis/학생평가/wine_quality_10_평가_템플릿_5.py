# 통계 모델:
# 목표 정답률:

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

print("결과 예측하기")
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')
match_dic={}
# 전체 독립변수 식별
columns_list = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']

# 최적의 독립변수 식별
for num in range(1,12):
    combi_list = list(combinations(columns_list, num))
    for tup in combi_list:
        my_formula = 'quality ~ '
        for data in tup:
            my_formula += '%s +'%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=wine).fit()
        dependent_variable = wine['quality']
        independent_variable = wine[list(tup)]
        y_predicted = lm.predict(independent_variable)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0


# hint]
# combinations(,)
# lm = ols(, data=).fit()
# y_predicted = lm.predict()


# 정답률 최대값 찾기
match_dic = sorted(, ,)
# print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d')
print("MAX 조합: %s >> %.2f %%")
