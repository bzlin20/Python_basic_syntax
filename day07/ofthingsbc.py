"""
面向对象编程基础
"""
#定义类
class Student(object):
	def __init__(self,name,age):  #__init__是一个特殊方法用于在创建对象时进行初始化操作
		self.name=name  # 通过这个方法我们可以为学生对象绑定name和age两个属性
		self.age=age
	def study(self,course_name):
		print('%s正在学习%s'%(self.name,course_name))
	def watch_movie(self):
		if self.age<18:
			print('%s只能观看《熊出没》.' % self.name)
		else:
			 print('%s正在观看大电影.' % self.name)

#创建对象
def main():
	#创建学生对象并指定姓名和年龄
	stu1=Student('小智',45)
	#调用方法
	stu1.study('python')

if __name__=='__main__':
	main()
	xiaoming=Student('小明',19)
	xiaoming.study('数学')
	xiaoming.watch_movie()





