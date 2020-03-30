"""
@file:   celery_config
@author: linuxzhen520@163.com
@date:   2020/03/24
@desc:
"""

# 配置消息中间件的地址
BROKER_URL = "redis://127.0.0.1:6379/1"

# 结果存放地址
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"

# 启动Celery时，导入任务
CELERY_IMPORTS = (
    'celery_app.tasks',
)

from celery.schedules import crontab
# 配置定时任务
CELERYBEAT_SCHEDULE = {
    "task1-every-minute":{
        'task': 'celery_app.tasks.celery_task',
        'schedule': crontab(minute="*/1"),
        'args': ('hello li',),
    }
}
