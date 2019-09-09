import requests
from time import time
from threading import Thread

"""
下面我们还是通过requests来实现一个访问网络数据接口并从中获取美女图片
下载链接然后下载美女图片到本地的例子程序
"""


#继承Thread类创建自定义的线程类
class DownLoadHanler(Thread):

	def __init__(self,url):
		super().__init__()
		self.url = url

	def run(self):
		filename = self.url[self.url.rfind('/')+1:]
		resp = requests.get(self.url)
		with open('C:\\Users\\Administrator\\Desktop'+filename,'wb') as f:
			f.write(resp.content)

def main():
	# 通过requests模块的get函数获取网络资源
	resp = requests.get(
		'https://image.baidu.com/')
	#将服务器返回的json格式数据解析为字典
	data_model = resp.json()
	for mm_dict in data_model['newslist']:
		url = mm_dict['picUrl']
		#通过多线程的方式实现图片下载
		DownLoadHanler(url).start()

if __name__ == '__main__':
	main()

