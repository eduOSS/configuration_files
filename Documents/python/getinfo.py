#! \usr\bin\python
# coding:utf-8
import re
import urllib
def getHtml(url): # get the html from the url given
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getUrlList(res,url): # using the regular expression and the html to get the urls(or other info.) wanted     
    html = getHtml(url)
    infoGot = re.findall(res,html)
    return infoGot

def getInfo(html):
    labelRes = r'label">([\u4e00-\u9fa5]*):&nbsp;'
    itemsRes = r'even">([\u4e00-\u9fa5\w*])((</a>)?</div></div></div>|target="_blank">)'
    label = re.findall(labelRes,html)
    items = re.findall(itemsRes,html)
    print label
    #lait = zip(label,items)
    #for ilait in lait:
    #    print ilait

def getInfoUrl(): # get the url from which I would get the further to get the metedata wanted
    for j in range(58,64):
        homeUrl = 'http://www.openinnovation.cn/opentools/function/'+str(j)
        homeRes = r'http://www\.openinnovation\.cn/node/9\w{3}'	
        infoUrlList = getUrlList(homeRes,homeUrl) # get the final urllist
        for i in infoUrlList:
            infoHtml = getHtml(i) # get the information page
            getInfo(infoHtml)


getInfoUrl()
