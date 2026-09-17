# TODO 1.导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 解决个别版本show()无法展示的问题
import matplotlib
matplotlib.use('TkAgg')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# TODO 2.numpy负责生成数据
# 此处用numpy随即生成1-100的多个数字,组成5行3列的数组
my_arr = np.random.randint(1, 100, (5, 3))
print(my_arr)
print('--------------------------')
# TODO 3.使用pandas给numpy数据添加索引和标签
df =pd.DataFrame(my_arr, index=['张三', '李四','王五','赵六','田七'], columns=['语文','英语','数学'])
print(df)
print('--------------------------')
# 需求1: 获取各个学科的总成绩
# 方式1: 一个个获取
print(df['语文'].sum())
print(df['英语'].sum())
print(df['数学'].sum())
# 方式2: df整体获取
print(df.sum(axis=0))   # axis=0: 按照列相加
print('--------------------------')
# 需求2: 获取各个同学的总成绩
print(df.sum(axis=1))

# TODO 4.matplotlib可视化数据
fig, ax = plt.subplots()
# 绘制散点图 注意: 下面数据是随便传的,未来根据具体需求决定x,y内容
ax.scatter(x=df["语文"], y=df['数学'])
ax.set_title('综合案例')
plt.show()
