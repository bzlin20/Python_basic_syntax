"""
元组使用语法

Python 的元组与列表类似，不同之处在于元组的元素不能修改
里面的数据类型可以是多种
"""
def main():
	#定义元组
	t=('hh',34,True,'beijing')
	print(t)
	#获取元组中的元素
	print(t[0])
	print(t[3])
	#遍历元组中的值
	for member in t:
		print(member)
	t=('aa',20,True,'shanghai')
	print(t)
	person=list(t)
	#列表是可以修它的元素的
	person[0]='李小龙'
	person[1]=25
	print(person)

	#将列表转换成元组
	ff_list=['aa','bb','cc']
	ff_trule=tuple(ff_list)
	print(ff_trule)

if __name__=='__main__':
	main()

"""
元组在创建时间和占用的空间上面都优于列表
"""

