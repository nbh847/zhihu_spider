# 爬虫API执行入口

from flask import Flask
from flask_restful import Resource, Api, reqparse
from config.api_handler import handler
from config.setting import FAILED_CODE, SUCCESS_CODE, DEBUG_STATUS, API_HOST, API_PORT

# API入口
app = Flask(__name__)
api = Api(app)

# parser是参数设置
parser = reqparse.RequestParser()
parser.add_argument('shop_url', type=str, default='', help='商铺主页链接地址')

api.add_resource(ChangeRedis, '/redis')

if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT, debug=DEBUG_STATUS)
