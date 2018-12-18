#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： 关键字和保留字
# ====================================================


# 引入模块keyword取别名叫做k，第一次接触python就把它理解成跟java中的导包一样的概念就行。
import keyword as k

# 列出python的所有关键字和保留字
print(k.kwlist)


# 结果：
# ['False', 'None', 'True', 'and', 'as',
# 'assert', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return',
# 'try', 'while', 'with', 'yield']
