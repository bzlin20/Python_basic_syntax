"""
果一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”，
对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态
下面的例子演示了100个线程向同一个银行账户转账（转入1元钱）的场景
"""
from time import sleep
from threading import Thread,Lock

"""
class Account(object):
	def __init__(self):
		self._balance = 0
	def deposit(self,money):
		#计算存款后的余额
		new_balance = self._balance+money  #临界资源
		sleep(0.01)
		#修改账户余额
		self._balance = new_balance
	@property
	def balance(self):
		return self._balance
"""

"""
。在这种情况下，“锁”就可以派上用场了。我们可以通过“锁”来保护“临界资源”，
只有获得“锁”的线程才能访问“临界资源”，而其他没有得到“锁”的线程只能被阻塞起来，
直到获得“锁”的线程释放了“锁”，
其他线程才有机会获得“锁”，进而访问被保护的“临界资源”
"""


class Account(object):
	def __init__(self):
		self._balance = 0
		self._lock = Lock()

	def deposit(self,money):
		#先获取锁才能执行后续的代码
		self._lock.acquire()
		try:
			new_balance = self._balance+money
			sleep(0.01)
			self._balance = new_balance
		finally:
			# 在finally中执行释放锁的操作保证正常异常锁都能释放
			self._lock.release()
	@property
	def balance(self):
		return self._balance
	
	

class AddMoneyThread(Thread):
	def __init__(self,account,money):
		super().__init__()
		self._account = account
		self._money = money
	def run(self):
		self._account.deposit(self._money)

def main():
	account = Account()
	threads= []
	for _ in range(100):
		t = AddMoneyThread(account,1)
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	print('账户余额为:￥%d元'%account.balance)

if __name__ == '__main__':
	main()




