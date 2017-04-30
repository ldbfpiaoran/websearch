#-*- coding: UTF-8 -*-

#创建扫描ip段

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

