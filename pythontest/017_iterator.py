#!/usr/bin/python3
# -*-coding:utf-8-*-


# ====================================================
# 内容描述： 迭代器相关
# ====================================================


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000

"""



"""
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为                     

可迭代对象：Iterable。


可以使用isinstance()判断一个对象是否是Iterable对象：
"""
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))



print("-------------------------------1-----------------------------------")



"""
而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
直到最后抛出StopIteration错误表示无法继续返回下一个值了。

可以被next()函数调用并不断返回下一个值的对象称为          

迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：
"""
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))




print("-------------------------------2-----------------------------------")

"""
生成器都是Iterator对象，
但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：
"""
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))






print("-------------------------------3-----------------------------------")
"""
总结：


凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的
"""