#!/usr/bin/python3
# -*-coding:utf-8-*-


# ====================================================
# 内容描述： 流程控制--while
# ====================================================


# 求  1 - 10 之间的奇数和
sum = 0
count = 0
while count < 10:
    count += 1
    if count%2 == 0:
        # 只是当前这一次循环的循环体代码不执行
        continue
    sum += count
print(sum)



print("---------------------------1-----------------------------")
# 在 1 - 10 中  求  1- 7 的和
sum1 = 0
count1 = 0
while count1 < 10:
    count1 += 1
    if count1 == 8:
        # 整个while循环彻底不继续执行了。
        break
    sum1 += count1
print(sum1)



print("---------------------------2-----------------------------")
"""
在 Python 的 while 循环中，还可以使用 else 语句，while … else 在循环条件为 false 时执行 else 语句块
"""
##
count = 0
while count < 5:
   print (count)
   count = count + 1
else:
   print ("else", count)
