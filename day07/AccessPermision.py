"""
对象访问可见性问题
"""

#如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
class Test:
	def __init__(self,foo):
		self.__foo=foo
	def __bar(self):
		print(self.__foo)
		print('__bar')

def main():
	test=Test('Hello')
	test.__bar()
	print(test.__foo)

if __name__=='__main__':
	main()

"""
在实际开发中尽量少用私有属性和方法
"""

