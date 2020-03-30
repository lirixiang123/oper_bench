"""
@file:   authorize.py
@author: linuxzhen520@163.com
@date:   2020/03/16
@desc:
"""
from hashlib import md5
from flask import request, current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from models.user import APIToken
from libs.error_code import APIAuthorizedException

# 创建auth方法
# 知道当前是哪种客户端访问

auth = HTTPBasicAuth()
"""
HTTPBasicAuth 是 HTTP协议中规定的一种定义方式
在协议中规定了数据应该如何发送 
header: key => Authorization
        value => basic base64(username:password)
当执行了auth.login_required => @auth.verify_password 装饰的函数
    如果该函数的返回值为True那么表示认证成功
    如果return False => Unauthorized Access 
    如果认证失败，而是直接raise APIAuthorizedException()
"""

@auth.verify_password
def verify_password(token, password):
    """多种认证方式"""
    print(token)
    if token and password:
        # 如果token和密码都有值，表示是使用用户密码认证
        raise APIAuthorizedException(message="这是用户名密码认证")
    elif token and token=="api":
        # 如果token有值，并且值为"api"
        return api_authorize()
    elif token:
        # 如果只有token，进行token认证
        data = verify_token(token)
        g.user = data
        return True
        # raise APIAuthorizedException(message="这是token认证")
    else:
        raise APIAuthorizedException(message="参数传递不完整")


def has_permission(api_token, url, method):
    """权限该api是否有指定url和指定方法的权限"""
    # 从服务端查找appid及对应的秘钥
    mypermission = method+url
    all_permissions = [permission.api_permission_method_type.name+permission.api_permission_url for permission in api_token.permissions]
    if mypermission not in all_permissions:
        raise APIAuthorizedException(message="没有当前接口的权限")
    return True


def api_authorize():
    # 客户端如何认证的？服务端也如何认证
    # sign 与  mysign一致
    # 客户端传过来的数据
    x = request
    params = request.args
    appid = params.get("appid", "")
    salt = params.get("salt", "")
    sign = params.get("sign", "")
    api_token = APIToken.query.filter_by(api_token_appid=appid).first()
    if not api_token:
        raise APIAuthorizedException(message="认证失败！没有查找到api_token")
    has_permission(api_token, url=request.path, method=request.method)
    user_appid = api_token.api_token_appid
    user_secretkey = api_token.api_token_secretkey
    user_sign = user_appid+salt+user_secretkey
    m1 = md5()
    m1.update(user_sign.encode(encoding="utf-8"))
    user_sign = m1.hexdigest()
    if sign != user_sign:
        raise APIAuthorizedException()
    else:
        return True


def create_token(uid):
    """生成token:uid, 有效期，密钥"""
    s = Serializer(current_app.config["SECRET_KEY"], current_app.config["EXPIRES_IN"])
    token = s.dumps({"uid":uid}).decode("ascii")
    return token


def verify_token(token):
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        # 尝试将token解密出来 => data
        data = s.loads(token)
    except BadSignature:
        raise APIAuthorizedException(message="无效的token")
    except SignatureExpired:
        raise APIAuthorizedException(message="token已过期")
    return data