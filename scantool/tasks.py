#-*- coding: UTF-8 -*-
from __future__ import absolute_import
from scantool.tool import masscan,start_job


from celery import shared_task


@shared_task(name='scan')
def dmain(tasksdata):
    # print(str(tasksdata['tasksid']))
    start_job.startjob(number=tasksdata['num'],taskname=str(tasksdata['tasksid']))     #  执行任务


@shared_task(name='masscanjob')
def masscanjob(name,port,host):
    print('aaaa')
    masscan.masscan(name=name,port=port,host=host)


