"""
Python中有关变量作用域的问题
"""

def foo():
	b='hello'
	def bar():
		c=True
		print(a)
		print(b)
		print(c)
	bar()
if __name =='__main__':  #全局变量
	a=100  
	foo()

#我们可以使用global关键字来指示foo函数中的变量a来自于全局作用域
