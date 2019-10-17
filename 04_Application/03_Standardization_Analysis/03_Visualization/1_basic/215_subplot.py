import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.figure()
plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,2,3,4],'ro')
plt.subplot(1,2,2)
plt.plot([5,6,7,8],[5,6,7,8],'b')
plt.show()
