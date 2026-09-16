# 需求: 定义学生类,创建张三和李四对象
# 1.先定义类
class Student(object):
    #__init__()方法: 初始化对象的属性  重点
    def __init__(self, name, age):
        # self就代表对象自己,谁调用当前方法,self就是谁!!!
        self.name = name
        self.age = age

    # __str__()方法: 返回打印对象的内容  了解
    def __str__(self):
        return f"姓名:{self.name},年龄:{self.age}"

    # __del__()方法: 对象删除的时候自动调用  了解
    def __del__(self):
        print(f"{self.name}对象被删除了")

    # 自定义方法
    def study(self):
        print('好好学习,天天向上')


# 2.再根据类创建对象
zs = Student('张三', 18)  # 自动调用__init__()
ls = Student('李四', 20)  # 自动调用__init__()

# 3.默认打印对象,打印的是内存地址,如果有str方法,打印的就是方法返回的字符串
print(zs)
print(ls)

# 4.对象调用属性
print(zs.name)
zs.study()
print(ls.name)
ls.study()

# 默认最后一行代码执行完,程序结束对象就没有用了,GC垃圾回收器自动就会删除对象,自动调用__del__()方法