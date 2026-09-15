"""容器"""
"""
字符串:用引号包裹,元素是字符,任意类型都可以转换为字符串
字符串是不可变类型
字符串支持索引
    正索引:从0开始,从左到右依次递增
    负索引:从-1开始,从右到左依次递减
"""
# 1.定义空字符串
s1 = ""
print(s1, type(s1))
s1 = ''
print(s1, type(s1))
s1 = """"""
print(s1, type(s1))
s1 = ''''''
print(s1, type(s1))
print('================================')
# 2.定义非空字符串
s2 = "你好"
print(s2, type(s2))
s2 = '你好'
print(s2, type(s2))
s2 = """你好"""
print(s2, type(s2))
s2 = '''你好'''
print(s2, type(s2))
print('================================')
# 3.字符串的索引
# 正索引: 0 1 2 3 4
# 负索引:-5-4-3-2-1
name = '黑马程序员'
# 需求: 获取第1个字符
print(name[0])
print(name[-5])
# 需求: 获取最后1个字符
print(name[4])
print(name[-1])
# 需求: 获取第3个字符
print(name[2])
print(name[-3])
print('================================')
# 4.字符串的功能函数
# 4.1 查询相关函数
# 注意: 字符串功能特别多,这里只介绍常用的
text = "黑马程序员是传智教育旗下的线下教育品牌"
# 需求: 统计text中字符的总个数
print(len(text))
# 需求: 统计text中"教育"和"教"出现的次数
print(text.count("教育"))
print(text.count("教"))
# 需求: 判断text中是否包含"教学"和"教"
print("教学" in text)
print("教" in text)
# 需求: 查询text中"教"出现的正索引位置
print(text.index('教'))  # 从左往右
print(text.rindex('教'))  # 从右往左
# 注意: index和rindex弊端是如果查找的内容不存在就报错
# print(text.index('武')) # 报错
# print(text.rindex('武')) # 报错
print(text.find('教'))   # 从左往右
print(text.rfind('教'))   # 从右往左
# 注意: find和rfind好处是如果查找的内容不存在就返回-1
print(text.find('武'))   # -1
print(text.rfind('武'))   # -1
print('-----------------------------------')
# 4.2 其他函数
# split(): 根据指定符号切割字符串,返回列表
info = '张三,18,狂野AI4期'
info_list = info.split(',')
print(info_list)    # ['张三', '18', '狂野AI4期']
# join(): 把容器(列表)中的元素用指定分隔符连接成字符串
info2 = '-'.join(info_list)
print(info2)    # 张三-18-狂野AI4期

# upper(): 所有字母转换大写
print('abcABC'.upper())
# lower(): 所有字母转换小写
print('abcABC'.lower())

# startswith(x): 判断是否以x开头
print("武常斌".startswith('武'))
print("武常斌".startswith('无'))
# endswith(x): 判断是否以x结尾
print("武常斌".endswith('斌'))
print("武常斌".endswith('彬'))

# replace(): 替换
print("你TMD呀".replace('TMD', '***'))
print("你TMD呀".replace('TMD', '挺萌的'))
print("    张三     ")
print("    张三     ".replace(' ', ''))
# strip(): 去除两端空白
print("    张三     ".strip())
