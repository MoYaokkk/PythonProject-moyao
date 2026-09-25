import numpy as np

# 设置随机种子为固定值
np.random.seed(1)

# 生成随机数组
arr1 = np.random.randint(0,10,size=5)
print('第一次生成',arr1)

print('==============================')
# 设置随机种子为固定值
np.random.seed(2)

# 生成随机数组
arr1 = np.random.randint(0,10,size=5)
print('第二次生成',arr1)

