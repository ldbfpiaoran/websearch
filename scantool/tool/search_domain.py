import requests
import json
'''
ip反查域名脚本

'''
# def search_domain1(ip):    爱站查询
#     try:
#         domain = []
#         url =  'http://dns.aizhan.com/'+ip+'/'
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1471.914 Safari/537.36'}
#         response = requests.get(url=url,headers=headers,timeout=2)
#         response.encoding = response.apparent_encoding
#         response = BeautifulSoup(response.text, "lxml")
#         data = response.find('table',{'style':'border-top:none'}).findAll('a',{'target':'_blank'})
#         for i in data:
#             domain.append(i.get_text())
#     except Exception as e:
#         print(e)
#         domain = '未知'
#     return domain


# webscan.cc 接口

def search_domain(ip):
    try:
        domain = []
        url = 'http://www.webscan.cc/?action=query&ip='+ip
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1471.914 Safari/537.36'}
        response = requests.get(url=url,headers=headers,timeout=3)
        response.encoding = response.apparent_encoding
        response = response.text
        response = json.loads(response)
        for i in response:
            domain.append(i['domain'])
    except Exception as e:
        print(e)
        domain = '未知'
    # print(domain)
    return domain



