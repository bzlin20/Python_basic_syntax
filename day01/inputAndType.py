"""
使用input函数输入 
使用int()进行类型转换
用占位符格式化输出的字符串
"""
a=int(input('a= '))
b=int(input('b= '))
print('%d +%d = %d'%(a,b,a+b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

"""
使用type()检查变量类型
"""
c=100
d=12.345
e='hello world'
f=True
g=1+5j
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
