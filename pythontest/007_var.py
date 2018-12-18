#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： 变量定义相关
# ====================================================


# 定义变量，不用声明类型， python是一种动态语言。具有类型推断功能， 能自动识别出aa变量是字符串类型
aa = "huangbo"
aa = 11


# 自动识别 bb变量 为  数值类型
bb = 11


# python的优良特性，可以在一行声明多个变量
cc, dd = "xuzheng", 22
print(cc, dd)


## int a,b, c;
## a = b = c = 12

# 实现cc和dd变量的交换
cc, dd = dd, cc
print(cc, dd)


# 连环声明
ee = ff = gg = hh = 12


# 声明list
list = [1,2,3,4,"huangbo",True]
print(list)
print(type(list))


# 声明元组
tuple=(1,2,3,4,"huangbo")
print(tuple)
print(type(tuple))


# 声明集合
set = {"a",1,"b",2,"c",3}
print(set)
print(type(set))



# 声明字典
dict = {"a":1,"b":2,"c":3}
print(dict)
print(type(dict))



print("-----------------------------------------------------------------------")
p = 'huangbo', True, 30
print(type(p))
name = p[0]
gender = p[1]
age = p[2]

name1, gender1, age1 = p
print(name, gender, age)
print(name1, gender1, age1)

num_list = [100, 19, 20, 98]
first, *left_num_list, last = num_list
print(first, left_num_list, last)
print("==================================================")
aa=[1,2,3,4,"aa",True,1.45,'q']
print("list集合",aa,end="\n")
bb=(1,2,3,4,5,"bb",True)
print("truple",bb)
cc={1,5,"erqew","31"}
print("set",cc)
dd={"ef":1,"rf":2}
print("字典",dd)
