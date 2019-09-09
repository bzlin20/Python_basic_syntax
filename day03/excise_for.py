"""
打印三角形  range(a,b,c) a-起始  b-终止 c-步长
"""
counts=int(input('请输入图形的层数：'))
for i in range(counts):
	for j in range(i+1):
		print('*',end='')
	print()

for i in range(counts):
	for j in range(counts-i):
		print(' ',end='')
	for k in range(i+1):
		print('*',end='')
	print()

for i in range(counts):
	for j in range(counts-i):
		print(' ',end='')
	for k in range(2*i+1):
		print('*',end='')
	print()

