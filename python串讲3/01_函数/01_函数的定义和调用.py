# 为什么要有函数? 为了重用代码,提高代码复用性
"""
函数:
提前组织好的,可以重复使用的,具有特定功能的代码段
1.先定义函数
def  函数名(形参):
    功能代码
    return 结果
2.再调用函数
变量 = 函数名(实参)
"""


# 需求: 定义一个函数用于计算任意两个数的和
def get_sum(a, b):
    sum = a + b
    return sum


print(get_sum(1,2))
print(get_sum(2,2))
print(get_sum(5,4))