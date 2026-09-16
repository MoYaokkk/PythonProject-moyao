# 1.先定义类
# 定义动物类
class Animal(object):
    def __init__(self, name):
        self.name = name

    def jiao(self):
        print(f"{self.name}会叫")


# 定义狗类
class Dog(Animal):
    # 重写,加入了自己特有操作
    def jiao(self):
        print(f"{self.name}会汪汪叫")


# 定义猫类
class Cat(Animal):
    # 重写,加入了自己特有操作
    def jiao(self):
        print(f"{self.name}会喵喵叫")


# 2.再根据类创建对象
a = Animal("动物")
d = Dog("旺财")
c = Cat("招财")
# 3.对象调用jiao方法
a.jiao()
d.jiao()
c.jiao()

# 4.如何查看继承关系(调用方法顺序)
print(Dog.mro())
print(Cat.mro())