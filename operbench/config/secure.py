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
# uri统一资源匹配符
# SQLALCHEMY_DATABASE_URI配置数据库连接的参数
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@127.0.0.1:3306/school?charset=utf8'
# 请求结束后自动提交数据库修改
SQLALCHEMY_COMMMIT_ON_TEARDOWN = True
# 如果设置成 True (默认情况)，Flask-SQLAlchemy	将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。


SECRET_KEY = "this is a secret key"

EXPIRES_IN = 3600 * 24

