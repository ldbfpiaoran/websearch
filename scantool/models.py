#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class tasksdata(models.Model):
    status = models.CharField(max_length=500,verbose_name='任务状态')
    taskname = models.CharField(max_length=500,verbose_name='任务名称')
    taskdata = models.CharField(max_length=500,verbose_name='任务内容')
    num = models.IntegerField(verbose_name='任务数量',default=0)
    completenum = models.IntegerField(verbose_name='完成数量',default=0)
    taskport = models.CharField(max_length=500,verbose_name='任务端口')

    def __str__(self):
        return self.taskname

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cookie = models.CharField(max_length=255,null=True)

    def __unicode__(self):
        return self.username

