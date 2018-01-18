from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"ml")

nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
