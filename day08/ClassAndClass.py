"""
类与类之间的关系 is-a has-a use-a
继承和多态  java一样
这个代码是继承
"""
class Person(object):
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
		print('%s正在愉快的玩耍'%sefl._name)

class Student(Person):
	def __init__(self,name,age,grade):
		super().__init__(name,age)  #调用父类
		self._grade=grade
	def study(self,course):
		print('%s的%s正在学习'%(self._grade,self._name))
def main():
	stu=Student('aa',13,'初一')
	stu.study('数学')
	stu.play()   #子类调用父类的方法



if __name__=='__main__':
	main()

	

	
