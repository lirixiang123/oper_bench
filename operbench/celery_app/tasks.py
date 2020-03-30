"""
@file:   tasks
@author: linuxzhen520@163.com
@date:   2020/03/24
@desc:
"""

from . import celery
import time
import random
import paramiko

@celery.task
def celery_task(sth1):
    print("celery_app.task start")
    delay_time = random.randint(5, 10)
    time.sleep(delay_time)
    print("celery_app.task end")
    return sth1


@celery.task
def rum_cmd(host, cmd):
    """连接到服务器，执行指定命令"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, 22, timeout=5)
        # stdin, stdout, stderr = ssh.exec_command(env_cmd)
        ## stdin.write("Y")   #简单交互，输入 ‘Y’
        stdin, stdout, stderr = ssh.exec_command(cmd)
        err = stderr.read()
        out = stdout.read()
        ssh.close()
        result = out if out else err
        return result.decode("utf-8")
    except Exception as ex:
        print(ex)