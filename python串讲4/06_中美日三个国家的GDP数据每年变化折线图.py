# TODO 需求:获取中美日三个国家GDP数据,并绘制每年变化折线图
# 1.导包
import pandas as pd
import matplotlib.pyplot as plt

# 解决个别版本show()无法展示的问题
import matplotlib
matplotlib.use('TkAgg')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 2.读取数据
# 注意: 以后用的多就是通过读取文件,生成df对象
df = pd.read_csv('data/1960-2019全球GDP数据.csv', encoding='gbk', sep=',')

# 3.先了解数据
# print(df.ndim)      # 维度
print(df.shape)     # 形状
# print(df.head())    # 如果不传递参数,默认是5
# print(df.tail())    # 如果不传递参数,默认是5
# print(df.columns)   # 获取所有列名
# print(df.count())   # 各个列的个数
# df.info()           # 基本信息

# 4.数据预处理
df.dropna(inplace=True)
print(df.shape)     # 形状(9930, 3

# 5.数据分析
# todo 需求1: 先查询中美日的gdp数据
df_cn = df[df['country'] == '中国']   # 用的是布尔值
df_us = df[df['country'] == '美国']
df_jp = df[df['country'] == '日本']
# 测试
# print(df_cn.head())
# print(df_us.head())
# print(df_jp.head())
# todo 需求2: 把年份作为索引列
df_cn.set_index('year', inplace=True)
df_us.set_index('year', inplace=True)
df_jp.set_index('year', inplace=True)
# 测试
# print(df_cn.head())
# print(df_us.head())
# print(df_jp.head())
# todo 需求3: 把GDP列名依次修改为中国,美国,日本
df_cn.rename(columns={'GDP': '中国'}, inplace=True)
df_us.rename(columns={'GDP': '美国'}, inplace=True)
df_jp.rename(columns={'GDP': '日本'}, inplace=True)
# 测试
# print(df_cn.head())
# print(df_us.head())
# print(df_jp.head())
# todo 需求4: 可视化展示中美日的每年变化折线图
plt.title('1960-2019年中美日GDP数据折线图')
plt.plot(df_cn.index, df_cn['中国'], label='中国', color='red')
plt.plot(df_us.index, df_us['美国'], label='美国', color='blue')
plt.plot(df_jp.index, df_jp['日本'], label='日本', color='green')
# 添加图例
plt.legend()
# 添加网格
plt.grid()
# 手动展示
plt.show()




