# 1.先定义类
# 定义动物类
class Animal(object):
    def __init__(self, name):
        self.name = name

    def jiao(self):
        print(f'{self.name}会叫')


# 定义狗类
class Dog():
    def __init__(self, name):
        self.name = name

    def jiao(self):
        print(f'{self.name}会汪汪叫')


# 定义猫类
class Cat():
    def __init__(self, name):
        self.name = name

    def jiao(self):
        print(f'{self.name}会喵喵叫')


# TODO 定义公共的API,穿入动物类型对象,调用"叫"方法,实现多态
def animal_jiao(animal: Animal):    # python只能警告,不能限制!!!
    animal.jiao()


# 2.再根据类创建对象,把对象传入到animal_jiao()方法中
d = Dog('旺财')
c = Cat("招财")
animal_jiao(d)
animal_jiao(c)