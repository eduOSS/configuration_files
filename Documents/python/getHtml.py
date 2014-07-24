#! /usr/bin/python
# coding = utf-8
import urllib

def gethtml():
    page = urllib.urlopen('http://www.openinnovation.cn/opentools/function/58')
    html = page.read()
    print html

gethtml()
