from urllib import urlopen
from bs4 import BeautifulSoup
uaddress = urlopen("http://www.ieee.org/conferences_events/conferences/search/index.html").read()
tree = BeautifulSoup(uaddress, "lxml")
j = 1;
print 
for link in tree.find_all('div',{'class':'content-r-full'}):
    for link2 in link.find_all('table',{'class':'nogrid-nopad'}):
        for link3 in link2.find_all('tr'):
            for link4 in link3.find_all('p'):
                children = link4.findChildren()
                if(len(children)==1):
                    print link4.text
                    print "----------"