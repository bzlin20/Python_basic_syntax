#要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）
"""
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）
"""

def main():
	f=None
	try:
		f=open('C:/Users/Administrator/Desktop/aa.txt','r',encoding='UTF-8')
		print(f.read())
	except FileNotFoundError:
		print('无法打开指定文件！')
	except LookupError:
		print('指定了未知的编码！')
	except UnicodeDecodeError:
		print('读取文件时解码错误!')
	finally:
		if f:
			f.close
if __name__=='__main__':
	main()

