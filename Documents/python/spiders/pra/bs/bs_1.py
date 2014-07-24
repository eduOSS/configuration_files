from bs4 import BeautifulSoup
import re

doc = ['<html><head><title>Page title</title></head>',
	'<body><p id="firstpara" align="center">this is paragraph<b>one</b>.',
	'<p id="secondpara" align="blah">this is paragraph<b>two</b>.',
	'</html>']
soup = BeautifulSoup(''.join(doc))

print soup.prettify()
print soup.contents[0].name
head = soup.contents[0].contents[0]
print head.next
print head.contents[0]#the same as the formal one 
print head.nextSibling.name
print head.nextSibling.contents[1]
print head.nextSibling.contents[0].nextSibling#the same as the formal one
titleTag = soup.html.head.title
print titleTag.string
print len(soup('title')) 
print soup.findAll('p',align='blah')
print soup.find('p',align='blah')
print soup('p',align='center')[0]['align'],'^^^^^^^^'
print soup('p',align='center')[0]
print soup.find('p',align=re.compile('^c'))['id']
print soup.find('head').title.string
print soup('p')[1].b.string,'*****'
print titleTag,'here is the titleTag'
titleTag['id']='theTitle'
titleTag.contents[0].replaceWith("New Title")
print soup.html.head
print soup.prettify()
print soup.p.extract()
soup.p.replaceWith(soup.b)
print soup.prettify()
soup.body.insert(0,"this page used to have")
soup.body.insert(2,"&lt:p&gt: tags!")
print soup.body
print soup.body.contents[0]
print soup.body.contents[1]
print soup.body.contents[2]
