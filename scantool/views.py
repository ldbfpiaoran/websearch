# -*- coding: UTF-8 -*-
# import logging
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from scantool.models import *
from scantool.tool.cmscan import *
from hostscan import insert_redis
from scantool.tool import taskcontrol,searchtool
from scantool import tasks
from random import Random
import json

# 生成cookie


def random_str(randomlength=29):
    cook = ''
    chars = '_AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        cook+=chars[random.randint(0, length)]
    return cook


def index(request):            # 主页
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username,cookie__exact=cookie)
    if islogin:
        return render(request,'index.html', locals())
    else:
        return HttpResponseRedirect('/login/')


def webscan(request):
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username,cookie__exact=cookie)
    if islogin:
        try:
            url = request.POST.get('url')
            information = main(url)
        except Exception as e:
            print(e)
            # logger.error(e)
        return render(request, 'webscan.html', locals())
    else:
        return HttpResponseRedirect('/login/')


def getPage(request, result_list):          # 分页效果
    paginator = Paginator(result_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        result_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        result_list = paginator.page(1)
    return result_list


def insert_ip(request):
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username, cookie__exact=cookie)
    if islogin:
        name = request.GET.get('name')
        ip = request.GET.get('ip')
        insert_redis.insert_ip_redis(name, ip)

        return HttpResponseRedirect('/scan/')
    else:
        return HttpResponseRedirect('/login/')


def addtask(request):    # 添加任务
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username, cookie__exact=cookie)
    if islogin:
        try:
            taskname = request.POST.get('taskname')
            taskdata = request.POST.get('taskdata')
            taskport = request.POST.get('taskport')
            taskcontrol.addtask(taskname, taskdata, taskport)
        except:
            print('没有属性')

        return HttpResponseRedirect('/scan/')
    else:
        return HttpResponseRedirect('/login/')


def deletetask(request):    # 删除任务
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username,cookie__exact=cookie)
    if islogin:
        try:
            tsid = request.POST.get('tasksid')
            taskcontrol.deletetask(tasksid=tsid)
        except:
            print('没有属性')

        return HttpResponseRedirect('/scan/')
    else:
        return HttpResponseRedirect('/login/')


def scan(request):    # 获取任务页面
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username, cookie__exact=cookie)
    if islogin:
        try:
            result_list = tasksdata.objects.all()
            data = getPage(request,result_list)
        except Exception as e:
            print(e)
            # logger.error(e)
        return render(request, 'scan.html', locals())
    else:
        return HttpResponseRedirect('/login/')


def addjob(request):
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username, cookie__exact=cookie)
    if islogin:
        try:
            tsid = request.POST.get('tasksid')
            tasksdata = taskcontrol.gettask(tasksid=tsid)  # 获取任务
            if tasksdata['status'] == '0':
                tasks.masscanjob.delay(name=tasksdata['tasksid'], host=tasksdata['taskdata'], port=tasksdata['taskport'])
                taskcontrol.updatatask(tasksid=tasksdata['tasksid'], completenum=0, status='1')
            else:
                print('任务开始啦')
        except Exception as e:
            print(e)

        return HttpResponseRedirect('/scan/')
    else:
        return HttpResponseRedirect('/login/')


def startjob(request):
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username,cookie__exact=cookie)
    if islogin:
        try:
            tsid = request.POST.get('tasksid')
            tasksdata = taskcontrol.gettask(tasksid=tsid)  # 获取任务
            if tasksdata['status'] == '2':
                taskcontrol.updatatask(tasksid=tasksdata['tasksid'], completenum=0, status='3')
                tasks.dmain.delay(tasksdata=tasksdata)
                tasks.dmain.delay(tasksdata=tasksdata)
                tasks.dmain.delay(tasksdata=tasksdata)
            else :
                print('任务开始啦')
        except Exception as e:
            print(e)
            # logger.error(e)

        return HttpResponseRedirect('/scan/')
    else:
        return HttpResponseRedirect('/login/')

def search(request):
    cookie = request.COOKIES.get('islogin')
    username = request.COOKIES.get('username')
    islogin = User.objects.filter(username__exact=username,cookie__exact=cookie)
    if islogin:
        try:
            searchdata = request.GET.get('searchcontent')
            page = request.GET.get('page')
            if searchdata != '':
                if ':' in searchdata:
                    searchdata = searchdata.split('&')
                    content = {}
                    for i in searchdata:
                        i = i.split(':')
                        content[i[0]] = i[1]
                    portarray, count, pagecount = searchtool.search(page=page,dic=content)
                else:
                    portarray, count, pagecount = searchtool.search(page=page,scontent=searchdata)
                pagec = []
                for i in range(1,pagecount):
                    pagec.append(i)
                if portarray == '':
                    return render(request, '111.html', locals())
                else:
                    return render(request,'showdata.html',locals())
        except Exception as e:
            print(e)

        return render(request,'111.html',locals())

        pass
    else:
        return HttpResponseRedirect('/login/')





def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                user = User.objects.filter(username__exact=username, password__exact=password)
                if user:
                    cook = random_str()
                    User.objects.filter(username__exact=username).update(cookie=cook)
                    response = HttpResponseRedirect('/index/')
                    response.set_cookie('islogin', cook, 3600)
                    response.set_cookie('username', username, 3600)
                    return response
                else:
                    return HttpResponseRedirect('/login/')
        except Exception as e:
            print(e)
    else:
        return render(request, 'login.html', locals())





