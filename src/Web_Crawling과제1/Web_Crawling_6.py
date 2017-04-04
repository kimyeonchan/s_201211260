from urllib import urlopen
from bs4 import BeautifulSoup
uaddress = urlopen("http://www.kbreport.com/main").read()
tree = BeautifulSoup(uaddress, "lxml")
print 
for link in tree.find_all('div',{'class':'team-rank-box'}):
    for link2 in link.find_all('tr'):
        children = link2.findChildren()
        for i in range(0,len(children)):
            if(children[i].get('href') is None):
                print children[i].text.strip(),
        print ""        