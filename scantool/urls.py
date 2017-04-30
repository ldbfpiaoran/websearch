#-*- coding: UTF-8 -*-
"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from scantool.views import *

urlpatterns = [
    url(r'^webscan/$', webscan, name='webscan'),
    url(r'^insertip/$', insert_ip, name='insert_ip'),
    url(r'^index/$', index, name='index'),
    url(r'^$', index, name='index'),
    url(r'^scan/$', scan, name='scan'),
    url(r'^addtask/$', addtask, name='addtask'),
    url(r'^delete/$', deletetask, name='deletetask'),
    url(r'^addjob/$', addjob, name='addjob'),
    url(r'^startjob/$', startjob, name='startjob'),
    url(r'^login/$', login, name='login'),
    url(r'^search/$', search, name='search'),
]
