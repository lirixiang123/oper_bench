"""
@file:   user
@author: linuxzhen520@163.com
@date:   2020/03/17
@desc:
"""

from .base import ma
from models.ops_tools import Task


class TaskSchema(ma.Schema):
    class Meta:
        # 为哪个用户模型创建序列化器
        model = Task
        # 序列化出来的结果有哪些字段
        fields = ('task_id', 'task_name', 'task_command', 'task_host', 'task_args')

class TaskLogSchema(ma.Schema):
    class Meta:
        # 为哪个用户模型创建序列化器
        model = Task
        # 序列化出来的结果有哪些字段
        fields = ('tasklog_tid', 'tasklog_result', 'tasklog_create_time', 'user')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
tasklog_schema = TaskLogSchema()
tasklogs_schema = TaskLogSchema(many=True)

