"""
定义与测试用例相关的配置
"""

import os
import sys
basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)
# 配置一个测试数据库
DB_PATH = 'sqlite:///' + os.path.join(basedir, 'test_data.sqlite')


