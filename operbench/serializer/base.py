"""
@file:   __init__
@author: linuxzhen520@163.com
@date:   2020/03/17
@desc:
"""

from flask_marshmallow import Marshmallow
ma = Marshmallow()

# 注册序列化器到 ma
from . import user