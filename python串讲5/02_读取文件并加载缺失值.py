# 1.导包
import pandas as pd
import numpy as np
# 2.读取文件
# 方式1: 默认keep_default_na是True
# 代表自动用NaN填充所有缺失值(空,NULL,null,None,NA,nan)
df = pd.read_csv('data/survey_visited.csv')
print(df)
print('---------------------------')
# 方式2: 修改keep_default_na为False
# 代表所有缺失值(空,NULL,null,None,NA,nan)位置不填充NaN
df = pd.read_csv('data/survey_visited.csv', keep_default_na=False)
print(df)
print('---------------------------')
# 方式3: 修改keep_default_na为False,使用na_values指定要用NaN填充的值
# 代表所有缺失值(空,NULL,null,None,NA,nan)位置不填充NaN,这些地方填na_values=[None, np.nan, pd.NA]
df = pd.read_csv('data/survey_visited.csv', keep_default_na=False, na_values=[None, np.nan, pd.NA])
print(df)
print('---------------------------')
