# 1.导包
import numpy as np
import pandas as pd
# 2.读取文件
# csv: 具有固定分隔符的结构化数据,都是csv格式,不用关注后缀名是不是csv
df = pd.read_csv('data/gapminder.tsv', sep='\t')    # \t是制表符
print(df.shape) # (1704, 6)
# df.info()
# 3.分析数据(分组聚合操作)
# todo 需求1: 求每个年份的平均寿命
# TODO 方式1: 原生聚合函数
# 伪sql: select avg(聚合字段名) from 表明 group by 分组字段名;
# 伪sql: select avg(lifeExp) from 表明 group by year;
print(df.groupby('year').agg({'lifeExp': 'mean'}))      # 字典中可以传递多个字段和对应的聚合函数
print('==========================')
# TODO 方式2: 透视表
# index指定分组字段,values指定聚合字段,aggfunc指定聚合函数
result = df.pivot_table(index=['year'], values='lifeExp', aggfunc='mean')
print(result)
