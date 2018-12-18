#!/usr/bin/python3
# -*-coding:utf-8-*-


# ====================================================
# 内容描述： 数据类型 --- Set类型
# 集合的两大真正有用的操作;
    #   1、去重
    #   2、求交集，并集，差集
# ====================================================


# python 的 set 和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素。set 和 dict 类似，但是 set 不存储 value 值的。

# 集合操作相关

## 创建set    创建一个 set，需要提供一个 list 作为输入集合
set1 = set([4,2,3])
print(set1)
set2 = set([4,2,3,3,3,3,3])
print(set2)


"""
## 通过观察结果发现：
1、tuple (元组) 使用小括号
2、list (列表) 使用方括号
3、dict (字典) 使用的是大括号
4、dict 也是无序的，只不过 dict 保存的是 key-value 键值对值，而 set 可以理解为只保存 key 值。
"""

print("---------------------------1-----------------------------")
## 添加元素
set3 = set(["huangbo", 22, 33, 44.55])
print(set3)
set3.add("huangbo")
print(set3)
set3.add(44)
print(set3)



print("---------------------------2-----------------------------")
## set移除元素
set3 = set(["huangbo", 22, 33, 44.55])
set3.remove(22)
print(set3)



print("---------------------------3-----------------------------")
## set的高级使用
# 因为 set 是一个无序不重复元素集，因此，两个 set 可以做数学意义上的 union(并集), intersection(交集), difference(差集) 等操作
set11 = set(["hello","huangbo", 2, 3 ,4])
set22 = set(["hi", "huangbo", 3, 4, 5])
# 求交集
print(set11 & set22)
# 求并集
print(set11 | set22)
# 求差集
print(set11 - set22)
print(set22 - set11)