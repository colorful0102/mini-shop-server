# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/2.
  Flask 对配置项的限制，你必须保证命名全都大写，才能注入到current_app.config中
"""
from app.libs.enums import ClientTypeEnum
__author__ = 'Allen7D'

'''
应用于Swagger的URL，会自动添加协议前缀(http://或者https://)，因为会切换协议前缀
local_setting.py中 SERVER_URL = '127.0.0.1:8010'
'''
SERVER_URL = 'server.mini-shop.ivinetrue.com'  # 外部（云服务器）地址
SERVER_SCHEMES = ["https", "http"]
# 所有红图的路径
API_PATH = 'app.api'
# all api by module(version)
# 可以控制Swagger API文档的显示顺序
ALL_RP_API_LIST = \
    ['v1.token'] + \
    ['cms.admin', 'cms.group', 'cms.auth'] + \
    ['v1.user', 'v1.address',
     'v1.banner', 'v1.theme', 'v1.category', 'v1.product', 'v1.order', 'v1.pay'] + \
    ['cms.user', 'cms.file']

# 所有endpoint的meta信息
EP_META = {}
EP_INFO_LIST = []
EP_INFOS = {}

# 项目的github地址
GITHUB_URL = 'https://github.com/Allen7D/mini-shop-serve'
# 项目文档地址
DOC_URL = 'http://doc.mini-shop.ivinetrue.com'

# 登录类型(站内)
CLINET_INNER_TYPES = (ClientTypeEnum.USERNAME, ClientTypeEnum.EMAIL, ClientTypeEnum.MOBILE)