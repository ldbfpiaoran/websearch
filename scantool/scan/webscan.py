#-*- coding: UTF-8 -*-
import re
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
import pymysql
from scantool.scan import appscan
from scantool.tool import config,search_ipaddrs,search_domain


localconfig = config.Config

def get_host_informathion(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1471.914 Safari/537.36'}
    response = requests.get(url=url, headers=headers,timeout=2,verify=False)
    response.encoding = response.apparent_encoding
    bresponse = BeautifulSoup(response.text, "lxml")
    title = bresponse.findAll('title')
    header = ''
    for i in title:
        title = i.get_text()
    head = response.headers
    body = response.text
    for key in head.keys():  # 将 header集合
        header = header + key + ':' + head[key]+'\n'
    return [title,header,body]


def insert_data(ip,port,title,header,domain,appname='',ipaddrs='无'):
    try:
        conn = pymysql.connect(host=localconfig.host, user=localconfig.username, passwd=localconfig.passwd, db='mysql',
                           charset=localconfig.charset, port=localconfig.port)
        conn = conn.cursor()
        conn.execute('use chttp')
        savesql = 'insert into `ip_data` (`ip`,`port`,`title`,`header`,`appname`,`ipaddrs`,`domain`) values (%s,%s,%s,%s,%s,%s,%s)'
        conn.execute(savesql,(ip,port,title,header,appname,ipaddrs,domain))
        conn.connection.commit()
    except Exception as e:
            print(e)





def scan_main(ip):
    i = ip.split(':')[1]
    url = 'http://'+ip
    try:
        urldata = get_host_informathion(url=url)
        if urldata != '':
            try:
                title = urldata[0]
                header = urldata[1]
                body = urldata[2]
            except Exception as e:
                print(e)

            information = appscan.main_scan(title=title, header=header, body=body)  #加入app类型  未编写
            if urldata :
                ipaddrs = search_ipaddrs.ip_scan(ip)
                domain = str(search_domain.search_domain(ip))
                insert_data(ip=ip,port=i,title=title,header=header,appname=information,ipaddrs=ipaddrs,domain=domain)
            else:
                print('search false')
        else:
            print('urldata is false')
    except Exception as e:
        print(e)







