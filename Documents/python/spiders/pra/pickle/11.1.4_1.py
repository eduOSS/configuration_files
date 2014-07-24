#references:https://docs.python.org/2/library/pickle.html
#
#!/usr/bin/python
#coding:utf8
import pickle
__author__ = ['leo.adams']

class Foo:
    attr = 'a class attr'

picklestring = pickle.dumps(Foo)
print picklestring
