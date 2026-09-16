# 需求: 当前目录中的文件,图片,视频,音频等做个备份
"""
r: 读取文本文件 w: 覆盖写数据到文本文件 a: 追加写数据到文本文件
rb: 二进制读取文本文件 wb: 二进制覆盖写数据到文本文件 ab: 追加写数据到文本文件
"""
# 方式1: 原始方式 必须手动关闭,否则浪费资源
# 打开文件
f_in = open('hm.jpg', mode = 'rb')
f_out = open('hm[备份1].jpg', mode = 'wb')
# 读写文件
data = f_in.read()
f_out.write(data)
print('文件备份完成!')
# 关闭文件(节省资源)
f_in.close()
f_out.close()
print('=========================================')
# 方式2: with方式(推荐) 自动关闭,无需手动
with open('hm.jpg', mode = 'rb') as f_in:
    with open('hm[备份2].jpg', mode = 'wb') as f_out:
        data = f_in.read()
        f_out.write(data)
print('文件备份完成!')