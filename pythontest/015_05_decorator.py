#!/usr/bin/python3
# -*- coding:utf-8 -*-


# ====================================================
# 内容描述：  装饰器
# ====================================================

import urllib

"""
装饰器在Python中应用特别广泛，其特点是可以在具体函数执行之前或者之后做相关的操作
比如：执行前打印执行函数的相关信息，对函数的参数进行校验；
      执行后记录函数调用的相关流水日志等。
使用装饰器最大的好处是使得函数功能单一化，仅仅处理业务逻辑，而不附带其它功能。

装饰器可以把与业务逻辑无关的代码抽离出来，让代码保持干净清爽，而且装饰器还能被多个地方重复利用。
比如一个爬虫网页的函数，如果该 URL 曾经被爬过就直接从缓存中获取，否则爬下来之后加入到缓存，防止后续重复爬取。

深入理解装饰器：
https://mp.weixin.qq.com/s?__biz=MzAwOTQ4MzY1Nw==&mid=2247484032&idx=1&sn=7d62403e4b0566f103d103a9d0b05c96
"""
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page


# 使用装饰器改写：
def cache(func):
    saved = {}

    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page
    return wrapper

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()