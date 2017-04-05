# -*- coding:utf-8 -*-
import urllib
import re
from bs4 import BeautifulSoup
keyword='비오는'
f = urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
mydata = f.read()
tree = BeautifulSoup(mydata,"lxml")
table = tree.find_all('table',{'summary':'트랙 리스트'})
tbody = table[0].find_all('tbody')
name = tbody[0].find_all('td',{'class':'name'})
for i in range(1,len(name)):
    children = name[i].findChildren()
    print children[4].get('title')