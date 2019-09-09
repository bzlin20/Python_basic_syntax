"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random

def generate_code(code_len):
	"""
   生成指定长度的验证码
	"""
	all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_pos=len(all_chars)-1
	code =''
	for _ in range(code_len):
		index=random.randint(0,last_pos)
		code+=all_chars[index]
	return code
if __name__=='__main__':
	n=int(input('请输入验证码的个数: '))
	print(generate_code(n))