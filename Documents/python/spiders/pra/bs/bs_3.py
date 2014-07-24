from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup("""Bob's <b>Bold</b> Barbeque Sauce now available in 
                        <b class="hickory">Hickory</b> and <b class="lime">Lime</a>""")
mysoup=soup.find('b',{"class":"lime"})
print mysoup

