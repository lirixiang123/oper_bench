"""
@file:   __init__
@author: linuxzhen520@163.com
@date:   2020/02/09
@desc:
"""

from .view01 import view01_bp
from .v1 import v1_bp

def init_app(app):
    app.register_blueprint(view01_bp)
    app.register_blueprint(v1_bp)