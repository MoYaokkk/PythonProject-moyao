# 导包
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# TODO 准备数据
# 1.准备数据(特征2列和标签1列)
x,y = make_blobs(n_samples=1000,
                 n_features=2,
                 centers=[[0,0],[-1,-1],[1,1],[2,2]],
                 cluster_std=[0.4,0.2,0.2,0.3]
                 )
print(x.shape)  # (1000, 2)
print(y.shape)  # (1000,)

# 2.提前绘制散点图看看数据分布
plt.scatter(x[:,0],x[:,1])
plt.show()
# TODO 使用Kmeans模型
# 3.创建Kmeans模型
model = KMeans(n_clusters=2)
y_pred = model.fit_predict(x)
# 4.按照预测值通过颜色划分类别:绘制散点图看看数据分布
plt.scatter(x[:,0],x[:,1],c=y_pred)
plt.show()