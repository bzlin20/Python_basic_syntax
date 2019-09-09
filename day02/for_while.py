"""
一种是for-in循环，一种是while循环。
"""
#1、求和
sum=0
for x in range(1,100):
	sum+=x
print(sum)


#如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random

answere=random.randint(1,100)
count=0
while True:
	count+=1
	number= 1 #int(input('请输入一个整数: '))
	if number>answere:
		print('小一点')
	elif number<answere:
		print('大一点')
	else:
		print('恭喜你猜对了！')
		break
	print('你总共猜了%d次'%count)
	if count>=5:
		print('你的智商余额明显不足')
		break

"""
9x9乘法表
"""
for i in range(1,10):
	for j in range(1,i+1):
		print('%d * %d = %d'%(i,j,i*j),end='\t')
	print()






