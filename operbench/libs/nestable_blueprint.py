"""
@file:   nestable_blueprint
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:   定义了一个可扩展蓝图
"""

from flask import Blueprint

class NestableBlueprint(Blueprint):
    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            # v1_bp.register_blueprint(cmdb_bp)
            # state => 当前蓝图 => v1_bp
            # blueprint => 子蓝图=>cmdb_bp
            # 获取当前最终版的url前缀 => /api/v1/cmdb
            url_prefix = (state.url_prefix or u"") + (options.get('url_prefix', blueprint.url_prefix) or u"")
            if 'url_prefix' in options:
                del options['url_prefix']
            # 注册蓝图
            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)
        # 添加路由记录=>record的参数是一个函数
        self.record(deferred)