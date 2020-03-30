"""
@file:   response
@author: linuxzhen520@163.com
@date:   2020/03/16
@desc:
"""
from libs.error_code import Success

def generate_response(data,
                      message=Success.message,
                      status_code=Success.status_code,
                      **kwargs
                      ):
    return {
        "message": message,
        "status_code": status_code,
        "data": data,
        **kwargs
    }
