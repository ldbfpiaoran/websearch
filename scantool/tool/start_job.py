#-*- coding: UTF-8 -*-
#开始扫描
import redis
from scantool.scan import webscan
from scantool.tool import taskcontrol



pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)
r = redis.StrictRedis(connection_pool=pool)


def startjob(number,taskname):
    surplus = 1
    number = int(number)
    while surplus > 0 :
        surplus = r.llen(taskname)
        task = r.brpop(taskname, 0)
        ip = task[1].decode('ascii')
        # print(ip)
        # print(port)
        print(ip)
        webscan.scan_main(ip=ip)
        if r.llen(taskname) ==0:
            taskcontrol.updatatask(tasksid=int(taskname),completenum=100,status='4')
            break
        elif surplus%200 == 0:
            completenum = (number-surplus)*100//number
            taskcontrol.updatatask(tasksid=int(taskname), completenum=completenum, status='3')



