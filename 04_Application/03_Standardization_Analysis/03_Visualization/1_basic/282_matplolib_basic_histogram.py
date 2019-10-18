# 히스토그램
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

mu1, mu2, sigma = 100, 130, 15
# mu1, mu2, sigma = 100, 130, 5
#randn(10000) => -1~1 사이의 정규 분포를 갖는 값을 10000개 생성, mean:0, variance:1
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# hist함수 인자
# bins: 수치가 클수록 세로축이 정교해짐
# normed: False일 경우 확률이 아니라 빈도로 표시
# alpha: 투명도

n, bins, patches = ax1.hist(x1, bins=50, normed=False, color='darkgreen')
n, bins, patches = ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
plt.suptitle('Histograms', fontsize=14, fontweight='bold')
plt.title('Two Frequency Distributions')

plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
plt.show()

