#!/usr/bin/python3
# -*-coding:utf-8-*-


# ====================================================
# 内容描述： 函数操作相关
# ====================================================


print(ord("A"))         # 把一个字符转换成unicode编码
print(chr(65))          # 把数字转换成一个字符
print(abs(-1))          # 求绝对值
print(type(3+4j))       # 求参数变量的类型



print("---------------------------1-----------------------------")
a = 1
b = str(a)
print(a, b)
print(type(a), type(b))
c = int(b)
print(type(b), type(c))
d = float(c)
print(type(c), type(d))



print("---------------------------2-----------------------------")
e = "True"
f = bool(e)
print(type(e), type(f))
print(type(3 > 2))
print(bool(""), type(bool("")))
print(bool(" "), type(bool(" ")))
print(bool(0), type(bool(0)))
print(bool(3), type(bool(3)))



print("---------------------------3-----------------------------")
"""
自定义函数，基本有以下规则步骤：
    1、函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()
    2、任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数
    3、函数的第一行语句可以选择性地使用文档字符串（用于存放函数说明）
    4、函数内容以冒号起始，并且缩进
    5、return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None。
"""

"""
定义一个函数：

def 定义一个函数，给定一个函数名 sum
声明两个参数 num1 和 num2
函数的第一行语句进行函数说明：两数之和
最终 return 语句结束函数，并返回两数之和
"""
# 定义函数
def sum(num1,num2):
    "两数之和"
    return num1 + num2

# 调用函数
print(sum(5,6))



print("---------------------------4-----------------------------")
"""
函数参数：

传参分为两种：
1、可变类型， 传递的是引用
2、不可变类型， 传递的是值的拷贝

解释：b = 1,创建了一个整形对象 1 ，变量 b 指向了这个对象，然后通过函数 chagne_number 时，
按传值的方式复制了变量 b ，传递的只是 b 的值的一个copy，并没有影响到 b 的本身。
"""
## 有意思的测试：
def chagne_number(b):
    b = 1000
b = 1
chagne_number(b)
print(b)


print("---------------------------5-----------------------------")
array = [1,2,3,4,5]
def change_array(array):
    array[0] = "huangbo"
some = change_array(array)
print(array)
print(some)

array1 = [1,2,3,4,5]
def change_array1(array):
    array[0] = "huangbo"
    return array
some = change_array1(array1)
print(array1)
print(some)




print("---------------------------6-----------------------------")
"""
函数默认参数
有时候，我们自定义的函数中，如果调用的时候没有设置参数，需要给个默认值，
这时候就需要用到默认值参数了。
"""
def print_user_info(name, sex, age=18):
    print(name, sex, age)

## 位置参数
print_user_info("huangbo", "F", 20)
print_user_info("huangbo", "F")
## 关键字参数
print_user_info(age=30,  name="huangbo", sex="M")
"""
需要注意的是：
1、只有在形参表末尾的那些参数可以有默认参数值
2、默认参数的值是不可变的对象，比如None、True、False、数字或字符串，
当默认参数是可变对象时，默认值在其他地方被修改后你将会遇到各种麻烦。
这些修改会影响到下次调用这个函数时的默认值。
"""





print("---------------------------7-----------------------------")
"""
变长参数

有时我们在设计函数接口的时候，可会需要可变长的参数。也就是说，我们事先无法确定传入的参数个数。
Python 提供了一种元组的方式来接受没有直接定义的参数。这种方式在参数前边加星号 * 。
如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。

在如下函数定义中：hobby就是一个元组
"""
def print_user_info2(name, age, sex = '男', *hobby):
    print(name, sex, age)
    print(hobby)
print_user_info2("huangbo", "F", 20, 20)
print_user_info2("huangbo", "F", 20, "a", "b", "c", 1, 2, 33.33)






print("---------------------------8-----------------------------")
"""
匿名函数：
python 使用 lambda 来创建匿名函数，也就是不再使用 def 语句这样标准的形式定义一个函数。

匿名函数主要有以下特点：
1、lambda 只是一个表达式，函数体比 def 简单很多。
2、lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
3、lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

注意：尽管 lambda 表达式允许你定义简单函数，但是它的使用是有限制的。 
你只能指定单个表达式，它的值就是最后的返回值。
也就是说不能包含其他的语言特性了， 包括多个语句、条件表达式、迭代以及异常处理等等。
"""
## 例子：
sum = lambda num1, num2 : num1 + num2
s = sum(1, 2)
print(s)


## 有趣测试    lambda的参数是运行时绑定的
num2 = 100
sum1 = lambda num1: num1 + num2
num2 = 10000
sum2 = lambda num1: num1 + num2
print(sum1(1))
print(sum2(1))





print("---------------------------9-----------------------------")

"""
闭包：https://zhuanlan.zhihu.com/p/21346046

Closures are functions that refer to independent (free) variables (variables that are used locally, but defined in an enclosing scope). In other words, the function defined in the closure 'remembers' the environment in which it was created.
"""