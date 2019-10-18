# 회귀선과 일변량 히스토그램을 포함한 산점도
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

tips = sns.load_dataset('tips')
print(tips.head(100))
sns.lmplot(x="total_bill", y="tip", data=tips)

plt.show()