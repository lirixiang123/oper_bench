"""
@file:   ops_tools
@author: linuxzhen520@163.com
@date:   2020/03/24
@desc:
"""
import datetime
from .base import db


class Task(db.Model):
    # id, name, command, args, host
    __tablename__ = "tasks"
    task_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    task_name = db.Column(db.String(64), nullable=False)
    task_command = db.Column(db.String(256), nullable=False)
    task_args = db.Column(db.String(256))
    task_host = db.Column(db.String(16), nullable=False)
    tasklogs = db.relationship("TaskLog", backref="task")



class TaskLog(db.Model):
    __tablename__ = "tasklog"
    tasklog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    task_id = db.Column(db.ForeignKey('tasks.task_id'), nullable=False)
    # celery任务的id
    tasklog_tid = db.Column(db.String(64), nullable=False)
    tasklog_result = db.Column(db.Text)
    tasklog_create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    user = db.Column(db.ForeignKey("user_profile.user_profile_id"))

