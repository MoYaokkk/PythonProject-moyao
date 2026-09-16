"""模块"""
"""
标识符命名规则:
    组成: 只能有字母,数字,下划线,汉字
    注意: 不能以数字开头,不能是关键字,严格区分大小写,不建议用汉字
模块: 符合标识符命名规则的py文件,就是python模块
模块好处: 模块能够被导入重复使用
如何自定义模块? 符合标识符命名规则的py文件,里面定义的函数就能被远程调用
"""
# 导包方式1: import方式
import my_module1
my_module1.show()

import python_package.my_moudle2    #用python包的方式
python_package.my_moudle2.show2()

# 导包方式2: from方式
from my_module1 import show
show()

from python_package.my_moudle2 import show2     #python包的方式
show2()
