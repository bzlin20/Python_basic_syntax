#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： 换行和缩进
# ====================================================


'''
python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
'''


if True:
    print("True")
else:
    print("False")


if True:
        print("True")
else:
        print("False")




'''
多行语句：
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠()来实现多行语句
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠()
'''

total_1 = 2 + 3 + 4
total_2 = 2 + \
          3 + \
          4
print(total_1)
print(total_2)


total_all = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
aa={'aa','bb',4}
print(aa)
print(total_all)