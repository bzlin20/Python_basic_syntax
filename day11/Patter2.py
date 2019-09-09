"""
例子2：从一段文字中提取出国内手机号码

    提取 
"""
import re

def main():
	#创建正则表达式对象，使用了compile
	patern=re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
	sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，不是15600998765，也是110或119，王大锤的手机号才是15600998765。'''
    #查找所有匹配并保存到一个列表中
	mylist = re.findall(patern,sentence)
	print(mylist)

    #通过迭代器取出匹配对象并获得匹配内容
	for temp in patern.finditer(sentence):
		print(temp.group())

    #通过seach函数指定搜素位置找出所有匹配
	m = patern.search(sentence)
	while m:
		print(m.group())
		m=patern.search(sentence,m.end())

if __name__ == '__main__':
	main()


