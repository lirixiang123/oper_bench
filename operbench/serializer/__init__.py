"""
@file:   __init__
@author: linuxzhen520@163.com
@date:   2020/03/17
@desc:
"""

from .base import ma

def init_app(app):
    ma.init_app(app)