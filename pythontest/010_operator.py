#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： 运算符相关
# ====================================================



## 算数运算符
print(5 + 3)    # 加法
print(5 - 3)    # 减法
print(5 * 3)    # 乘法
print(5 / 3)    # 除法，得到精确的数
print(5 // 3)   # 除法，得到整数值
print(5 % 3)    # 求余


print(5 ** 3)   # 乘方
print("aa" * 3) # 字符串重复拼接几次



print("---------------------------1-------------------------------")
## 逻辑运算符
print(True and True)
print(True and False)
print(True or True)
print(True and False)
print(not True)


print("---------------------------2-------------------------------")
## 比较运算符
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(3 <= 2)
print(3 != 2)
print(3 == 2)


print("---------------------------3-------------------------------")
## 赋值运算符
a = 9; print(a)
a += 2; print(a)
a -= 2; print(a)
a *= 2; print(a)
a /= 2; print(a)
a //= 2; print(a)     #  a = a // 2     a += 1 ===>  a = a + 1
a **= 3; print(a)



print("---------------------------4-------------------------------")
## 位运算符
a = 60
b = 13
print(bin(a))
print(bin(b))
# a = 0011 1100
# b = 0000 1101
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a >> 2)
print(a << 2)


print("---------------------------5-------------------------------")
## 成员运算符
list2 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(2 in list2)
print(2 not in list2)
print(5 in list2)
print(5 not in list2)



print("---------------------------6-------------------------------")
## 身份运算符 ： 身份运算符用于比较两个对象的存储单元
## id(a) 函数用于获取对象a的内存地址
print(2 is 2)
print(id(2) is id(2))   # Integer.cache(-128 - 127)
print(2 is not 3)
print([1, 2, 3] is [1, 2, 3])
print((1,2) is (1,2))
print(True is True)




print("---------------------------7-------------------------------")
## python中的三元表达式
test = False
result = test and 'Test is true' or 'Test is False'
print(result)

#  test          and   'Test is true'     or 'Test is False'
#  expression    ?      result1            :   result2

## 另外一种写法
a,b = 4,3
min = a if a < b else b
##   if (a < b) a else b
print(min)


## a = 3  b = 4
## temp = a, a = b, b = temp;