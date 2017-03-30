from urllib import urlopen
from bs4 import BeautifulSoup
uaddress = urlopen("http://python.org/").read()
tree = BeautifulSoup(uaddress, "lxml")
j = 1;
print 
for link in tree.find_all('a'):
    if link.get('href')[0] == 'h':
        print  j, link.get('href')
        j+=1