"""
进程和线程

进程就是操作系统中执行的一个程序，操作系统以进程为单位分配存储空间

一个进程还可以拥有多个并发的执行线索，简单的说就是拥有多个可以获得CPU调度的执行单元，
这就是所谓的线程

Python既支持多进程又支持多线程，
因此使用Python实现并发编程主要有3种方式：多进程、多线程、多进程+多线程。
"""

"""
单进程  实例：
"""
from random import randint
from time import time,sleep

def download_task(filename):
	print('开始下载%s.....'%filename)
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s下载完成!耗费了%d秒'%(filename,time_to_download))

def main():
	start = time()
	download_task('python从入门到住院.pdf')
	download_task('Peking Hot.jpg')
	end=time()
	print('总共耗费了%.2f秒.'%(end-start))

if __name__ == '__main__':
	main()