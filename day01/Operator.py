"""
[] [:]	下标，切片
**	指数
~ + -	按位取反, 正负号
* / % //	乘，除，模，整除
+ -	加，减
>> <<	右移，左移
&	按位与
^ |	按位异或，按位或
<= < > >=	小于等于，小于，大于，大于等于
== !=	等于，不等于
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
= += -= *= /= %= //= **= &= |= ^= >>= <<=	（复合）赋值运算符
"""

a=5
b=10
a +=b   #a=a+b
print('a= ',a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)