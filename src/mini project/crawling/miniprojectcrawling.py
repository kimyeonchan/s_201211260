import mysql.connector
import os
import urllib
from mysql.connector import errorcode
from urllib import urlopen
from bs4 import BeautifulSoup
def check(child):
    if(child ==""):
        return 0;
    else:
        child = int(child)
        return child
    
def check2(child):
    if(child ==""):
        return '0';
    else:
        return child
try:
    cnx = mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='mysql')
    cursor = cnx.cursor()
    query = 'create database test2'
    cursor.execute(query)
    query = 'use test2'
    cursor.execute(query)
    query= 'create table parking(parking_code varchar(20) primary key, parking_name varchar(40), addr varchar(100), tel varchar(15), capacity int, cur_parking int, begin_time varchar(50), end_time varchar(50), rates int, rates_time int, add_rate int, add_rate_time int, day_maximum int );'
    cursor.execute(query)
    startindex = 1
    endindex = 999
    i =0;
    while i < 2:  
        url  = 'http://openapi.seoul.go.kr:8088/7462416a50706f7135376b724c4641/xml/GetParkInfo/'+str(startindex)+'/'+str(endindex)
        uResponse = urllib.urlopen(url)
        _html = uResponse.read()
        tree = BeautifulSoup(_html, "lxml")
        for link in tree.findAll("row"):
            children = link.findChildren()
            add_parking = ("INSERT INTO parking (parking_code, parking_name, addr, tel, capacity, cur_parking, begin_time, end_time, rates, rates_time, add_rate, add_rate_time, day_maximum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            child7 = check2(children[7].get_text())
            child30 = check(children[30].text)
            child31 = check(children[31].text)
            child32 = check(children[32].text)
            child33 = check(children[33].text)
            child38 = check(children[38].text)
            data_parking = [children[0].get_text(),
                            children[1].get_text(),
                            children[2].get_text(),
                            child7,
                            int(children[10].text), 
                            int(children[11].text), 
                            children[17].get_text(),
                            children[18].get_text(),
                            child30, child31, child32, child33, child38]
            if (int(children[10].text)>=5):
                cursor.execute(add_parking, data_parking)
        print i
        i+=1;
        startindex +=999;
        endindex += 999;
        print "success"
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    else:
        print(err)
else:
    cnx.commit()
    cursor.close()
    cnx.close()