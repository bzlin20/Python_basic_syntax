"""
练习5：计算指定的年月日是这一年的第几天
"""

def is_leap_year(year):
	return year%4==0 and year%100!=0 or year%400==0


def which_day(year,month,date):
	days_of_month=[
	[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	][is_leap_year(year)]
	total=0
	for index in range(month-1):
		total +=days_of_month[index]
	return total+date

def main():
	print('一年过了',which_day(2019,7,12))
	print('一年过了',which_day(2019,7,13))
	print('一年过了',which_day(2019,7,14))
	print('一年过了',which_day(2019,1,1))
    



if __name__ == '__main__':
	main()

