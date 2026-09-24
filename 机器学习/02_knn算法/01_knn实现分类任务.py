# 1.导包  此处导入knn分类模型
from sklearn.neighbors import KNeighborsClassifier

# 2.准备数据(此处我们模拟数据)
# 先模拟特征数据x
x_train = [[0],[1],[2],[3]]
x_text = [[4]]
# 在模拟标签数据y (假设1:垃圾邮件,0:正常邮件)
y_train = [0,0,0,1]     # 标签再这里是个一维
# TODO 3.需求: 预测x_test中的4属于垃圾邮件还是正常邮件
# todo 3.1 创建分类模型
knn_model = KNeighborsClassifier(n_neighbors=3)     # 平票时按类别标签升序取靠前的,即 0。
# todo 3.2 模型训练
knn_model.fit(x_train,y_train)
# todo 3.3 模型预测
y_pred = knn_model.predict(x_text)
# todo 3.4 打印预测结果
print(f'分类预测结果为:{y_pred}')      # 0

