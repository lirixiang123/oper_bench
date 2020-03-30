"""
@file:   router
@author: linuxzhen520@163.com
@date:   2020/02/08
@desc:
"""


from flask import Blueprint


view01_bp = Blueprint('view01',__name__,url_prefix='/view01/')

# from flask import Flask, current_app
# app = current_app()
# 注意：这里用/index/,在浏览器上可以用/index或/index/
# (flask内部做一次重定向) => F12可查看
@view01_bp.route('/index/')
def index():
    # 调用一个异步任务
    from celery_app.tasks import celery_task
    # 立即发送任务，立刻执行任务
    celery_task.delay('hello world!')
    # celery_task.apply_async() => 指定运行倒计时，发送到哪个队列....
    return "This is index"

def index2():
    return "This is index2"
view01_bp.add_url_rule('/index2/', view_func=index2)
