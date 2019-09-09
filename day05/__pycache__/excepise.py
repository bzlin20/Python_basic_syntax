"""
实现计算求最大公约数和最小公倍数的函数。
"""
def gcd(x,y):
	(x,y)=(y,x) if x>y else (x,y)
	for factor in range(x,0,-1):
		if x%factor ==0 and y%factor==0:
			return factor

def lcm(x,y):
	return x*y //gcd(x,y)

"""
回文数
"""

def hwnumber(n):
	result=n[::-1]
	return result==n

s=input('请输入一个数:')
print(hwnumber(s))
