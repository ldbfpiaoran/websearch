import requests
import json

'''查询ip地理位置  注意接口上限 续费'''

def ip_scan(ip):
    host = 'https://dm-81.data.aliyun.com'
    path = '/rest/160601/ip/getIpInfo.json'
    appcode = 'fbdf0c736f6644f6992550040849aada'
    querys = 'ip='+ip
    url = host+path+'?'+querys
    header = {'Authorization':'APPCODE fbdf0c736f6644f6992550040849aada'}
    result = '无'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url,headers=header,verify=False,timeout=2)
        r = json.loads(response.text)
        country = r['data']['country']
        region = r['data']['region']
        city = r['data']['city']
        isp = r['data']['isp']
        result = country+','+city+','+isp
        # print(result)
    except:
        # print(ip+'>>>>> false')
        result = 'unknow'
    return result

# ip_scan('47.93.87.52')