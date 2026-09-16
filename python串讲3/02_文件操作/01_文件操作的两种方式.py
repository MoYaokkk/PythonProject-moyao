# 需求: 把当前目录下的test.txt读取到程序中,打印内容
# 方式1: 原始方式 必须手动关闭,否则浪费资源
# 打开文件
f = open('test.txt', mode = 'r', encoding = 'utf-8')
# 读文件
data = f.read()
print(data)
# 关闭文件(节省资源)
f.close()
print('=========================================')
# 方式2: with方式(推荐) 自动关闭,无需手动
with open('test.txt', mode = 'r', encoding = 'utf-8') as f:
    # 读文件
    data = f.read()
    print(data)