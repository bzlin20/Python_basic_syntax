#!/usr/bin/python3
# -*-coding:utf-8-*-


# ====================================================
# 内容描述： 模块相关
# ====================================================


'''

在 python 用 import 或者 from...import... 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *


java中的 类 .class  和   python 中的 模块 .py   等同
所有的这些 .py 的文件也会被包给组织起来。

      包       模块          函数     别名
from urllib.request import urlopen as uo
import urillib.request

'''

# 正确的写法
import os
import sys
# 不推荐的写法
import sys,os


# 正确的写法
from subprocess import Popen, PIPE
from urllib.request import *


# 正确的写法
from urllib.request import urlopen


# 给引入的模块或者函数取别名
# import numpy as np
from urllib.request import urlopen as uo
uo("http://www.baidu.com")




"""
常用内置模块
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319347182373b696e637cc04430b8ee2d548ca1b36d000
"""


"""
安装第三方模块
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432002680493d1babda364904ca0a6e28374498d59a7000
"""






print("---------------------------1-----------------------------")

for x in "huangbo":
    print(x)

ddd = {'x': 'A', 'y': 'B', 'z': 'C' }
keys = ddd.keys()
for xx in keys:
    print(xx, ddd.get(xx))