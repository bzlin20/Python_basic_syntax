"""
函数的使用方式
1、函数可以赋值给变量
2、函数可以作为函数的参数
3、函数可以作为函数的返回值

"""

items1 = list(map(lambda x:x **2 ,filter(lambda x:x%2,range(1,10))))
items2 =  [x**2 for x in range(1,10) if x %2]
print(items1)
print(items2)