"""
@file:   secure
@author: linuxzhen520@163.com
@date:   2020/02/08
@desc:
"""

DEBUG = True
ENV = "development"

# 注意=>Debug这个名字不行
# DEBUG在Flask中有一个默认值为False

# DB配置
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "this is a secret key"

EXPIRES_IN = 3600 * 24

