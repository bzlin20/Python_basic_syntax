"""
英制单位英寸和公制单位厘米互换
"""

value=float(input('请输入长度:'))
unit=input('请输入单位：')
if unit=='in' or unit=='英寸':
	 print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
	 print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
	print('请输入有效的单位')

"""
掷骰子决定做什么事情
"""
from random import randint
face=randint(1,6)
if face==1:
	result='唱歌'
elif face==2:
	result='跳个舞'
elif face==3:
	result='学狗叫'
elif face==4:
	result='做俯卧撑'
elif face==5:
	result='打人'
else:
	result='去西藏'
print(result)

