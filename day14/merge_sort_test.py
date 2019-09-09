"""
归并排序
"""
def merge_sort(items,comp = lambda x, y :x <y):
	"""归并排序 """
	if len(items)<2:
		return items[:]
	mid = len(items)/2
	left = merge_sort(items[:mid],comp)
	right = merge_sort(items[mid:],comp)
	merge(left,right,comp)

def merge(items1,items2,comp):
	"""合并"""
	items= []
	index1,index2=0,0
	while index1<len(items1) and index2<len(item2):
		if comp(items1[index1],items2[index2]):
			items.append(items1[index1])
			index1+=1
		else:
			items1.append(items2[index2])
			index2+=1
	items +=items1[index1:]
	items +=items2[index2:]
	return items


lists=[1,2,36,4351,4514,35,4,51,4,541534]
print(merge_sort(lists))