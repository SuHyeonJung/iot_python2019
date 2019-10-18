# 산점도

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# 1~14까지 array반환
x = np.arange(start=1, stop=15, step=1)

# 1차 방정식에 준하는 선형회귀 결과를 얻기 위한 분석
y_linear = x + 5 * np.random.randn(14)
# 2차 방정식에 준하는 선형회귀 결과를 얻기 위한 분석
y_quardratic = x**2 + 10 * np.random.randn(14)

# deg=1 : 1차 방정식 형태, deg=2 : 2차 방정식 형태
fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
fn_quardratic = np.poly1d(np.polyfit(x, y_quardratic, deg=2))

fig=plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(x, y_linear, 'bo', x, y_quardratic, 'go', x, fn_linear(x), \
         'b-', x, fn_quardratic(x), 'g-', linewidth=2.)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.set_title('Scatter Plots with Best Fit Lines')
plt.xlabel('x')
plt.ylabel('f(x)')

predict_x = 16
predict_y = fn_linear(predict_x)
print(predict_y)
plt.scatter(predict_x, predict_y)
# X축, Y축 표시 영역 범위 설정
plt.xlim((min(x)-1, predict_x+1))
# predict_x로 변경, predict_x가 더 길이가 넓으므로
plt.ylim((min(y_quardratic)-10, max(y_quardratic)+10))
# y 최대값을 그대로 유지 기존값이 더 크기 때문에

plt.savefig('sxatter_plot.png', dpi=400, bbox_inches='tight')
plt.show()


