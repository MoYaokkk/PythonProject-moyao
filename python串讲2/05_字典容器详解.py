"""容器"""
"""
字典: 用大括号{},每个元素是键值对 k:v
注意: 字典的键不能重复,所以键只能是不可变类型,但是值可以是任意类型

字典不支持索引!!!但是可以根据键key找value值
"""
# 1.定义空字典
d1 = {}
print(d1, type(d1))
d1 = dict()
print(d1, type(d1))
# 2.定义非空字典
# 注意: 字典key如果重复,那么后面的值会覆盖前面的值,本质是一个修改操作
d2 = {"name": '张三', "age": 18}
print(d2, type(d2))
d2 = {"name": '张三', "age": 18, 'name': '李四'}
print(d2, type(d2))
# 3.字典的嵌套
stu_score = {
    "张三": {'语文': 99, '数学': 88},
    "李四": {'语文': 69, '数学': 38},
    "王五": {'语文': 19, '数学': 98},
}
# 根据key获取值
# 需求: 查找张三的所有考试成绩
print(stu_score['张三'])
print(stu_score.get('张三'))
# 需求: 查找张三的语文考试成绩
print(stu_score['张三']['语文'])
print(stu_score.get('张三').get('语文'))
print('==========================')
# 4.字典的查询操作
# 需求: 获取stu_score元素个数
print(len(stu_score))
# 需求: 判断张三是否在字典中
print('张三' in stu_score)
print('==========================')
# 5.字典的增删改操作
stu_dict = {}
print(stu_dict)
# 增 如果key不存在就是新增
stu_dict['张三'] = 18
print(stu_dict)
# 改 如果key存在,就是修改
stu_dict['张三'] = 28
stu_dict['李四'] = 28
stu_dict['王五'] = 28
print(stu_dict)
# 删 del 字典[key]
del stu_dict['张三']
print(stu_dict)
# 删 pop()
stu_dict.pop('李四')
print(stu_dict)
# 删 clear()
stu_dict.clear()
print(stu_dict)
print('==========================')
score = {"语文": 88, "数学": 99, "英语": 100}
# 需求: 查询所有的学科
print(score.keys())
# 需求: 查询所有的成绩
print(score.values())
# 需求: 查询所有的键值对元组
print(score.items())