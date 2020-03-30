"""
@file:   enums
@author: linuxzhen520@163.com
@date:   2020/03/16
@desc:
"""

import enum

class AssetType(enum.Enum):
    SERVER = 1
    NETWORK = 2


class StatusType(enum.Enum):
    INIT = 0
    ONLINE = 1
    OFFLINE = 2
    UNREACHABLE = 3
    MAINTAIN = 4

class DiskIfaceType(enum.Enum):
    Disk = 0


class MethodType(enum.Enum):
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5
