from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
print type(tag)
print tag.name
tag.name = 'leo'
print tag.name
print tag.string
print tag.attrs
print tag['class']
print soup

print '--------------------------------------------------'
tag['class']='verygood'
tag['id']='verybad'
tag['leo']='verybadleo'
print tag['class']
print tag['id']
print tag['leo']
print soup
