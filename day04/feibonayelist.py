"""
斐波那锲数列
"""
a=1
b=0
for i in range(10):
	a+=b
	b+=a
	print(a,b,end=',')