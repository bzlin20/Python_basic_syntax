"""
练习1：华式温度转摄氏温度
"""
temps=float(input("情输入华式温度："))
ctemp=(temps-32)/1.8
print('%.0f华式度=%.0f摄氏度'%(temps,ctemp))

"""
输入圆的半径计算计算周长和面积
"""
import math
radius =float(input('请输入圆的半径：'))
p=2*math.pi*radius
area=math.pi*(radius*radius)
print('周长:%.2f'%p)
print('面积:%.2f'%area)

"""
输入年份判断是不是闰年。
"""
year=int(input('请输入年份：'))
is_run=((year%4==0 and year%100!=0) or year%400==0)
print(is_run)