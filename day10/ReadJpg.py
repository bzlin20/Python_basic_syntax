"""
读取二进制文件
"""
def main():
	try:
		with open('F:\\喜欢的壁纸\\大学.jpg','rb') as fs1:
			data= fs1.read()
			print(type(data))
	except FileNotFoundError as e:
		print('找不到指定文件')
	except IOError as e:
		print('读写文件时错误')
	print('程序执行结束')

if __name__ =='__main__':
	main()