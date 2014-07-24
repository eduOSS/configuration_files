#!usr/bin/python
#coding:utf8
#http://jython.org/docs/library/collections.html
import itertools 
import collections
s = {('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)}
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
print d.items()

d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

print d.items()

s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1
print d[1].__class__
print d.items()

def constant_factory(value):
    return itertools.repeat(value).next
d = collections.defaultdict(constant_factory('<missing>'))
print d.items(),'---------------------------------------'
d.update(name='John', action='ran')
print d.items()
#'%(name)s %(action)s to %(object)s' % d
