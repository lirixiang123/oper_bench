"""
@file:   __init__.py
@author: linuxzhen520@163.com
@date:   2020/03/24
@desc:
"""

from celery import Celery

celery = Celery("celery_app")
# 从配置文件中读取并配置celery
celery.config_from_object('config.celery_config')