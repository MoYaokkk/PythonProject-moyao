"""
位置传参: 实参和形参的顺序和个数都要一致
关键字传参: 实参和形参的个数必须一致,顺序无所谓
默认参数: 定义函数的时候提前设置好默认值,如果用户没传参就用默认的,如果用户传参了,就用新传入的
可变参数:
    *args: 以元组的形式接收位置参数
    **kwargs: 以字典的形式接收关键字参数
"""


# 1.先定义函数
def show1(name, age, weight):
    print(f"姓名:{name},年龄{age}岁,体重{weight}kg")


# 默认参数
def show2(name = '张三', age = 18, weight = 18):
    print(f"姓名:{name},年龄{age}岁,体重:{weight}kg")


# 可变参数:
# *args: 以元组的形式接收位置参数
def show3(*args):
    print(args, type(args))


# **kwargs: 以字典的形式接收关键字参数
def show4(**kwargs):
    print(kwargs, type(kwargs))


def show5(*args, **kwargs):
    print(args)
    print(kwargs)


# 2.再调用函数
if __name__ == '__main__':
    # 位置传参
    show1('张三', 18, 66)
    # 关键字传参
    show1(name = '张三', weight = 75, age = 28)
    # 默认参数
    show2()
    # 可变参数: 位置参数
    show3(1,2,3)
    # 可变参数: 关键字传参
    show4(a=1, b=2, c=3)
    # 可变参数: 位置传参和关键字传参
    show5(1, 2, 3, a=7, b=8, c=9)
