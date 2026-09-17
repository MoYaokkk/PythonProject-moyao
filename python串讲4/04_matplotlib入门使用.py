# 1.导包
import random
import matplotlib.pyplot as plt
# 解决个别版本show()无法展示的问题
import matplotlib
matplotlib.use('TkAgg')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 需求: 绘制每个月销量曲线图
# 2.准备测试数据
a = [i for i in range(1, 13)]   # 12个月份
nums = [random.randint(0, 100) for i in a]   #每个月份对应的销量

# 3.绘图
# plt.plot()画图默认折线图
plt.plot(a, nums)
# 添加标题
plt.title('matplotlib入门案列')
# 添加坐标
plt.xlabel('月份')
plt.ylabel('销量')
# 添加网格
plt.grid()
# 展示图
plt.show()