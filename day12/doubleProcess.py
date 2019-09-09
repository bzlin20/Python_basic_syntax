"""
多进程实例

目前的多线程开发我们推荐使用threading模块，
该模块对多线程编程提供了更好的面向对象的封装
我们把刚才下载文件的例子用多线程的方式来实现一遍。

"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep
from threading import Thread


"""
def download_task(filename):
		print('启动下载进程,进程号[%d]'%getpid())
		print('开始下载%s......'%filename)
		time_to_download = randint(5,10)
		sleep(time_to_download)
		print('%s下载完成!耗费了%d秒'%(filename,time_to_download))

	def main1():
		start =time()
		p1 = Process(target=download_task,args=('python从入门到入院.pdf',))
		p1.start()
		p2 = Process(target=download_task,args=('Peking host.jpg',))
		p2.start()
		p1.join()
		p2.join()
		end =time()
		print('总共耗费%.2f秒'%(end - start))
"""


"""
我们通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，
后面的args是一个元组，它代表了传递给函数的参数。Process对象的start方法用来启动进程，
而join方法表示等待进程执行结束。运行上面的代码可以明显发现两个下载任务“同时”启动了，而且程序的执行时间将大大缩短，
不再是两个任务的时间总和。
"""


"""
threading模块的Thread类来创建线程，但是我们之前讲过一个非常重要的概念叫“继承”，
我们可以从已有的类创建新类，因此也可以通过继承Thread类的方式来创建自定义的线程类，
然后再创建线程对象并启动线程
"""

class DownLoadTask(Thread):
	def __init__(self,filename):
		Thread.__init__(self)    #必须加上这句话
		self._filename =filename
	def run(self):
		print('开始下载%s......'%self._filename)
		time_to_download = randint(5,10)
		sleep(time_to_download)
		print('%s下载完成!耗费了%d秒'%(self._filename,time_to_download))

def main():
	start = time()
	t1=DownLoadTask('python从入门到入院.pdf')
	t1.start()
	t2=DownLoadTask('那托闹海.txt')
	t2.start()
	t1.join()
	t2.join()
	end = time()
	print('总共耗费%.2f'%(end - start))

if __name__ == '__main__':
	main()








