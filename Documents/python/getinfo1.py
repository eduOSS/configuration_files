#! \usr\bin\python
# coding:utf-8
import re
import urllib
def getHtml(url): # get the html from the url given
    page = urllib.urlopen(url)
    html = page.read()
    print html
    return html

def getUrlList(res,url): # using the regular expression and the html to get the urls(or other info.) wanted     
    html = getHtml(url)
    infoGot = re.findall(res,html)
    return infoGot

def getInfoUrl(): # get the url from which I would get the further to get the metedata wanted
    for j in range(58,64):
        homeUrl = 'http://www.openinnovation.cn/opentools/function/'+str(j)
        homeRes = r'http://www\.openinnovation\.cn/node/9\w{3}'
        infoUrlList = getUrlList(homeRes,homeUrl) # get the final urllist
        print infoUrlList

getInfoUrl()
