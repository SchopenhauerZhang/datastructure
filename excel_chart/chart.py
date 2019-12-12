import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000', periods=1000), columns=list('ABCD'))
df = df.cumsum()
print(df.plot())


fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

# 默认在最后一个sub_plot上绘图
plt.plot(np.random.randn(50),'k--')
# “k--”：表示黑色虚线

_  = ax1.hist(np.random.randn(100), bins = 20, color='k', alpha=0.3)

ax2.scatter(np.arange(30), np.arange(30)+ 3* np.random.randn(30))