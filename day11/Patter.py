"""
正则表达式

.	匹配任意字符	
\w	匹配字母/数字/下划线	
但不能匹配b#t
\s	匹配空白字符（包括\r、\n、\t等
\d	匹配数字	\d\d	
\b	匹配单词的边界	
^	匹配字符串的开始
+	匹配1次或多次	
?	匹配0次或1次	
$	匹配字符串的结束	
\S	匹配非空白字符	
\D	匹配非数字	
*	匹配0次或多次	\w*	
{M,N}	匹配至少M次至多N次	\w{3,6}			
{M,N}?	重复M到N次，但尽可能少重复		
Python对正则表达式的支持
Python提供了re模块来支持正则表达式相关操作，下面是re模块中的核心函数。

函数	说明
match(pattern, string, flags=0)	用正则表达式匹配字符串 成功返回匹配对象 否则返回None
split(pattern, string, maxsplit=0, flags=0)	用正则表达式指定的模式分隔符拆分字符串 返回列表
sub(pattern, repl, string, count=0, flags=0)	用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数
fullmatch(pattern, string, flags=0)	match函数的完全匹配（从字符串开头到结尾）版本
findall(pattern, string, flags=0)	查找字符串所有与正则表达式匹配的模式 返回字符串的列表
finditer(pattern, string, flags=0)	查找字符串所有与正则表达式匹配的模式 返回一个迭代器
purge()	清除隐式编译的正则表达式的缓存
re.I / re.IGNORECASE	忽略大小写匹配标记
re.M / re.MULTILINE	多行匹配标记
"""



"""
例子1：验证输入用户名和qq号是否有效并给出对应得提示信息
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，
QQ号是5~12的数字且首位不能为0
"""
import re

def main():
	i=0
	while i<5:
		if i == 4:
			print('您输入的次数已达上限，请下次再试！')
			break
		username = input('请输入用户名: ')
		m1=re.match(r'^\w{6,20}$',username)
		if not m1:
			print('请输入正确的用户名！')
			i+=1
			continue
		qq = input('请输入QQ号: ')
		m2=re.match(r'^[1-9][0-9]{4,11}$',qq)
		if not m2:
			print('请输入正确的QQ号！')
			i+=1
			continue
		if m1 and m2:
			print('你输入的信息是有效的')
			break
		


if __name__=='__main__':
	main()
