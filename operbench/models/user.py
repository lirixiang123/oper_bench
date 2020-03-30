"""
@file:   user
@author: linuxzhen520@163.com
@date:   2020/03/16
@desc:
"""
import random
import string
from werkzeug.security import generate_password_hash
from .base import db
from libs.enums import MethodType

class UserProfile(db.Model):
    __tablename__ = "user_profile"
    user_profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_profile_name = db.Column(db.String(32), nullable=False)
    # business_units = db.relationship('BusinessUnit', backref='user_profile')
    # business_unit_id = db.Column(db.Integer, db.ForeignKey("business_unit.business_unit_id"))
    user_profile_email = db.Column(db.String(32), nullable=False, unique=True)
    user_profile_mobile =  db.Column(db.String(11))
    # password=>数据表中的列名
    _password = db.Column("password", db.String(128))
    api_tokens = db.relationship("APIToken", backref="user_profile")
    tasklogs = db.relationship("TaskLog", backref="user_profile")
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())

    # password是真实对外的属性 => password.setter, password.getter, password.deleter
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        # value => 明文密码
        self._password = generate_password_hash(value)

    @classmethod
    def create_user(cls, user_profile_email, user_profile_name, password):
        user = cls()
        user.user_profile_email = user_profile_email
        user.user_profile_name = user_profile_name if user_profile_name else "".join(random.choices(string.ascii_letters, k=8))
        user.password = password
        db.session.add(user)
        db.session.commit()
        return user




api_token_permissions = db.Table("api_token_permissions",
                                 db.Column("api_token_id", db.ForeignKey("api_token.api_token_id")),
                                 db.Column("api_permission_id", db.ForeignKey("api_permission.api_permission_id")),
                                 )

class APIToken(db.Model):
    __tablename__ = "api_token"
    api_token_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_token_appid = db.Column(db.String(32))
    api_token_secretkey = db.Column(db.String(32))
    user_profile_id = db.Column(db.ForeignKey("user_profile.user_profile_id"))
    permissions = db.relationship("APIPermission",
                                  secondary=api_token_permissions,
                                  backref= "api_tokens")
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())


class APIPermission(db.Model):
    __tablename__ = "api_permission"
    api_permission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_permission_url = db.Column(db.String(128))
    api_permission_method_type = db.Column(db.Enum(MethodType))
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())
