"""
选择排序算法
"""

def select_sort(origin_intems,comp=lambda x,y :x<y):
	items=origin_intems[:]
	for i in range(len(items)-1):
		for j in range(i+1,len(items)):
			if comp(items[j],items[i]):
				tem = items[i]
				items[i]= items[j]
				items[j]= tem
	return items
array=[1,4,5,7,2,4,6,7,4]
print(select_sort(array))



"""
冒泡排序
"""

def bubble_sort(origin_items,comp = lambda x,y:x<y):
	items = origin_items[:]
	for i in range(len(items)-1):
		for j in range(len(items)-1-i):
			if comp(items[j],items[j+1]):
				tmp = items[j]
				items[j] = items[j+1]
				items[j+1] = tmp
	return items 

print(bubble_sort(array))
