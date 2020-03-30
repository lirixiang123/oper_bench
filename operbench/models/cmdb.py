"""
@file:   cmdb
@author: linuxzhen520@163.com
@date:   2020/03/11
@desc:
"""


from .base import db
from libs.enums import DiskIfaceType, StatusType, AssetType
from .user import UserProfile


# 一个表 => 继承自db.Model一个类
# 每一个表都要求有一个主键,一般我们主键都设置的是id为自增的主键
# 字段名的命名 => 表名_字段名
class Asset(db.Model):
    __tablename__ = "asset"
    # 一个数据库字段，就是类的一个db.Column属性
    asset_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asset_asset_type = db.Column(db.Enum(AssetType))
    asset_hostname = db.Column(db.String(64))
    asset_sn = db.Column(db.String(128), nullable=False, unique=True)
    manufactory_id = db.Column(db.ForeignKey('manufactory.manufactory_id'))
    asset_model = db.Column(db.String(64))
    # 合同相关就不在这里设置了
    asset_warranty = db.Column(db.DateTime())
    # 业务线 （业务线名字+成员）  => 业务管理员
    business_unit_id = db.Column(db.ForeignKey('business_unit.business_unit_id'))
    # 管理员  （管理员组名+成员） => 硬件管理员
    admin_id = db.Column(db.ForeignKey('business_unit.business_unit_id'))
    # 由于这里两个字段链接到同一个表了，不避免区分不开，relationship写在这里
    business_unit = db.relationship("BusinessUnit", backref="asset_businesses",foreign_keys=[business_unit_id])
    admin = db.relationship("BusinessUnit", backref="asset_admins",foreign_keys=[admin_id])
    idc_id = db.Column(db.ForeignKey('idc.idc_id'))
    asset_floor = db.Column(db.Integer())
    asset_cabinet_num = db.Column(db.String(32))
    asset_cabinet_order = db.Column(db.Integer())
    asset_status = db.Column(db.Enum(StatusType))
    asset_maintain_record = db.Column(db.Text())
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    # 是否启用当前数据
    status = db.Column(db.Integer())
    # 一对一关系 server与asset
    server = db.relationship("Server", backref="asset", uselist=False)


class Manufactory(db.Model):
    __tablename__ = "manufactory"
    manufactory_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 为asset添加反向查询字段 => 字段名叫 manufactory
    assets = db.relationship('Asset', backref='manufactory')
    disks = db.relationship('Disk', backref='manufactory')
    rams = db.relationship('Memory', backref='manufactory')
    manufactory_name = db.Column(db.String(64))
    manufactory_tel = db.Column(db.String(11))
    manufactory_note = db.Column(db.Text)
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    # 是否启用当前数据
    status = db.Column(db.Integer())


class IDC(db.Model):
    __tablename__ = "idc"
    idc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asserts = db.relationship('Asset', backref='idc')
    idc_name = db.Column(db.String(64))
    idc_name_cn = db.Column(db.String(64))
    idc_region = db.Column(db.String(64))
    # 运营商
    idc_isp = db.Column(db.String(64))
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())


business_unit_users = db.Table("business_unit_users",
                               db.Column("user_profile_id", db.ForeignKey("user_profile.user_profile_id")),
                               db.Column("business_unit_id", db.ForeignKey("business_unit.business_unit_id"))
                               )

class BusinessUnit(db.Model):
    __tablename__ = "business_unit"
    business_unit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_unit_name = db.Column(db.String(64))
    business_unit_name_cn = db.Column(db.String(64))
    # m2m =>好多人 => 管理员
    # 一个业务应该由很多人来维护， 一个人可以维护多个业务线
    managers = db.relationship("UserProfile",
                               # 指定中间表
                               secondary=business_unit_users,
                               backref="business_units")
    business_unit_note = db.Column(db.Text)
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())


class Server(db.Model):
    __tablename__ = "server"
    server_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.asset_id'))
    server_cpu_count = db.Column(db.Integer)
    server_cpu_cour_count = db.Column(db.Integer)
    server_cpu_model = db.Column(db.String(64))
    nics = db.relationship("Nic", backref='server')
    disks = db.relationship("Disk", backref='server')
    rams = db.relationship("Memory", backref='server')
    server_raid_type = db.Column(db.String(6))
    server_ram_size = db.Column(db.Integer)
    server_os = db.Column(db.ForeignKey("os.os_id"))
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())


class Nic(db.Model):
    __tablename__ = "nic"
    nic_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nic_name = db.Column(db.String(12))
    nic_model = db.Column(db.String(32))
    server_id = db.Column(db.ForeignKey("server.server_id"))
    nic_ipaddr = db.Column(db.String(32))
    nic_mac = db.Column(db.String(17))
    nic_netmask = db.Column(db.String(15))
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())


class OS(db.Model):
    __tablename__ = "os"
    os_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    os_type = db.Column(db.String(64))
    os_version = db.Column(db.String(128))
    servers = db.relationship("Server", backref="os")
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())


class Disk(db.Model):
    __talbename__ = "disk"
    disk_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    disk_sn = db.Column(db.String(128), nullable=False, unique=True)
    server_id = db.Column(db.ForeignKey("server.server_id"))
    disk_slot = db.Column(db.String(10))
    manufactory_id = db.Column(db.ForeignKey("manufactory.manufactory_id"))
    disk_model = db.Column(db.String(32))
    disk_capacity = db.Column(db.String(10))
    disk_iface_type = db.Column(db.Enum(DiskIfaceType))
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())


class Memory(db.Model):
    __tablename__ = "memory"
    memory_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    memory_sn = db.Column(db.String(128), nullable=False, unique=True)
    server_id = db.Column(db.ForeignKey("server.server_id"))
    memory_slot = db.Column(db.String(10))
    manufactory_id = db.Column(db.ForeignKey("manufactory.manufactory_id"))
    memory_model = db.Column(db.String(32))
    memory_capacity = db.Column(db.String(10))
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())
