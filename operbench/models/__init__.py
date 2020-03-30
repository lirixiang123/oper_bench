"""
@file:   __init__
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:
"""

from .base import db

def ini_app(app):
    db.init_app(app)
