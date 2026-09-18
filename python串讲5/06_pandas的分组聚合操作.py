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
# 伪sql: select avg(聚合字段名) from 表明 group by 分组字段名;
# 伪sql: select avg(lifeExp) from 表明 group by year;
print(df.groupby('year').lifeExp.mean())        # df.列名是s对象
print(df.groupby('year')['lifeExp'].mean())     # df[列名]是s对象
print(df.groupby('year')[['lifeExp']].mean())     # df[列名]是df对象
print(df.groupby('year').agg({'lifeExp': 'mean'}))      # 字典中可以传递多个字段和对应的聚合函数
print(df.groupby('year').agg({'lifeExp': np.mean}))      # 字典中可以传递多个字段和对应的聚合函数
print('======================')
# todo 需求2: 求每个年份,每个大洲的平均寿命和最高GDP
# 伪sql: select avg(聚合字段名),max(聚合字段名) from 表明 group by 分组字段名1, 分组字段名2;
# 伪sql: select avg(lifeExp),max(gdpPercap) from 表明 group by year,continent;
print(df.groupby(['year', 'continent']).agg({'lifeExp': 'mean', 'gdpPercap': 'max'}))      # 字典中可以传递多个字段和对应的聚合函数
print(df.groupby(['year', 'continent']).agg({'lifeExp': np.mean,'gdpPercap': np.max}))      # 字典中可以传递多个字段和对应的聚合函数
# 课下练习:
# 练习1: 求每年各个国家的平均年龄
print(df.groupby(['year','country']).agg({'lifeExp':'mean'}))
# 练习2: 求每年各个国家的平均年龄和最高gdp
print(df.groupby(['year','country']).agg({'lifeExp':'mean', 'gdpPercap':'max'}))
# 练习3: 单独计算1952年的平均寿命
print(df[df['year'] == 1952]['lifeExp'].mean())
