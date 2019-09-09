"""
练习1：定义一个类描述数字时钟
"""

from time import sleep
import datetime

class Clock(object):
	def __init__(self,hour=0,minute=0,second=0):
		self._hour=hour
		self._minute=minute
		self._second=second
	def run(self):
		self._second+=1
		if self._second==60:
			self._second=0
			self._minute+=1
			if self._minute==60:
				self._minute=0
				self._hour+=1
				if self._hour==24:
					self._hour=0
	def show(self):
		return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)
def main():
	hour=int(datetime.datetime.now().strftime('%H'))
	minter=int(datetime.datetime.now().strftime('%M'))
	second=int(datetime.datetime.now().strftime('%S'))
	clock = Clock(hour,minter,second)
	while True:
		print(clock.show())
		sleep(1)
		clock.run()

if __name__=='__main__':
	main()

