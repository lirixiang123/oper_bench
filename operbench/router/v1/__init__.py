"""
@file:   __init__
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:
"""

from libs.nestable_blueprint import NestableBlueprint

from .cmdb import cmdb_bp
from .user import user_bp
from .ops_tools import ops_tools_bp

v1_bp = NestableBlueprint('v1', __name__, url_prefix='/api/v1')
v1_bp.register_blueprint(cmdb_bp)
v1_bp.register_blueprint(user_bp)
v1_bp.register_blueprint(ops_tools_bp)

