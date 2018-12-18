#!/usr/bin/python3
# -*-coding:utf-8-*-


# ====================================================
# 内容描述： 测试python中的异常语法结构
# ====================================================


# from urllib.request import urlopen
from urllib.request import URLError as ue

try:
    print(2 + 2)
    # 2 / 0
    raise ue("XXX")

except TypeError as e:
    print("出现异常", e)
except ZeroDivisionError as ee:
    print("非法除数", ee)
except ue as urle:
    print("非法URL", urle)
else:
    print("没有出现异常")
finally:
    print("程序执行完毕")