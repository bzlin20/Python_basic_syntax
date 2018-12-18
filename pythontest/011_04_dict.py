#!/usr/bin/python3
# -*-coding:utf-8-*-


# ====================================================
# 内容描述： 数据类型 --- Dict类型  -- 字典
# ====================================================


# Python 内置了 字典（dict），dict 全称dictionary
# 相当于 JAVA 中的 map，使用键-值（key-value）存储，具有极快的查找速度。


## 创建dict 注意：键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的。
dict1 = {"huangbo": 11, "xuzheng":22, "wangbaoqiang":33}
print(dict1)


## 修改字典
dict1["liutao"] = 40
print(dict1)
dict1["huangbo"] = 111
print(dict1)

dict1["huangbo"]


## 删除字典 通过 del 可以删除 dict （字典）中的某个元素，也能删除 dict （字典）
# 通过调用 clear() 方法可以清除字典中的所有元素
del dict1["huangbo"]
print(dict1)
dict1.clear()
print(dict1)
del dict1
# print(dict1)



## 其他使用注意
"""
1、dict （字典）是不允许一个键创建两次的，但是在创建 dict （字典）的时候如果出现了一个键值赋予了两次，会以最后一次赋予的值为准
2、dict （字典）键必须不可变，可是键可以用数字，字符串或元组充当，但是就是不能使用列表
3、dict  内部存放的顺序和 key 放入的顺序是没有任何关系
"""
tt = (1,2,3)
dict2 = {"huangbo":11, 22:33, tt: 44}
print(dict2)
print(dict2["huangbo"])
print(dict2[22])
print(dict2[tt])
# list2 = [2,3,4]
# dict2[list2] = 22
# print(dict2)

"""
和 list 比较，dict 有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢
    需要占用大量的内存，内存浪费多

而list相反：
    查找和插入的时间随着元素的增加而增加
    占用空间小，浪费内存很少
"""



print("----------------------999999----")
##  dict的其他操作
tt = (1,2,3)
dict2 = {"huangbo":11, 22:33, tt: 33}
print(len(dict2))
print(str(dict2))
print(type(dict2))
print(dict2.values())

print("222222222222222222222222222222222")


## 字典遍历
tt = (1,2,3)
dict2 = {"huangbo":11, 22:33, tt: 44}
#  [("huangbo",11), (22,33), (tt,44)]
for x, y in dict2.items():
    print(x, y)

for t in dict2.items():
    print(t[0], t[1])

for xx in dict2:
    print(xx, dict2[xx])


print("----------------------------------9---------------------------------")

# 字典合并
a = {'a': 1, 'b': 2}
b = {'c': 3}
new_dict = a.copy()
new_dict.update(b)
print(new_dict)




print("----------------------------------10  暂时不对---------------------------------")
# set1 = {("a", 1),("b",2),("c",3)}
# map1 = {"a":1, "b":2, "c":3}
# map2 = map(set1)
# print(map2)
