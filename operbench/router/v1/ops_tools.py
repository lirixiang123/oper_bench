"""
@file:   user
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:
"""

# 蓝图/可扩展蓝图
from flask import Blueprint, request, g
from flask_restful import Resource, Api
from libs.handler import default_error_handler
from libs.response import generate_response
from libs.error_code import ArgsTypeException
from libs.authorize import auth
from models.ops_tools import Task, db, TaskLog
from serializer.ops_tools import task_schema, tasks_schema, tasklog_schema, tasklogs_schema
from celery_app.tasks import rum_cmd
from celery.result import AsyncResult
from celery_app import celery

ops_tools_bp = Blueprint('ops_tools', __name__, url_prefix='/ops_tools')
api = Api(ops_tools_bp)
# 设置当出现异常时的标准化输出
# api.handle_error = default_error_handler

# 任务管理
class TaskView(Resource):
    @auth.login_required
    def get(self):
        tasks = tasks_schema.dump(Task.query.all())
        return generate_response(data=tasks, total=len(tasks))

    @auth.login_required
    def post(self):
        params = request.json
        task_name = params.get("command_name", "")
        task_command = params.get("command","")
        task_args = params.get("args", "")
        task_host = params.get("force_host", "")
        # 这里请同学们自己进行优化 => forms . validate
        task = Task(task_name=task_name, task_args=task_args,
                    task_command=task_command,task_host=task_host)
        db.session.add(task)
        db.session.commit()
        return generate_response(data=task_schema.dump(task))

    @auth.login_required
    def delete(self):
        params = request.json
        # 凡是获取客户端数据 => 都使用forms来进行数据检验和检查
        task_id = params.get("task_id", "")
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        return generate_response(data=[])

class RunTaskView(Resource):
    @auth.login_required
    def post(self):
        # 获取参数部分，每个函数都有类似代码，可以优化
        params = request.json
        task_id = params.get("task_id","")
        # get根据id来查找数据
        task = Task.query.get(task_id)
        # 发布异步任务
        res = rum_cmd.delay(task.task_host, task.task_command)
        # 写日志
        tasklog = TaskLog(task_id=task.task_id, tasklog_tid=res.task_id, user=g.user.get("uid"))
        db.session.add(tasklog)
        db.session.commit()
        return generate_response(data=tasklog_schema.dump(tasklog))

class TaskLogView(Resource):
    @auth.login_required
    def get(self):
        tasklogs = TaskLog.query.all()
        for tasklog in tasklogs:
            res = AsyncResult(tasklog.tasklog_tid, app=celery)
            if not tasklog.tasklog_result and res.result:
                tasklog.tasklog_result = res.result
                db.session.add(tasklog)
        db.session.commit()
        return generate_response(data=tasklogs_schema.dump(tasklogs), total=len(tasklogs))



api.add_resource(TaskView, '/tasks/')
api.add_resource(RunTaskView, '/tasks/run/')
api.add_resource(TaskLogView, '/tasklogs/')
