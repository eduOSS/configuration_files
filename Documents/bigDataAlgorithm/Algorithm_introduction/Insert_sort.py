#references:
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


a = [3,5,7,2,4,7,3,9,23,43,12,34,23]

for i in range(1,len(a)):
    j = i - 1
    key = a[i]
    while j >= 0 and key < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key

print a
