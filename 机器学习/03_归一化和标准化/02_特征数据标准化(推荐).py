# 1.导包 此处导入标准化模型
from sklearn.preprocessing import StandardScaler

# 2.准备数据(模拟数据)
x_train = [
    [90,1,0,40],
    [60,4,15,45],
    [75,3,13,46]
]

# TODO 3.需求: 在模型训练特征进行规范化数据
# todo 3.1 创建标准化模型
model = StandardScaler()
# todo 3.2 规范化数据
new_x_train = model.fit_transform(x_train)
# todo 3.3 打印结果
print(new_x_train)

