"""快捷写法"""
"""
推导式:就是python中生成列表,集合,字典,生成器快捷方式
"""
# 需求: 准备1个列表,里面存储1到10
l1 = [i for i in range(1,11)]
print(l1)
# 需求: 准备1个列表,里面存储1到10的偶数
l2 = [i for i in range(1,11) if i % 2 == 0]
print(l2)
print(type(l1), type(l2))
print('===============================================')
# 需求: 准备1个集合,里面存储1到10
s1 = {i for i in range(1,11)}
print(s1)
# 需求: 准备1个集合,里面存储1到10的偶数
s2 = {i for i in range(1,11) if i % 2 == 0}
print(s2)
print(type(s1), type(s2))
print('===============================================')
# 需求: 准备1个字典,里面存储1到10
d1 = {i: i for i in range(1,11)}
print(d1)
# 需求: 准备1个字典,里面存储1到10的偶数
d2 = {i: i**3 for i in range(1,11) if i % 2 == 0}
print(d2)
print(type(d1), type(d2))