"""容器"""
"""
元组: 用小括号(),元素是任意类型,支持重复
元组是不可变类型!!!
支持索引:
    正索引:从0开始,从左到右依次递增
    负索引:从-1开始,从右到左依次递减
    
元组几乎和列表一样,唯一不同的是不支持修改!!!
"""
# 1.定义空元组
t1 = ()
print(t1, type(t1))
t1 = tuple()
print(t1, type(t1))
# 2.定义非空元组
t2 = ('你好', 10, 3.14, True)
print(t2, type(t2))
# TODO 元组如果存储1个元素,必须加逗号
t2 = ('你好',)
print(t2, type(t2))
# 虽然元组可以存储任意类型,建议存储同类型
name_tuple = ('张三', '李四', '王五')
age_tuple = (18, 28, 38)
# 元组支持嵌套
big_tuple = (name_tuple, age_tuple)
print(big_tuple)
print('===========================')
# 3.元组的索引
names = ('张三', '李四', '王五', '张三', '赵六')
print(type(names))
# 正索引: 0 1 2 3 4
# 负索引:-5-4-3-2-1
# 需求: 获取第1个字符
print(names[0])
print(names[-5])
# 需求: 获取最后1个字符
print(names[-1])
print(names[4])
# 需求: 获取第3个字符
print(names[2])
print(names[-3])
print('===========================')
# 4 查询操作
names = ('张三', '李四', '王五', '张三', '赵六')
print(names)
# 需求: 获取长度
print(len(names))
# 需求: 获取张三的个数
print(names.count('张三'))
# 需求: 判断张三是否在元组中
print('张三' in names)
# 需求: 获取张三的索引位置
print(names.index("张三"))

# TODO 元组不支持修改,所以没有增删改操作!!!