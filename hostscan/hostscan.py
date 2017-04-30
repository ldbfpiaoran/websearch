import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
import pymysql



'''
CREATE TABLE httpdata (id BIGINT(7) NOT NULL AUTO_INCREMENT, ip VARCHAR(200),title VARCHAR(10000),header
VARCHAR(10000), created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(id));

'''


def save_data(url,title,header):
    print(url, title, header)
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root',
                               db='mysql', charset='utf8', port=3306)
        conn = conn.cursor()
        conn.execute('use http_information')

        savesql = 'insert into `scantool_httpdata` (`ip`,`title`,`header`) values (%s,%s,%s)'
        conn.execute(savesql, (url, title, header))
        conn.connection.commit()
    except:
        conn.close()




def get_host_informathion(url):
    print('start......'+url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1471.914 Safari/537.36'}
    try:
        response = requests.get(url=url, headers=headers,timeout=5)
        response.encoding = response.apparent_encoding
        head = response.headers
        header = ''
        for key in head.keys():  # 将 header集合
            header = header + key + ':' + head[key]+'    '
        if response.status_code == 200:
            try:
                bresponse = BeautifulSoup(response.text, "lxml")
                title = bresponse.findAll('title')
                for i in title:
                    title = i.get_text()
            except:
                title = ''

        if header and title:
            result = [url,title,header]
            save_data(url,title,header)
            print(url + '成功')
        else:
            print(url+'失败')
    except:
        result = 500
        print(url+'失败')




def ipnum(ip):
    ip = [int(x) for x in ip.split('.')]
    return ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3]


def numip(num):
    return '%s.%s.%s.%s' % ((num & 0xff000000) >> 24,
                            (num & 0x00ff0000) >> 16,
                            (num & 0x0000ff00) >> 8,
                            num & 0x000000ff)

def ip_range(start, end):
    return [numip(num) for num in range(ipnum(start), ipnum(end) + 1) if num & 0xff]


def main(startip,endip,port=[80,81,8080,8081,8000]):
    iplist = ip_range(startip,endip)
    urllist = []
    result = []
    pool = Pool(2)
    for ip in iplist:
        for p in port:
            urllist.append('http://'+str(ip)+':'+str(p))
    # pool.map(get_host_informathion,urllist)
    for i in urllist:
        pool.apply_async(get_host_informathion,args=(i,))
    pool.close()
    pool.join()

if __name__ == '__main__':
    httpdata = []
    main('59.44.20.1','59.44.20.255')










