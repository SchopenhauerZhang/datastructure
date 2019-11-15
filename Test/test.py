#!/usr/bin/python3
# @File: test.py
# --coding:utf-8--
# @Author:Schopenhauerzhang@icloud.com(Schopenhauerzhang@gmail.com)
# @license:Copyright Schopenhauerzhang@icloud.com All rights Reserved.  
# @Time: 2019-08-05 18:03
import time
import gc
from queue import Queue


# this is my name
# of courese
# you are my some thing else
def get():
	i = 100
	
	while (i > 0):
		i -= 1
		print('get')
		post()


def post():
	i = 1000
	while (i > 0):
		i -= 1
	time.sleep(1)
	print('post')


def queue():
	que = Queue(2046)
	print(que.maxsize)


