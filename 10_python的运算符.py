"""
算术运算符: + - * / // % **
赋值运算符: =
复合赋值运算符: += -= *= /= //= %= **=
比较运算符: == != > >= < <=
逻辑运算符: and or not
"""
# 算术运算符: + - * / // % **
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.33...
print(10 // 3)  # 3
print(10 % 3)   # 1
print(10 ** 3)  # 1000
print('=======================')
# 赋值运算符: =
a = 10
print(a)
print('=======================')
# 复合赋值运算符: += -= *= /= //= %= **=
a += 3  # a = a + 3
print(a)    # 13
a -= 3  # a = a - 3
print(a)    # 10
a *= 3  # a = a * 3
print(a)    # 30
a /= 3  # a = a / 3
print(a)    # 10.0(注意)
a //= 3 # a = a // 3
print(a)    # 3.0
a %= 3  # a = a % 3
print(a)    # 0.0
a **= 3 # a = a ** 3
print(a)    # 0.0
# 比较运算符: == != > >= < <=
print(10 == 3)
print(10 != 3)
print(10 > 3)
print(10 >= 3)
print(10 < 3)
print(10 <= 3)
# 逻辑运算符: and or not
print(False and True)   # 有False则False
print(True or False)    #有True则True
print(not True)         #取反