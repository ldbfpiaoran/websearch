import os
import redis
from scantool.tool import taskcontrol

pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)
r = redis.StrictRedis(connection_pool=pool)

def masscan(name,port,host):
    osname = os.name
    tmp = str(host)+'.log'
    if osname is 'nt':
        try:
            path = os.getcwd()
            os.chdir(path+'\\scantool\\masscan\\windows_64')
            os.system('masscan.exe -p%s %s -oL %s --rate=10000'%(port,host,tmp))
            result_file = open(tmp, 'r')
            result_json = result_file.readlines()
            result_file.close()
            del result_json[0]
            del result_json[-1]
            for res in result_json:
                try:
                    ip = res.split()[3]
                    port = res.split()[2]
                    r.lpush(name, ip+':'+port)
                except Exception as e:
                    print(e)
            os.remove(tmp)
            taskcontrol.updatatask(tasksid=name, completenum=0, status='2')
        except Exception as e:
            print(e)
    elif osname is 'posix':
        try:
            os.chdir('scantool/masscan/linux_64')
            os.system('masscan -p%s %s -oL %s --rate=10000' % (port, host, tmp))
            result_file = open(tmp, 'r')
            result_json = result_file.readlines()
            result_file.close()
            del result_json[0]
            del result_json[-1]
            for res in result_json:
                try:
                    ip = res.split()[3]
                    port = res.split()[2]
                    r.lpush(name, ip+':'+port)
                except Exception as e:
                    print(e)
            os.remove(tmp)
            taskcontrol.updatatask(tasksid=name, completenum=0, status='2')
        except Exception as e:
            print(e)




