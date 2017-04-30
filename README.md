基于django 框架 redis  elasticsearch web指纹搜索引擎
==== 
![](https://github.com/cuijianxiong/websearch/blob/master/1.png) 
![](https://github.com/cuijianxiong/websearch/blob/master/2.png)
![](https://github.com/cuijianxiong/websearch/blob/master/3.png)
![](https://github.com/cuijianxiong/websearch/blob/master/4.png)

安装
------- 
apt-get install mysql-server mysql-client <br>
vi /etc/mysql/mysql.conf.d/mysqld.cnf<br>
apt-get install redis-server <br>
apt-get install masscan<br>

在 [mysqld] 域下加上：<br>

character-set-server=utf8<br>

pip3 install django==1.9.5<br>
pip3 install pymysql==0.7.2<br>
pip3 install BeautifulSoup4==4.5.3<br>
celery=3.1.25<br>
pip3 install elasticsearch<br>
pip3 install elasticsearch_dsl<br>
django-celery 3.2.1 <br>
flower 0.9.1<br>
lxml     3.7.3<br>
requests   2.13.0<br>
redis   2.10.5<br>

source sql文件 chttp.sql<br>
配置elasticsearch-jdbc-2.3.4.0/bin/mysql-chttp.sh  的环境变量及数据库密码<br>
配置webscan/settings.py  DATABASES属性配置数据库密码<br>
配置scantool/tool/config.py  <br>

启动
------- 
1 先启动elasticsearch  这里用的elasticsearch-2.3.4<br>
2 elasticsearch-jdbc-2.3.4.0/bin/mysql-chttp.sh  增量同步数据库脚本 <br>
也可以启动  mysql-dump.sh  等扫描任务结束后一起插入elasticsearch<br>
3 python3 manage.py runserver 0.0.0.0:8000<br>
4 python3 manage.py celery worker -l info -c 3  异步脚本 这里启动3线程<br>
5 愉快的扫描吧  <br>


tips
------- 
1 在scantool/views.py  startjob函数下tasks.dmain.delay  为异步扫描任务  这里默认启动了三个<br>
可以往上加如果性能好的话<br>
random_str  为生成cookie函数 自己改吧<br>



遗憾
-------
有些问题还不够完美后续有时间会完美下去<br>

1 cookie单点登录问题  这个以后解决  cookie还不过期啊<br>
2 scantool/tool/rule.py  为指纹扫描规则 （这里用了赵武大大fofa的规则 见谅哈  没全添加进去  ）<br>
3 elasticsearch搜索有些问题 貌似中文的事情  汉语是世界上最好的语言~~~~<br>
4 界面丑  js css html什么的我都不会啊<br>
5 scantool/tool/webscan.py 下get_host_informathion函数我为了速度设置成了timeout=2  可以改了  因为前期用masscan探测存活了<br>
6 hostscan那个目录可以删的  没用的  辣鸡~~~<br>
7 有啥问题最好邮件问我  github我不咋上<br>
8 渣渣写的东西  大牛轻喷啊<br>
