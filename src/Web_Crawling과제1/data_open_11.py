import os
import urllib
import requests
import urlparse
import mylib
SERVICE='ArpltnInforInqireSvc'
OPERATION_NAME='getMinuDustFrcstDspth'
params1=os.path.join(SERVICE,OPERATION_NAME)
keyPath=os.path.join(os.getcwd(),'key.properties')
key=mylib.getKey(keyPath)
_d=dict()
_d['dataTerm']='month'
params2 = urllib.urlencode(_d)
params=params1+'?'+'serviceKey='+key['gokr']+'&'+params2
_url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
url=urlparse.urljoin(_url,params)
url = url.replace('\\','/')
data=requests.get(url).text
print data