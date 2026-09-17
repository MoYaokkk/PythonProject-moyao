# 1.导包
import numpy as np

# 2.创建numpy数组
# 此处咱们用最简单的方式创建: 把列表转换为numpy数组
my_list = [[10, 20], [30, 40]]
print(my_list, type(my_list))
my_array = np.array(my_list)
print(my_array, type(my_array))
print("==================================")
# 3.数组的基础运算
# 下面的操作都是返回新的数组
print(my_array + 2)
print(my_array - 2)
print(my_array * 2)
print(my_array / 2)
print(np.max(my_array))
print(np.min(my_array))
print(np.mean(my_array))
# 还有很多计算的api,大家自己研究