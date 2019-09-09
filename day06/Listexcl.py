"""
使用列表
"""

def ddllist():
	list1=[1,3,5,6,1]
	print(list1)
	list2=['hello']*5
	print(len(list2))

	print(list1[0])  #取值
	print(list1[4])

	print(list1[-1])
	print(list1[-3])
	list1[2]=300   #赋值
	print(list1)
	#添加元素
	list1.append(200)
	list1.insert(1,400)
	list1+=[10000,20000]
	print(list1)
	print(len(list1))
	#删除元素
	list1.remove(3)
	del list1[0]
	print(list1)
	#清空列表元素
	list1.clear()
	print(list1)

def forlist():
	fr=['g','adad','agegega','geqefd']
	fr+=['erqerq','eqefrgs','etyqeet']
	#循环标量列表元素
	for f in fr:
		print(f.title,end=' ')  #title单词以大写开头，其余都是小写
	print()
	#列表切片
	f2=fr[1:4]
	print(f2)

	f3=fr[:]  #复制列表
	f4=fr[-3:-1]

	f5=fr[::-1] #反转

def sortlist():
	list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
	list2 =sorted(list1) # sorted函数返回列表排序后的拷贝不会修改传入的列表
	list3=sorted(list1,reverse=True) #反转
	list4=sorted(list1,key=len)  #安装字符串的长度进行排序
	print(list1)
	print(list2)
	print(list3)
	print(list4)

#列表生成式
def createlist():
	f=[x for x in range(1,10)]
	print(f)
	f=[x+y for x in 'ABCDE' for y in '1234567']
	print(f)




if __name__ == '__main__':
	ddllist()
	forlist()
	sortlist()
	createlist()











