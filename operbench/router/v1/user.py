"""
@file:   user
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:
"""

# 蓝图/可扩展蓝图
from flask import Blueprint, request, g
from flask_restful import Resource, Api
from libs.handler import default_error_handler
from forms.user import RegisterForm, LoginForm
from models.user import UserProfile
from libs.response import generate_response
from serializer.user import user_schema
from libs.error_code import ArgsTypeException
from libs.authorize import create_token, auth

user_bp = Blueprint('user', __name__, url_prefix='/user/')
api = Api(user_bp)
# 设置当出现异常时的标准化输出
api.handle_error = default_error_handler



# 创建用户注册功能
class RegisterView(Resource):
    def post(self):
        # 获取用户传过来的参数(api的参数为json数据)
        data = request.json
        # 检查参数的合法性（RequestParser/WTForms）
        form = RegisterForm(data=data)
        # 如果合法，创建
        if form.validate():
            # 创建用户UserProfile.create_user()
            user = UserProfile.create_user(user_profile_email=form.email.data,
                                    user_profile_name=form.name.data,
                                    password=form.password.data)
            return generate_response(data=user_schema.dump(user))
        else:
            raise ArgsTypeException(message=form.errors)

# 用户登录功能
class LoginView(Resource):
    def post(self):
        x = request
        # 获取用户传过来的参数(api的参数为json数据)
        data = request.json
        # 将数据与LoginForm进行绑定
        form = LoginForm(data=data)
        # 检查用户是否合法
        user = form.validate()
        # 生成token
        token = create_token(uid=user.user_profile_id)
        return generate_response(data={"token":token})


class UserView(Resource):
    @auth.login_required
    def get(self):
        print(g.user)
        user = UserProfile.query.filter_by(user_profile_id=g.user.get('uid')).first()
        if user:
            result = {
                "name": user.user_profile_name,
                "user_id": user.user_profile_id,
                "access": ['super_admin', 'admin'],
                "token": 'super_admin',
                "avatar": 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1584520364&di=db69d24b012b2f38f45db664eb0c6425&src=http://uploads.xuexila.com/allimg/1612/907-16122QJ510-50.jpg'
            }
        else:
            result = {
                "name": 'super_admin',
                "user_id": '1',
                "access": ['super_admin', 'admin'],
                "token": 'super_admin',
                "avatar": 'https://file.iviewui.com/dist/a0e88e83800f138b94d2414621bd9704.png'
                }
        return result




api.add_resource(RegisterView, '/register/')
api.add_resource(LoginView, '/login/')
api.add_resource(UserView, '/')