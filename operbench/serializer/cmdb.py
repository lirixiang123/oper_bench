"""
@file:   user
@author: linuxzhen520@163.com
@date:   2020/03/17
@desc:
"""

from .base import ma
from models.cmdb import IDC


class IDCSchema(ma.Schema):
    class Meta:
        # 为哪个用户模型创建序列化器
        model = IDC
        # 序列化出来的结果有哪些字段
        fields = ('idc_id','idc_name', 'idc_name_cn', 'idc_region', 'idc_isp')

idc_schema = IDCSchema()
idcs_schema = IDCSchema(many=True)