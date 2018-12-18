#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： 数据类型相关
# ====================================================


"""
Python3 中有六个标准的数据类型：

    Number（数字）  数值类型    整形 和  浮点型  double
    String（字符串）   char
    List（列表）    list
    Tuple（元组）    tuple
    Sets（集合）     set
    Dictionary（字典）   dict

    type(a) 求出a变量的类型
    isinstance(a,b) 判断变量a是否是b类型， a变量的类型可以是b变量的子类的类型

    isinstance和type的区别:
        type()不会认为子类是一种父类类型,
        isinstance()会认为子类是一种父类类型
"""


# 声明数值类型
num_1 = 1
num_2 = 3.1415926
num_3 = True
num_4 = 3 + 4j
print(num_1, num_2, num_3, num_4)


print("---------------------------1-------------------------------")
# 声明字符串类型
str_1 = "huangbo"
str_2 = 'a'
print(str_1, str_2)
print(type(str_1), type(str_2))
print(isinstance(str_1, str))


print("---------------------------2-------------------------------")
# 声明list
list = [1, 2, 3, 4, "huangbo", True, 3 + 4j]
print(list)
print(type(list))


print("---------------------------3-------------------------------")
# 声明元组
tuple=(1, 2, 3, 4, "huangbo", 3 + 4j)
print(tuple)
print(type(tuple))


print("---------------------------4-------------------------------")
# 声明集合
set = {"a", 1, "b", 2, "c", 3, 3, 3, 3}
print(set)
print(type(set))


print("---------------------------5-------------------------------")
# 声明字典
dict = {"a" : 1, "b" : 2, "c" : 3}
print(dict)
print(type(dict))