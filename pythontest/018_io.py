#!/usr/bin/python3
# -*-coding:utf-8-*-

# ====================================================
# 内容描述： 文件读写相关
# ====================================================




"""
文件读写：
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000
"""

## 读文件：
f = open('c:/words.txt', 'r')
print(f, type(f))
print(f.read())
# print(f.readline())
# print(f.readlines())
f.close()


print("-------------------------------0-----------------------------------")


try:
    file = open('c:/words.txt')
    for line in file:
        print(line.strip())
except:
    print("File error!")
finally:
    file.close()

# 改写：
print("改写：")
with open('c:/words.txt') as file:
    for line in file:
        print(line.strip())

print("-------------------------------1-----------------------------------")
## 更换一种更为简便的写法：
with open('c:/words.txt', 'r') as f:
    print(f.read())




print("-------------------------------2-----------------------------------")
## 写文件
fw = open('c:/words_hello.txt', 'a', newline="\n")
fw.write('Hello, world!')
fw.close()




print("-------------------------------3-----------------------------------")
## 更换一种更为简便的写法：
with open('c:/words_hello.txt', 'a') as f:
    f.write('Hello, world!')


