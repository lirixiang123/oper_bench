"""
@file:   app
@author: linuxzhen520@163.com
@date:   2020/02/08
@desc:
"""
import os
from flask import Flask
from flask_cors import CORS


def create_app(config=None):
    app = Flask(__name__)
    cors = CORS(app, resources={"*": {"origins":"*"}})
    # load default configuration
    app.config.from_object('config.settings')
    app.config.from_object('config.secure')

    # load environment configuration
    # FLASK_CONF="/path/to/config_dev.py"
    # FLASK_CONF="/path/to/config_prod.py"
    # 也可以根据系统环境变量，加载不同的配置文件
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')

    # load app sepcified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    import router, models, serializer
    router.init_app(app)
    models.ini_app(app)
    serializer.init_app(app)
    return app