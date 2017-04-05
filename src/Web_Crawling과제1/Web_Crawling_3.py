from urllib import urlopen
from bs4 import BeautifulSoup
from urllib import FancyURLopener
class MyOpener(FancyURLopener):
    version = 'My new User-Agent'
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
myopener = MyOpener()
page = myopener.open('http://www.google.com/search?q=python')
tree = BeautifulSoup(page,"lxml")
j = 1;
for link in tree.find_all('a'):
    if(link.get('href') is not None):
        if link.get('href')[0] == 'h':
            print j,link.get('href')
            j = j+1;