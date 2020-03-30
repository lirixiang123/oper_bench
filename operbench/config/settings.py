"""
@file:   settings
@author: linuxzhen520@163.com
@date:   2020/02/08
@desc:
"""

AVATOR_SIZE = "60*60"
PER_PAGE = 10
import logging
from logging.handlers import RotatingFileHandler
# 启动的监听端口和IP也以在这里配置
# 启动的监听端口和IP也以在这里配置
# 日志配置
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，日志保存到哪里，日志文件大小....
import os
if not os.path.isdir("./logs"):
    os.makedirs("logs")
file_log_handler = RotatingFileHandler("logs/log.log", maxBytes=1024, backupCount=5)
# 创建日志格式
formatter = logging.Formatter("%(levelname)s %(filename)s: %(lineno)d %(message)s")
file_log_handler.setFormatter(formatter)
# 为全局工具的日志对象加载日志记录器
logging.getLogger().addHandler(file_log_handler)

# 如果在你的项目中有很多个日志记录器，用字典形式定义
