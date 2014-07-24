#! usr/bin/python
# coding:utf-8

from __future__ import division

def jia(x,y):
	return x+y
def jian(x,y):
	return x-y
def cheng(x,y):
	return x*y
def chu(x,y):
	return x/y

operator={'+':jia,'-':jian,'*':cheng,'/':chu}
def f(x,o,y):
	print operator.get(o)(x,y)
f(5,'/',2)

def f1(x,o,y):
	print {'+':jia,'-':jian,'*':cheng,'/':chu}.get(o)(x,y)
f1(7,'/',3)

def f2(x,o,y):
	print {'+':lambda x,y:x+y,'-':lambda x,y:x-y ,'*':lambda x,y:x*y ,'/':lambda x,y:x/y }.get(o)(x,y)
f2(9,'/',5)

