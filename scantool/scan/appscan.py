#-*- coding: UTF-8 -*-
import re
from scantool.scan import rule


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



def scan_head(header,body):
    headrule = rule.head
    # headrule = router_rule.head
    web_information = 0
    for key in headrule.keys():
        #print(key)
        if '&' in key:
            keys = re.split('&',key)
            if re.search(keys[0],header,re.I) and re.search(keys[1],body,re.I) :
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





def scan_body(body):
    bodyrule = rule.body
    web_information = 0
    for key in bodyrule.keys():
        #print(key)   #排查哪条正则写错了
        if '&' in key:
            keys = re.split('&',key)
            if re.search(keys[0],body,re.I) and re.search(keys[1],body,re.I):
                web_information = bodyrule[key]
                break
            else:
                continue
        else:
            req = re.search(key,body,re.I)
            if req:
                web_information = bodyrule[key]
                break
            else:
                continue

    return web_information


def main_scan(title='',header='',body=''):
    web_information = scan_title(title=title)
    if web_information == 0:
        web_information = scan_head(header=header,body=body)
        if web_information == 0:
            web_information = scan_body(body=body)
            if web_information == 0:
                information = '未知'
            else:
                information = web_information
        else:
            information = web_information
    else:
        information = web_information
    return information


def get_apptype(appname):
    return '无'


