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
END_INDEX=5
USE_DT = str(20160501)
_maxIter=10
_iter=0
while _iter<_maxIter:
    params=os.path.join(KEY,TYPE,SERVICE,str(START_INDEX),str(END_INDEX),USE_DT)
    params = params.replace('\\','/')
    _url='http://openAPI.seoul.go.kr:8088/'
    url=urlparse.urljoin(_url,params)
    data=requests.get(url).text
    p1=re.compile('<SUB_STA_NM>(.+?)</SUB_STA_NM>')
    p2=re.compile('<RIDE_PASGR_NUM>(.+?)</RIDE_PASGR_NUM>')
    p3=re.compile('<ALIGHT_PASGR_NUM>(.+?)</ALIGHT_PASGR_NUM>')
    res1=p1.findall(data)
    res2=p2.findall(data)
    res3=p3.findall(data)
    for i in range(len(res1)):
        print '역 이름 : ' , res1[i] , ',  승차수 : ' , res2[i], ',  하차 수 :' , res3[i]
    START_INDEX+=5
    END_INDEX+=5
    _iter+=1