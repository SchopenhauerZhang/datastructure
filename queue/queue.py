#!/usr/bin/python3
# @File: queue.py.py
# --coding:utf-8--
# @Author:Schopenhauerzhang@icloud.com(Schopenhauerzhang@gmail.com)
# @license:Copyright Schopenhauerzhang@icloud.com All rights Reserved.  
# @Time: 2019-08-05 17:41

class Queue(object):
	def __init__(self,max_size = 1024):
		self._len = 0
		self._queue = []
		self._max_size = 1024
		
	@property
	def len(self):
		return self._len
	
	@len.setter
	def len(self, length):
		self._len += length
		
	@len.deleter
	def len(self):
		self._len = 0
		return True
	
	@property
	def queue(self):
		return self._queue.pop()
	
	@queue.setter
	def queue(self, map):
		self.queue.append(map)
		return True
	
	@property
	def max_size(self):
		return self._max_size
	
	@max_size.deleter
	def max_size(self):
		try:
			self._max_size = 1024
		except Exception:
			exit("delete fail , check the env or something for the error")
			
		return True

