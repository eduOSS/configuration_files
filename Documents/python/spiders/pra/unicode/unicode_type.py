#https://docs.python.org/2/howto/unicode.html
unicode('abcdef')
s = unicode('abcdef')
print type(s)
print unicode('abcdef' + chr(54))
print unicode('4')
print unicode('4').__class__
print int(unicode('4')).__class__
