#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re
# import base64
from scantool.tool import rule
#from multiprocessing import Process







def scan_title(title):
    titlerule = rule.title
    web_information = 0
    for key in titlerule.keys():
        req = re.search(key,title,re.I)
        if req:
            web_information = titlerule[key]
            break
        else:
            continue
    return web_information

def scan_head(header):
    headrule = rule.head
    web_information = 0
    for key in headrule.keys():
        if '&' in key:
            keys = re.split('&',key)
            if re.search(keys[0],header,re.I) and re.search(keys[1],response,re.I) :
                web_information = headrule[key]
                break
            else:
                continue
        else:
            req = re.search(key,header,re.I)
            if req:
                web_information = headrule[key]
                break
            else:
                continue
    return web_information




def scan_body(response):
    body = rule.body
    web_information = 0
    for key in body.keys():

        if '&' in key:
            keys = re.split('&',key)
            if re.search(keys[0],response,re.I) and re.search(keys[1],response,re.I):
                web_information = body[key]
                break
            else:
                continue
        else:
            req = re.search(key,response,re.I)
            if req:
                web_information = body[key]
                break
            else:
                continue
    return web_information


def main(url):
    if url.startswith('http://'):
        url = url
    else:
        url = 'http://' + url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1471.914 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding

    bresponse = BeautifulSoup(response.text, "lxml")
    title = bresponse.findAll('title')
    for a in title:
        title = a.get_text()
    head = response.headers
    response = response.text
    header = ''
    for key in head.keys():
        header = header + key + ':' + head[key]
    web_information = scan_title(title=title)
    if web_information == 0:
        web_information = scan_head(header=header)
        if web_information == 0:
            web_information = scan_body(response=response)
            if web_information == 0:
                information = '无能为力了'
            else:
                information = web_information
        else:
            information = web_information
    else:
        information = web_information
    result = {'~~~。。。。。~~~',information}
    return result




