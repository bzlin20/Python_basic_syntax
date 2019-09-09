"""
字符串和数据数据结构
"""
def main():
	str1='hello world'
	print(len(str1))
	
	print(str1.capitalize())
	
	print(str1.upper())
	
	print(str1.find('or'))

	print(str1.startswith('He')) #检查字符串是否以指定字符串开头

	print(str1.endswith('!'))#结尾

	str2 = 'abc123456'  #下标从0开始
	print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
	print(str2[2:5])  # c12
	print(str2[2:])  # c123456
	print(str2[2::2])  # c246
	print(str2[::-1])  # 654321cba
	print(str2[-3:-1])  # 45

if __name__ == '__main__':
	main()


