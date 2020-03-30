"""
@file:   user.py
@author: linuxzhen520@163.com
@date:   2020/03/17
@desc:
"""

from wtforms import Form, StringField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
from models.user import UserProfile
from werkzeug.security import check_password_hash
from libs.error_code import APIAuthorizedException


class RegisterForm(Form):
    """定义用户注册的数据校验"""
    email = StringField(validators=[DataRequired(message="password是必填项"),
                                    Email(message="邮箱不合法")])
    password = StringField(validators=[DataRequired(message="password是必填项"),
                                       Regexp(r'^\w{6,18}$', message="输入的密码不符合规范")])
    name = StringField()


    def validate_email(self, value):
        # 增加额外对email的验证，value => email
        # 验证email在数据库中否存在，如果已经存在 raise
        if UserProfile.query.filter_by(user_profile_email=value.data).first():
            raise ValidationError("邮箱已经存在")

    # def validate_name(self, value):
    #     pass


class LoginForm(Form):
    # 这里字段的值一定要跟调用方传过来的参数名一致，iview-admin的登录这里用的userName,password
    userName = StringField(validators=[DataRequired(), Email()])
    password = StringField(validators=[DataRequired()])

    def validate(self):
        """验证邮箱密码是否一致"""
        user = UserProfile.query.filter_by(user_profile_email=self.userName.data).first()
        if user and check_password_hash(user.password, self.password.data):
            return user
        else:
            raise APIAuthorizedException(message=self.errors)