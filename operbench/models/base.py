"""
@file:   base
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:
"""

from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()

from . import cmdb
from . import user
from . import ops_tools
