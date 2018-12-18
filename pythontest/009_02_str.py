#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述： 数据类型 --- String类型
# ====================================================



# 字符串处理相关
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 ''
# 自然字符串，通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是转义为换行。
# python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
# 字符串是不可变的。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。


# 输出需带转义的字符
print("hello world")
print('hello world')
print('''hello world''')
print("""hello world""")



print("---------------------------1-------------------------------")
print('I\'m ok.')
print('\\\t\\')
print(r'\\\t\\')



print("---------------------------2-------------------------------")
print('''hello huangxiaoming
    xuzheng
        huangbo
            wangbaoqiang
''')


print("---------------------------3-------------------------------")
# 字符串的一些相关运算：
str = "huangbo"
print(str)                  # 输出字符串
print(str[0:-1])            # 输出第一个到倒数第二个的所有字符
print(str[0])               # 输出字符串第一个字符
print(str[2:5])             # 输出从第三个开始到第五个的字符
print(str[2:])              # 输出从第三个开始的后的所有字符
print(str * 2)              # 输出字符串两次
print(str + "xuzheng")      # 连接字符串


print("---------------------------4-------------------------------")
# 转义
print("huang\nbo")
print(r"huang\nbo")
print(R"huang\nbo")



##
#
#  python的字符串：
a = "huangbo"
b = 'huangbo'
c = """huangbo"""
d = '''huangbo'''

print(a, b, c, d)
"""print(a, b, c, d)

    print(2)

"""

#
#
#