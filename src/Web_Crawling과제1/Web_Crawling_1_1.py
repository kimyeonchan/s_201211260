import urllib, re
uaddress = urllib.urlopen('http://python.org/')
website = uaddress.read()
#p=re.compile('http://.+"')
regulaton = re.compile('href="(http://.*?)"')
result = regulaton.findall(website)
print "number of http url : ",len(result)
for i in range(0,len(result)):
    print i+1,result[i]