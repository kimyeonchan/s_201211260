import os
import mylib
import urlparse
import re
import requests
keyPath=os.path.join(os.getcwd(),'key.properties')
key=mylib.getKey(keyPath)
KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardSubwayStatsNew'
START_INDEX=1
END_INDEX=1000
USE_DT = str(20160501)
_maxIter=2
_iter=0
while _iter<_maxIter:
    params=os.path.join(KEY,TYPE,SERVICE,str(START_INDEX),str(END_INDEX),USE_DT)
    params = params.replace('\\','/')
    _url='http://openAPI.seoul.go.kr:8088/'
    url=urlparse.urljoin(_url,params)
    data=requests.get(url).text
    print data