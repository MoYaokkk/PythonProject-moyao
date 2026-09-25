# 导包 此处导入线性回归API
from sklearn.linear_model import LinearRegression

# 1.准备数据 x:特征(身高) y:标签
x_train = [
    [160],[166],[172],[174],[180]
]
y_train = [
    56.3,60.6,65.1,68.5,75
]
x_test = [[176]]

# 2.准备模型
model = LinearRegression()
# 3.模型训练
# TODO 训练线性回归目的是什么? 找线性规律(最优的k和b)
model.fit(x_train,y_train)
# 训练后打印k和b
print(f'最优的斜率:k是{model.coef_}')         # [0.92942177]
print(f'最优的偏置:b是{model.intercept_}')        # -93.27346938775517
print('==========================================')

# 4.模型预测
# TODO 方式1: 手动套入公式
y_pred1 = model.coef_[0] * x_test[0][0] + model.intercept_
print(f'手动计算结果:{y_pred1}')
# TODO 方式2: 使用模型自带的预测方法
y_pred2 = model.predict(x_test)
print(f'模型预测结果:{y_pred2}')