"""
数据类型: python中的字面量对应的类型
常见的有: 字符串:str   整数:int  浮点数:float   布尔值:bool
注意: 变量本来没有类型,只有字面量数据才有类型
type(x): 查看x的数据类型
"""
# 1.查看字面量类型
print(type('你好'))   # <class 'str'>
print(type(10))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type(True))    # <class 'bool'>
# 2.type()查看变量的类型,本质查看的是变量记录的数据的类型
a = "你好"
print(type(a))       # <class 'str'>

b = 10
print(type(b))       # <class 'int'>

c = 3.14
print(type(c))       # <class 'float'>

d = False
print(type(d))       # <class 'bool'>