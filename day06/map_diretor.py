"""
使用字典
"""
def main():
	scores={'aa':95,'bb':89,'cc':79}
	#通过键可以获取字典中对应的值
	print(scores['aa'])
	print(scores['bb'])
	#对字典进行遍历（遍历其实是键再通过键取对应的值）
	for elem in scores:
		print("%s\t------>\t%d"%(elem,scores[elem]))
	#更新字典中的元素
	scores['aa']=0
	scores['bb']=1
	scores.update(dd=12,ee=49)
	print(scores)
	if 'ff' in scores:
		print(scores.get('ff'))  #get也可以获取键对应得默认值
	print(scores.get('ff',60))
	#删除字典中的元素
	print(scores.popitem())
	print(scores.pop('aa',95))
if __name__ == '__main__':
	main()

