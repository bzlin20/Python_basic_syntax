"""
                                    __slots__魔法
我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定
。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
"""
class Person(object):
	#限定person对象只能绑定name,age和gender属性
	__slots__ = ('_name','_age','_gender')

	def __init__(self,name,age):
		self._name=name
		self._age=age
	@property
	def name(self):
		return self._name
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self,age):
		self._age=age
	def play(self):
		if self._age<=16:
			print('%s正在玩飞行棋' % self._name)
		else:
			print('%s正在玩斗地主' % self._name)
"""
静态类和方法
    就是在方法前加上@staticmethod
    调用的时候直接用类名.方法名
"""
	@staticmethod
	def is_valid(a,b,c):
		return a+b>c and b+c>a and a+c>b
"""
定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象
"""
	@classmethod
	def testclass(cls):
		return aa

def main():
	persons=Person('王大锤',22)
	persons.play()
#	persons._gender = '男'  不能赋值
	Persons.is_valid(1,2,3)   #直接调用静态方法

if __name__ == '__main__':
	main()






	

	
