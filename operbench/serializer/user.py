"""
@file:   user
@author: linuxzhen520@163.com
@date:   2020/03/17
@desc:
"""

from .base import ma
from models.user import UserProfile


class UserSchema(ma.Schema):
    class Meta:
        # 为哪个用户模型创建序列化器
        model = UserProfile
        # 序列化出来的结果有哪些字段
        fields = ('user_profile_id', 'user_profile_email', 'user_profile_name', 'user_profile_mobile')

user_schema = UserSchema()
users_schema = UserSchema(many=True)