"""
如何实现两个进程间的通信。我们启动两个进程，
一个输出Ping，一个输出Pong，
两个进程输出的Ping和Pong加起来一共10个
"""

#错误代码
from multiprocessing import Process
from time import sleep

counter=0

def sub_task(string):
	global counter
	while counter<10:
		print(string,end='',flush=True)
		counter+=1
		sleep(0.01)

"""
当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，
每个子进程有自己独立的内存空间，
这也就意味着两个子进程中各有一个counter变量
"""

def main():
	Process(target=sub_task,args=('Ping',)).start()
	Process(target=sub_task,args=('Pong',)).start()



if __name__ == '__main__':
	main()
