# 1.导包
import numpy as np
import pandas as pd
# 2.创建pandas对象
# 此处咱们用最简单的方式创建: 把列表转换为pandas对象
# 2.1创建Series对象
my_list1 = [10, 20, 30, 40]
print(my_list1, type(my_list1))
s = pd.Series(my_list1, name='nums')
print(s, type(s))   # Series只能组成一列
# 2.2创建DataFrame对象(类似表格)
my_list1 = [10, 20, 30, 40]
df1 = pd.DataFrame(my_list1, columns=['nums1'])
print(df1, type(df1))   # 类似表格中只有1列的情况

my_list2 = [[10, 11], [20, 21], [30, 31], [40, 41]]
df2 = pd.DataFrame(my_list2, columns=['nums1', 'nums2'])
print(df2, type(df2))   # 类似表格中有4行2列
print('====================================================')
# 3.pandas相比numpy多了行列索引和标签
# 需求: 获取df2的第2列
print(df2['nums2'])
# 需求: 获取df2的第2列的总和,平均,最大值,最小值
print(df2['nums2'].sum())
print(df2['nums2'].mean())
print(df2['nums2'].max())
print(df2['nums2'].min())