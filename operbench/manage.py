"""
@file:   manage.py
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:
"""


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from app import create_app
from celery_app import celery
app = create_app()

manager = Manager(app)

# 创建db管理工具 => app, db
# 注意，如果是sqlite数据库需要修改
# migrate = Migrate(app, db)
with app.app_context():
   migrate = Migrate()
   if db.engine.url.drivername == 'sqlite':
       migrate.init_app(app, db, render_as_batch=True)
   else:
       migrate.init_app(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()