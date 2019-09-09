"""
定义一个函数，求阶乘
"""

def factorial(num):
	result=1
	for n in range(1,num+1):
		result*=n
	return result
m=int(input('m= '))
n=int(input('n= '))
print(factorial(m)//factorial(n)//factorial(m-n))

"""
函数的参数
"""
from random import randint
def roll_dice(n=2):
	total =0
	for _ in range(n):
		total += randint(1,6)
	return total 
def  add(a=0.b=0,c=0):
	return a+b+c
#如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
#摇3颗色子
print(roll_dice(3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))

"""
可变参数  
在参数名前面的*表示args是一个可变参数
即在调用add函数时可以传入0个或多个参数
"""
def adds(*args):
	total=0
	for val in args:
		total +=val
	return total


