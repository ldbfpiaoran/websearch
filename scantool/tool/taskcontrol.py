#-*- coding: UTF-8 -*-
from scantool.tool import config,createip
import pymysql
import re


localconfig = config.Config

def addtask(taskname,taskdata,taskport,completenum=0):
    '''

    :param status: 0 未开始 1 扫描中 2 完成
    :param tasksname: 任务名称
    :param taskdata:  任务内容
    :param taskport:  任务端口
    :param tasktaddrs:   任务ip
    :return:
    '''
    status = 0
    ip = re.split('-',taskdata)
    startip = ip[0]
    endip = ip[1]
    taskaddrs = createip.ip_range(startip,endip)
    num = len(taskaddrs)

    try:
        conn = pymysql.connect(host=localconfig.host, user=localconfig.username, passwd=localconfig.passwd, db='mysql',
                           charset=localconfig.charset, port=localconfig.port)
        conn = conn.cursor()
        conn.execute('use chttp')
        savesql = 'insert into `scantool_tasksdata` (`status`,`taskname`,`taskdata`,`num`,`completenum`,`taskport`) values (%s,%s,%s,%s,%s,%s)'
        print((status,taskname,taskdata,num,completenum,taskport))
        conn.execute(savesql,(status,taskname,taskdata,num,completenum,taskport))
        conn.connection.commit()
    except Exception as e:
        print(e)
        conn.close()


# def taskshow():
#     try:
#         conn = pymysql.connect(host=localconfig.host, user=localconfig.username, passwd=localconfig.passwd, db='mysql',
#                            charset=localconfig.charset, port=localconfig.port)
#         conn = conn.cursor()
#         conn.execute('use http_information')
#         searchsql = 'select tasksid,status,taskname,taskdata,taskport from tasksdata'
#         conn.execute(searchsql)
#         result = conn.fetchall()
#
#         data = []
#         for i in result:
#             each = {}
#             each['tasksid'] = i[0]
#             each['status'] = i[1]
#             each['taskname'] = i[2]
#             each['taskdata'] = i[3]
#             each['taskport'] = i[4]
#             data.append(each)
#     except:
#         conn.close()
#     return data
#
#
# def getpage(tablename):
#     try:
#         conn = pymysql.connect(host=localconfig.host, user=localconfig.username, passwd=localconfig.passwd, db='mysql',
#                            charset=localconfig.charset, port=localconfig.port)
#         conn = conn.cursor()
#         conn.execute('use http_information')
#         sql = 'select count(*) from '+tablename
#         conn.execute(sql)
#         result = conn.fetchone()
#         count = result[0]
#         print(count)
#     except:
#         conn.close()
#     return count


def deletetask(tasksid):
    # try:
    conn = pymysql.connect(host=localconfig.host, user=localconfig.username, passwd=localconfig.passwd, db='chttp',
                           charset=localconfig.charset, port=localconfig.port)
    cur = conn.cursor()
    # conn.execute('use http_information')
    sql = "DELETE FROM scantool_tasksdata WHERE id="+str(tasksid)
    print(sql)
    sta = cur.execute(sql)

    if sta==1:
        print('Done')
    else:
        print('Failed')
    conn.commit()
    cur.close()
    conn.close()


def gettask(tasksid):
    conn = pymysql.connect(host=localconfig.host, user=localconfig.username, passwd=localconfig.passwd, db='chttp',
                           charset=localconfig.charset, port=localconfig.port)
    cur = conn.cursor()
    # conn.execute('use http_information')
    sql = "SELECT * FROM scantool_tasksdata WHERE id="+str(tasksid)
    cur.execute(sql)
    result = cur.fetchall()
    each = {}
    for i in result:
        each['tasksid'] = i[0]
        each['status'] = i[1]
        each['taskname'] = i[2]
        each['taskdata'] = i[3]
        each['num']  = i[4]
        each['completenum'] = i[5]
        each['taskport'] = i[6]
    # print(each['status'])
    # print(type(each['tasksid']))
    return each


def updatatask(tasksid,completenum,status):
    conn = pymysql.connect(host=localconfig.host, user=localconfig.username, passwd=localconfig.passwd, db='chttp',
                           charset=localconfig.charset, port=localconfig.port)
    cur = conn.cursor()
    sql = 'UPDATE scantool_tasksdata SET completenum='+str(completenum)+',status="'+status+'" WHERE id='+str(tasksid)
    sta = cur.execute(sql)
    # if sta==1:
    #     print('Done')
    # else:
    #     print('Failed')
    conn.commit()
    cur.close()
    conn.close()



