#!/usr/bin/python3
# -*-coding:utf-8-*-


# ====================================================
# 内容描述： 流程控制 -- for相关
# 迭代相关 for循环可以遍历任何序列的项目，如一个列表或者一个字符串
# ====================================================



# range函数
print(range(10))
print(range(3, 10))
print(range(3, 10, 2))

for a in range(10):
    print(a)
print("------------------------------")
for a in range(3, 10):
    print(a)
print("------------------------------")
for a in range(3, 10, 2):
    print(a)
print("------------------------------")
for a in range(10, 0, -2):
    print(a)




print("---------------------------1-----------------------------")
aa = ["huangbo", "xuzheng", "wangbaoqiang", 44]
print("------------------------------")
# for 遍历列表：第一种，使用in进行遍历
for a in aa:
    print(a)
print("------------------------------")
# for 遍历列表：第二种，使用下标进行遍历
for i in range(len(aa)):
    print(aa[i])




print("---------------------------2-----------------------------")
# 遍历字符串
for letter in "huangbo":
    print(letter)




print("---------------------------3-----------------------------")
"""
有 while … else 语句，当然也有 for … else 语句啦，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
"""
for num in range(10, 20):           # 迭代 10 到 20 之间的数字
   for i in range(2, num):          # 根据因子迭代
      if num % i == 0:              # 确定是否能除尽，能除尽，则表示是合数
         print('%d 是一个合数' %num)
         break                      # 跳出当前循环
   else:                            # 循环的 else 部分
      print('%d 是一个质数' %num)


## for ... else ... 的用途
A = [[1, 2, 3, 4, 2, 66],
     [1, 0, 2, 32, -9, 3, 4, 1, 2],
     [7, 8, 9, 3, 2, 2],
     [2, -3, 3, 1, 1, 3, 21]]
# 上面这个矩阵， 求出全是正数的行的编号...

for a in A:
    ok = True
    for x in a:
        if x <= 0:  # 一旦发现存在负数，则记录ok变量并退出本层循环
            ok = False
            break
    if ok:
        print('第', A.index(a), '行全是正数')

print("for ... else ...")
for a in A:
    for x in a:
        if x <= 0:
            break
    else:  # 能执行到这一句说明上面的循环完整执行了，没有break
        print('第', A.index(a), '行全是正数')





print("---------------------------4-----------------------------")
##  条件语句和循环语句综合实例

# 打印99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
        print("{0}*{1}={2}\t".format(i, j, i*j), end="")
    print()



# list1 = [1,2,3,4,5]
# str11 = "-".join(list1)
# print(str11)

print("a\nb\nc")



print("---------------------------5-----------------------------")
## 一句话打印99乘法表
print ('\n'.join([' '.join(['%s*%s=%-3s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))

##  每一行是由多个表达式组成的    3*2=6,  第n行就有n个这样的表达式
##  每一行的多个这样的表达式，按照 “ ” 进行拼接  ，  最终整个99乘法表
## 有多少行，就可以组成一个 具有多少个元素的 一个 列表
##  再把这n个元素， 使用"\n" 拼接起来， 最终得到一个很庞大的字符串。




print("---------------------------6-----------------------------")
## 判断是否是 闰年
year = int(input("请输入一个年份: "))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0} 是闰年' .format(year))
else:
    print('{0} 不是闰年' .format(year))



print("---------------------------7-----------------------------")
# 带索引位置的循环遍历
colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print(i, 'mapping', color)


print("---------------------------8-----------------------------")
# 强大的for循环
student = [['Tom', (98, 96, 100)], ['Jack', (98, 96, 100)]]
for name, (first, second, third) in student:
    print(name, first, second, third)