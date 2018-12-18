#!/usr/bin/python3
# -*-coding:utf-8-*-

# ====================================================
# 内容描述： 列表生成式
# ====================================================


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000
"""


list = []
for x in range(1,10):
    list.append(x)
print(list)



print("---------------------------1-----------------------------")
# 以上操作太繁琐。如此操作
list2 = [x for x in range(1, 10)]
print(list2)



print("---------------------------2-----------------------------")
# 需求1： 求1-10的每个数的平方组成的列表
list3 = [ x*x for x in range(1,10)]
print(list3)



print("---------------------------3-----------------------------")
# 需求2： 求1-100中能被5除尽的数的平方组成的列表
list4 = [x*x for x in range(1, 101) if x%5 == 0]
print(list4)



print("---------------------------4-----------------------------")
# 需求3： 两层循环嵌套
list5 = [m + n for m in 'ABC' for n in 'XYZ']
print(list5)



print("---------------------------5-----------------------------")
# 需求4： 列举出C盘下的所有文件
import os
list6 = [d for d in os.listdir('c:/')]
print(list6)



print("---------------------------6-----------------------------")
# 需求5:  {'x': 'A', 'y': 'B', 'z': 'C' } 变成 ['y=B', 'x=A', 'z=C']
dict = {'x': 'A', 'y': 'B', 'z': 'C'}
list7 = [k + '=' + v for k, v in dict.items()]
print(list7)



print("---------------------------7-----------------------------")
# 需求6： L = ['Hello', 'World', 18, 'Apple', None] 转小写
L = ['Hello', 'World', 18, 'Apple', None]
list8 = [ x.lower() for x in L if isinstance(x, str)]
print(list8)



print("---------------------------8-----------------------------")
print([(x, y, x*y) for x in (0,1,2,3) for y in (0,1,2,3) if x < y])



print("---------------------------9-----------------------------")
## 根据value值进行删选
from random import randint
d = {x: randint(50, 100) for x in range(1, 21)}
res = {s: c for s, c in d.items() if c >= 90}
print(res)







list11 = set(range(1,11));
# list22 = [1,4,9,16,25,36]
result = []
for xx in list11:
    result.append(xx * xx)
print(result)

##      表达式      迭代          守卫条件
print([xx * xx for xx in list11 if xx % 2 == 0])