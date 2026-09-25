# 注意以下导包会报错,错误内容中有获取数据的代码
# from sklearn.datasets import load_boston      # 此行注释

# 以下代码,从错误信息中复制# 代码经过修改,源网站进不去
# 三个坑（loss改名、数据源502、漏import）全解决，核心结论是：慢和报错都出在联网取数据，跟GPU和模型训练无关。
from sklearn.datasets import fetch_openml
boston = fetch_openml(name="boston", version=1, as_frame=True)
data = boston.data.values.astype(float)
target = boston.target.values.astype(float)
# 自己打印
print(f'特征:{data}')
print(f'标签:{target}')