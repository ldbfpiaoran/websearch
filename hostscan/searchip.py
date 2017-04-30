import requests
import redis


def get_ip(name):
    pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)
    r = redis.StrictRedis(connection_pool=pool)
    task = r.brpop(name, 0)
    #print(r.llen(name))   #  当前队列长度
    task = task[1].decode('ascii')
    return task


def get_information(url,port):
    # 准备用 cms识别框架
    #待解决问题   扫描队列的停止问题  准备用 celery+redis
    pass


def save_information(information):
    pass




def main(task,port):
    url = 'http://'+task
    for p in port:
        information = get_information(url=url,port=p)
        save_information(information)


