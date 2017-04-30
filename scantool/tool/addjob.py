#-*- coding: UTF-8 -*-
import redis
#  向redis 添加扫描任务脚本
pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)
r = redis.StrictRedis(connection_pool=pool)

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



def insert_ip_redis(name,ip):    #端口在扫描设置里面添加
    ip = ip.split('-')
    startip = ip[0]
    endip = ip[1]
    iplist = ip_range(startip,endip)
    for i in iplist:
        r.lpush(name,i)


# insert_ip_redis('ad','218.60.147.1-218.60.148.255')