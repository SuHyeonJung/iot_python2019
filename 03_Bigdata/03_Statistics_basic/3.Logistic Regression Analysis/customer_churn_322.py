#목적: 로지스틱 회귀(Logistic Regression) 분석 기본 정보 확인
import pandas as pd
import numpy as np
import statsmodels.api as sm

churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']

dependent_variable = churn['churn01']
independent_variable = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variable_with_constant = sm.add_constant(independent_variable,
                                                     prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variable_with_constant).fit()
print(logit_model.summary())
print("\nCoefficients:\n%s" % logit_model.params)
print("\nCoefficient Std Errors:\n%s" % logit_model.bse)




