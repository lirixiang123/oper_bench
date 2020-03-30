"""
@file:   parse
@author: linuxzhen520@163.com
@date:   2020/03/16
@desc:
"""

from enum import Enum

def get_value(obj, key):
    if obj:
        value = getattr(obj, key)
        print(value)
        return value.name if isinstance(value, Enum) else value
    else:
        return ""


def get_value_list(objlist, *keys):
    """返回一个列表数据"""
    if len(keys) == 0:
        return list()
    else:
        result = list()
        for item in objlist:
            if len(keys) == 1:
                result.append(getattr(item, keys[0]))
            else:
                t_result = dict()
                for key in keys:
                    t_result[key] = getattr(item, key)
                result.append(t_result)
        return result


def get_ip(nics, eth):
    """获取网卡的ip地址：eth0"""
    for nic in nics:
        if eth == nic.nic_name:
            return nic.nic_ipaddr
    return ""


def server_item_parse(server):
    # 将一台服务的数据转化成一个字典格式
    # {id:xxx, os:xxx, hostname:xxx,.....}
    result = {
        "id": server.server_id,
        "os": server.server_os,
        "hostname": get_value(server.asset, "asset_hostname"),
        "sn": get_value(server.asset, "asset_sn"),
        "asset_type": get_value(server.asset, "asset_asset_type"),
        "ip":  get_ip(server.nics, "eth0"),
        "public_ip": get_ip(server.nics, "eth1"),
        "private_ip": get_ip(server.nics, "eth0"),
        "port": 22,
        "idc": get_value(server.asset.idc, "idc_name_cn"),
        "admin_user": get_value_list(server.asset.admin.managers, "user_profile_name") if server.asset.admin else [],
        "region": get_value(server.asset.idc, "idc_region"),
        "state": "true",
        "detail": get_value(server, "note"),
        "create_time": get_value(server, "create_at"),
        "update_time": get_value(server, "update_at"),
        # "tag_list": [
        #     "AWS",
        #     "腾讯云",
        #     "阿里云",
        #     "内网",
        #     "Demo"
        # ]
    }
    return result


def server_parse(servers):
    """将服务器数据序列化成目标格式"""
    if isinstance(servers, list):
        result = list()
        for server in servers:
            result.append(server_item_parse(server))
    else:
        result = server_item_parse(servers)
    return result