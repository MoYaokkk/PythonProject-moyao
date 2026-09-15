"""容器"""
"""
列表: 用中括号[],元素是任意类型,支持重复
列表是可变类型
支持索引
    正索引:从0开始,从左到右依次递增
    负索引:从-1开始,从右到左依次递减

"""
# 1.定义空列表
l1 = []
print(l1, type(l1))
l1 = list()
print(l1, type(l1))
print('===========================')
# 2.定义非空列表
l2 = ['你好', 10, 3.14, True]
print(l2, type(l2))
# 虽然列表可以存储任意类型,建议存储同类型
name_list = ['张三', '李四', '王五']
age_list = [18, 28 ,38]
# 列表支持嵌套
big_list = [name_list, age_list]
print(big_list, type(big_list))
print('===========================')
# 3.列表的索引
names = ['张三', '李四', '王五', '张三', '赵六']
# 正索引: 0 1 2 3 4
# 负索引:-5-4-3-2-1
# 需求: 获取第一个字符
print(names[0])
print(names[-5])
# 需求: 获取最后1个字符
print(names[-1])
print(names[4])
# 需求: 获取第3个字符
print(names[2])
print(names[-3])
print('===========================')
# 4.1 查询操作
names = ['张三', '李四', '王五', '张三', '赵六']
print(names)
# 需求: 获取列表长度
print(len(names))
# 需求: 获取张三的个数
print(names.count('张三'))
# 需求: 判断张三是否在列表中
print('张三' in names)
# 需求: 获取张三的索引位置
print(names.index('张三'))
print('===========================')
# 4.2 列表的增删改
# 需求: 定义空列表
names = []
print(names)
# append()1次追加1个 需求: 往names列表中添加"张三"和"李四"
names.append('张三')
names.append('李四')
print(names)
# insert()插入 需求: 把'熊大'插入到第一个位置
names.insert(0, '熊大')
print(names)
# extend()1次追加多个 需求:往names列表中添加"王五"和"赵六"
names.extend(['王五', '赵六'])
print(names)

# 把最后1个元素修改为'老五'
names[-1] = '老五'
print(names)

# remove()删除指定元素
names.remove('老五')
print(names)
# pop()根据索引位置删除对应元素
names.pop(0)
print(names)
# clear()清空所有元素
names.clear()
print(names)