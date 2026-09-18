# 1.导包
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# 解决个别版本show()无法展示的问题
import matplotlib
matplotlib.use('TkAgg')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 额外安装: pip install openxyl

# 2.加载数据
df = pd.read_excel('data/sales_test.xlsx', index_col='USERID')
# print(df)
# print(df.index)
print(df.shape)
print(df.columns)

# 3.数据预处理
# 删除全部为空的行
sale_data = df.dropna(how='all')
print(sale_data.shape)

# 4.数据分析

# todo 1.获取每个用户最近的购买时间,购买频率,购买金额
R_data = sale_data.groupby(sale_data.index)['ORDERDATE'].max()
F_data = sale_data.groupby(sale_data.index)['ORDERID'].count()
M_data = sale_data.groupby(sale_data.index)['AMOUNTINFO'].sum()

# todo 2.分别结算RFM的分数
F_score = pd.cut(F_data, bins=5, labels=[1, 2, 3, 4, 5])
M_score = pd.cut(M_data, bins=5, labels=[1, 2, 3, 4, 5])
# 设置一个基础时间,计算R分数
base_date = pd.to_datetime('2022-04-01')
R_days = (R_data - base_date).dt.days
R_score = pd.cut(R_days, bins=5, labels=[1, 2, 3, 4, 5])
# print(R_score)
# print(F_score)
# print(M_score)
print('---------------------------')

# todo 3.合并分数
rfm_list = [R_score, F_score, M_score]
rfm_columns = ['r_score', 'f_score', 'm_score']
# transpose()转置
rfm_df = pd.DataFrame(np.array(rfm_list).transpose(), dtype=np.int32, columns=rfm_columns,index=R_data.index)
# print(rfm_df)

# TODO 4.加权得分
# 商家根据自己的需求:设置关注用户交易时间,次数,金额的权重
# 比如: 我设置交易时间:20%,交易总次数:20%,交易总金额:60%
rfm_df['rfm_w_score'] = rfm_df['r_score'] * 0.2 + rfm_df['f_score'] * 0.2 + rfm_df['m_score'] * 0.6
# print(rfm_df)

# TODO 5.1 分析结果可视化
rfm_df['客户分类'] = pd.cut(rfm_df['rfm_w_score'], bins=[0, 2, 3, 5], labels=['低', '中', '高'])
print(rfm_df)
# 绘制柱状图
rfm_df['客户分类'].value_counts().plot(kind='bar', color=['red', 'green', 'blue'])
plt.title('RFM客户分群')
plt.xlabel('会员等级')
plt.ylabel('会员数量')
plt.grid()
plt.show()

# TODO 5.2 分析结果保存到本地
rfm_df.to_csv('data/rfm_score.csv')