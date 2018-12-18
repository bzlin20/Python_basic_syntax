#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： 高阶函数
# ====================================================

## 高阶函数的意义：除了可以接受函数作为参数外，还可以把函数作为结果值返回。


## 定义一个函数，求一个数值序列的和
def sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print(sum(1,2,3,4,5,6,7,8,9,10))


## 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
sum1 = lazy_sum(1,2,3,4,5,6,7,8,9,10)
print(type(sum1))
sum_result = sum1()
print(sum_result)