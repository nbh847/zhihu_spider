from .utils import Utils
from config.items import db, ThirdPartyShops, ThirdPartyGoods, ThirdPartyGoodsDetails
import json
from config.utils import RedisQueue
from config.setting import *

'''
 * @author Nibinhui
 * @since 2018/4/18
 *
'''


class Handler(object):

    def __init__(self):
        self.logger = get_logger()
        self.shop_redis = RedisQueue('shop')
        self.goods_redis = RedisQueue('goods')
        self.sg_redis = RedisQueue('shop-goods')
        self.goods_details_redis = RedisQueue('goods-details')




handler = Handler()
if __name__ == "__main__":
    h = Handler()
    h.run()
