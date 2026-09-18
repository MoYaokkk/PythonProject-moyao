# 1.导包
import pandas as pd
# 2.读取数据
train = pd.read_csv('data/titanic_train.csv')
# 3.了解数据
print(train.shape)  # (892, 12)
# train.info()    # 详细信息
print('-------------------------------')
# 4.删除缺失值
"""
dropna(inplace=True): 直接在原有基础上删除
dropna(): 默认是复制一份进行删除,原有的并没有被修改,只是返回了新的
"""
# 4.1 dropna() 默认how='any'直接删除有任意缺失值所在的行
new_train1 = train.dropna()
print(new_train1.shape)     # (183, 12)
print('-------------------------------')
# 4.2 dropna(how='all') 如果整行都是缺失值那就删除,否则保留
new_train2 = train.dropna(how='all')
print(new_train2.shape)     # (891, 12)
print('-------------------------------')
# 4.3 dropna(subset=[列名]) 指定重要列对应位置,有缺失值就删除所在行
# 如果多个列,用列表包裹
new_train3 = train.dropna(subset=["Age"])   # 默认how='any'
print(new_train3.shape)     # (714, 12)
print('-------------------------------')
# 4.4 drop() 直接删除缺失值比较多的那一列
new_train4 = train.drop('Cabin', axis =1)   # 1按照列删除
print(new_train4.shape)     # (892, 11)
