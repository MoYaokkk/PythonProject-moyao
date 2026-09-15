"""
输入函数使用格式: 变量 = input(提示语)
    上述格式解释:
        1.先把提示语展示到控制台
        2.input()等待并接受用户的输入内容
        3.把接受到的内容赋值给左边的变量
注意: input()默认接受的都是字符串类型
"""
# 需求: 依次接收用户录入的用户名,年龄,身高
name = input("请您输入用户名:")
age = input("请您输入年龄:")
height = input("请您输入身高:")
# 注意: input()默认接受的都是字符串类型
print('你输入的内容类型:',type(name), type(age), type(height))
print('您输入的内容是:', name, age, height)

#格式化输出变量
# 方式1: 占位符方式 %s给字符串占位 %d给数字占位 %f给浮点数占位
print("您输入的名字是:%s,年龄是:%s,身高是:%s" % (name, age, height))
print("您输入的名字是:%s,年龄是:%d,身高是:%f" % (name, int(age), float(height)))
# 方式2: format方式(推荐)
print(f"您输入的名字是:{name},年龄是:{age},身高是:{height}")
