"""
@file:   server
@author: linuxzhen520@163.com
@date:   2020/02/08
@desc:
"""

from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=app.config["DEBUG"])
