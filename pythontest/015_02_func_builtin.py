#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： python3中的一些常用内置函数的使用操作
# ====================================================



## zip压缩
a = ["a", "b", "c"]
b = [1, 2, 3]
zip_result = zip(a, b)
print(type(zip_result))
for z in zip_result:
    print(z)
print(dict(zip(a, b)))
print(list(zip(a, b)))



print("----------------------------------1--------------------------------------")
## enumerate函数
s = "ten_story"
s = enumerate(s)
for x in s:
    print(x)
print(list(enumerate(s)))
print(dict(enumerate(s)))




print("----------------------------------2--------------------------------------")
## list拷贝
list1 = list(range(1,11))
list2 = list1[:]
print(list1)
print(list2)




print("----------------------------------3--------------------------------------")
## list合并
L = [[1, 2], [4, 5, 6], [7]]
sum_L = sum(L, [])
print(sum_L)



print("----------------------------------4--------------------------------------")
## list反转
L = list(range(0, 10))
print(L)
r_L = L[::-1]   # 逆序L
print(r_L)




print("----------------------------------5--------------------------------------")
## map函数
map1 = map(lambda x: x * x, [1,3,5,7,9])
print(map1)
print(type(map1))
for m in map1:
    print(m)




print("----------------------------------6--------------------------------------")
## reduce函数
from functools import reduce
## 三个参数：函数，计算序列，初始值
result = reduce(lambda a,b: a+b, [1,2,3,4,5,6,7,8,9,10])
result1 = reduce(lambda a,b: a+b, [1,2,3,4,5,6,7,8,9,10], 100)
print(result, result1)

## 有意思的代码  需求：[1,2,3,4,5,6,7,8,9] 变成一个  123456789的一个 number数值
def f(a, b):
    return a*10 + b
result2 = reduce(f, [1,2,3,4,5,6,7,8,9])
print(result2)

## 利用reduce函数把一个数字字符串转变成数值，即实现 int("92739172")的功能
def str2intseq(str1, f):
    return reduce(f, [int(x) for x in str1])
print(str2intseq("123456789111", f))




print("----------------------------------7--------------------------------------")
## filter 函数
list_filter = [1,2,3,4,5,6,7,8]
filter_result_list = filter(lambda x : x % 2 == 0, list_filter)
print(filter_result_list)
for x in filter_result_list:
    print(x)



print("----------------------------------8--------------------------------------")
##  any 函数
numbers = [1, 10, 1000, 10000]
if any(number < 10 for number in numbers):
    print('Have number<10')



print("----------------------------------9--------------------------------------")
##  sorted 函数
list11 = [7,-3,5,1,-6,9,-4,2,8]
print(sorted(list11))
print(sorted(list11, reverse=True))
print(sorted(list11, key=lambda s:abs(s)))

##  按照成绩排序
name_age_tuple_list = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(name_age_tuple_list, key=lambda s:s[1]))