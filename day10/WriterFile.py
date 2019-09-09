"""
使用open函数时指定好文件名并将文件模式设置为'w'即可。
注意如果需要对文件内容进行追加式写入，应该将模式设置为'a'。
"""

from math import sqrt

def is_prime(n):
	"""
    判断素数的函数
	"""
	assert n>0
	for fa in range(2,int(sqrt(n))+1):
		if n% fa ==0:
			return False
	return True if n!=1 else False
def main():
	filenames=('a.txt','b.txt','c.txt')
	fs_list =[]
	try:
		for filename in filenames:
			fs_list.append(open(filename,'w',encoding='utf-8'))
		for number in range(1,10000):
			if is_prime(number):
				if number<100:
					fs_list[0].write(str(number)+'\n')
				elif number<1000:
					fs_list[1].write(str(number)+'\n')
				else:
					fs_list[2].write(str(number)+'\n')
	except IOError as ex:
		print(ex)
		print('写文件时发生错误')
	finally:
		for fs in fs_list:
			fs.close()
	print('操作完成')

if __name__ == '__main__':
	main()

