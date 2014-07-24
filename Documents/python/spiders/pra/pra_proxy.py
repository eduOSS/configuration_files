import urllib2
proxy_support = urllib2.ProxyHandler({'http':'http://91.213.30.151'})
opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)
content = urllib2.urlopen('http://www.ftchinese.com/story/001056809').read()
print content
