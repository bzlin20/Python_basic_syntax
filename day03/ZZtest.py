"""
水仙花数
"""

counts=1
while True:
	number=int(input('请输入一个整数: '))
	if len(str(number))!=3:
		print('%d不是3位数,请输入三位数'%(number))
	else:
		a=number%10
		b=number//10%10
		c=number//100

		if(a**3+b**3+c**3)==number:
			print('%d是水仙花数'%number)
			break
		else:
			print('输入的%d不是水仙花数,请再输入一次'%number)
	counts+=1
	if(counts>3):
		print('输入次数结束!')
		break

