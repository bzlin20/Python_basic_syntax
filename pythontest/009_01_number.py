#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： 数据类型 --- Number类型
# ====================================================


"""
Python3 支持
        int整型
        float浮点型  没有double， 只有float
        bool布尔型
        complex复数
四种数值类型。

在Python 3里，只有一种整数类型 int，表示为长整型，可以存储任何长度的数值，没有 python2 中的 Long
在Python 3里，只有一种浮点数类型 float，表示为浮点型，没有 python2 中的 Double

像大多数语言一样，数值类型的赋值和计算都是很直观的
内置的 type(a) 函数可以用来查询变量a所指的对象类型
内置的 isinstance(a, b) 函数可以用来判断指定变量a是否是指定类型b
"""


# 查看某个变量是什么类型  type() 函数
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))


# 比对某个变量是否是对应的参数类型   isinstance() 函数
aa = 111
print(type(aa))
print(isinstance(aa, int))




print("---------------------------1-------------------------------")
class A:
    pass

## 注意：这表示 B类型是 A 类型的子类， 等同于Java中的 B extends A
class B(A):
    pass

print(isinstance(A(), A))      # returns True
print(type(A()) == A)          # returns True
print(isinstance(B(), A))      # returns True
print(type(B()) == A)          # returns False




print("---------------------------2-------------------------------")
#  ord函数返回一个字符串的ASCII编码值
print(ord("A"))
print(ord("a"))
print(ord("1"))
#  chr函数返回一个数值的ASCII字符
print(chr(65))
print(chr(97))
print(chr(49))




print("---------------------------3-------------------------------")
"""
int(x [,base ])	            将x转换为一个整数
float(x)	                将x转换到一个浮点数
complex(real [,imag ])	    创建一个复数
str(x)	                    将对象 x 转换为字符串
repr(x)	                    将对象 x 转换为表达式字符串
eval(str)	                用来计算在字符串中的有效 Python 表达式,并返回一个对象
tuple(s)	                将序列 s 转换为一个元组
list(s)	                    将序列 s 转换为一个列表
chr(x)	                    将一个整数转换为一个字符
ord(x)	                    将一个字符转换为它的ASCII整数值
hex(x)	                    将一个整数转换为一个十六进制字符串
oct(x)	                    将一个整数转换为一个八进制字符串
"""
print(int("17"));
print(int("17", 10));
print(int("17", 16));
print(float(3))
print(float("3.33"))
print(complex(3, 4))
print(complex("3+4j"), type(complex("3+4j")), sep="\t")
print(str(23))




print("-------------------------------4-----------------------------------")
list1 = [1,2,3]
print(repr(list1), type(repr(list1)), sep="\t")
print(eval("(4+3)*2 - 4"))
print(tuple([1, 2, 3, 4, 5]))
print(list((1, 2, 3, 4, 5)))
print(hex(2333333))
print(oct(24))
# .....
