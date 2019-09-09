"""
正则表达式 替换

re.sub(pattern, repl, string, count=0, flags=0)

其中三个必选参数：pattern, repl, string

两个可选参数：count, flags

"""

import re

def main():
	sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
	purified = re.sub('fuck|shit|操|傻叉','*',sentence,flags=re.IGNORECASE)
	print(purified)

if __name__ == '__main__':
	main()