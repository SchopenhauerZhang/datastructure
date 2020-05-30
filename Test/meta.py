#!/usr/bin/env python3

class my_meta(type):
	def __init__(self,name,bases,dicts):
		print('init instance')
	def __new__(cls,name,bases,dicts):
		dicts['info'] = lambda self:print('Djx.')
		res = type.__new__(cls,name,bases,dicts)
		res.company = 'maizi'
		return res
class custom(metaclass = my_meta):
	pass

		



if __name__ == '__main__':
	cus = custom()
	cus.info()
