"""
Python中的集合跟数学上的集合是一致的，
不允许有重复元素，而且可以进行交集、并集、差集等运算。
"""
def main():
	set1={1,2,3,4,5,6,7,8}
	print(set1)
	print('length= ',len(set1))
	set2 = set(range(1,10))
	print(set2)
	set1.add(4)
	set1.add(10)
	set2.update([11,12])
	print(set1)
	print(set2)
	set2.discard(5)  #删除元素
	if 4 in set2:
		set2.remove(4) #remove的元素如果不存在会引发keyerror
	print(set2)
	#遍历集合
	for elem in set2:
		print(elem**2,end=' ')
	print()
	#将元组转换成集合
	set3=set((1,2,3,4,5,6,7,8,9))
	print(set3.pop())
	print(set3)
	





























