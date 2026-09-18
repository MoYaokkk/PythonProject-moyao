# 1.导包
import numpy as np
import pandas as pd

# 2.先认识空值
print(None, type(None))     # 原生python中的空值
print(np.nan, type(np.nan))     # numpy中的空值
print(pd.NA, type(pd.NA))    # pandas中的空值

# 3.空值判断操作
# 注意: 一般pandas中使用isna(),notna()判断,而不使用==
# isna()和isnull() 判断是否是空值 (推荐)
print(pd.isna('null'))  # False
print(pd.isna(''))  # False
print(pd.isna(None))    # True
print(pd.isna(np.nan))    # True
print(pd.isna(pd.NA))    # True
print('-------------------------------')
# notna()和notnull() 判断是否不是空值
print(pd.notna('null'))  # True
print(pd.notna(''))  # True
print(pd.notna(None))    # False
print(pd.notna(np.nan))    # False
print(pd.notna(pd.NA))    # False