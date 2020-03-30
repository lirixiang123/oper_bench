"""
@file:   user
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:
"""

# 蓝图/可扩展蓝图
from flask import Blueprint, request, current_app
from flask_restful import Api, Resource
from models.cmdb import Server, db, Asset, Nic, IDC
from libs.response import generate_response
from libs.parse import server_parse
from serializer.cmdb import idcs_schema, idc_schema
from libs.handler import default_error_handler
from libs.authorize import api_authorize, auth
from sqlalchemy import or_
import logging
cmdb_bp = Blueprint('cmdb', __name__, url_prefix='/cmdb')
# 创建一个restfulAPI
api = Api(cmdb_bp)

# 设置当处理异常时的处理办法(handle_error是异常的统一处理接口)
# api.handle_error = default_error_handler

@cmdb_bp.route('/')
def index():
    logging.info("user访问了index页面,可以写到装饰器中")
    return "/v1/cmdb/"

# 使用restful-api来进行接口开发
class ServerView(Resource):
    @auth.login_required
    def get(self):
        """获取所有服务器信息"""
        params = request.args
        page = int(params.get("page", 1))
        per_page = int(params.get("limit", current_app.config["PER_PAGE"]))
        keywords = params.get("key", "")
        if keywords:
            # 根据条件查询指定的数据(key => sn, hostname)
            # 跨表查询
            result = db.session.query(Server).join(Asset).filter(or_(Asset.asset_sn.like(f"%{keywords}%"), Asset.asset_hostname.like(f"%{keywords}%")))
        else:
            # 获取所有数据
            result = Server.query
        # 将查询到的数据进行分页
        paginate_servers = result.paginate(page, per_page=per_page, error_out=False)
        # 将数据序列化
        servers = server_parse(paginate_servers.items)
        # 返回数据（减少代码冗余）
        return generate_response(data=servers, total=paginate_servers.total)
        # 全文搜索 => ElasticSearch => 数据量比较大

    @auth.login_required
    def put(self):
        # 接收的数据[{},{}]
        return generate_response(data=[])

    @auth.login_required
    def post(self):
        import time
        import random
        params = request.json
        # 添加Asset -> 主机名
        hostname = params.get("hostname", "")
        asset_sn = params.get("sn", "")
        asset_sn = asset_sn if asset_sn else hash(str(time.time())+str(random.randint(1,99999)))
        asset = Asset(asset_sn=asset_sn, asset_hostname=hostname)
        # 添加Server -> idc
        detail = params.get("detail", "")
        server = Server(asset=asset, note=detail)
        # 添加NIC -> ip
        ipaddr = params.get("ip")
        eth = "eth0"
        nic = Nic(nic_ipaddr=ipaddr, nic_name=eth, server=server)
        # 入库
        db.session.add_all([asset, server, nic])
        db.session.commit()
        return generate_response(data=server_parse(server))


class IDCView(Resource):
    @auth.login_required
    def get(self):
        """获取所有idc信息"""
        # Log(user=xxx, method=request.method, url=request.url, ...)
        # commit()
        # 封装成装饰器
        params = request.args
        keywords = params.get("key", "")
        if keywords:
            idcs = IDC.query.filter_by(idc_name=keywords).all()
        else:
            idcs = IDC.query.all()
        return generate_response(data=idcs_schema.dump(idcs), total=len(idcs))

    @auth.login_required
    def post(self):
        """新建一个idc信息"""
        params = request.json
        idc_name = params.get("name","")
        idc = IDC(idc_name=idc_name, idc_name_cn=idc_name)
        db.session.add(idc)
        db.session.commit()
        return generate_response(data = idc_schema.dump(idc))

    @auth.login_required
    def put(self):
        """编辑idc信息"""
        pass


api.add_resource(ServerView, "/servers/")
api.add_resource(IDCView, "/idcs/")
