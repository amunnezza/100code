from  bs4 import BeautifulSoup
import os
os.chdir("./day45")
with open("website.html", encoding="utf8") as file:
    contents = file.read()
#print (contents)
soup = BeautifulSoup(contents, "html.parser")
#print (soup.title)
#print (soup.title.string)
#print (soup.prettify())
#print (soup.p)
#print (soup.li)
#print(soup.h3.text)
all_anchor_tag = soup.find_all(name="a")
for tag in all_anchor_tag:
    #print (tag.getText())
    print (tag.get("href"))