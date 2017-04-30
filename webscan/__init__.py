from __future__ import absolute_import
import pymysql
pymysql.install_as_MySQLdb()
from .celery import app as celery_app

