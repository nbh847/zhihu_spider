import peewee as pw
from .setting import *

db = pw.MySQLDatabase(MYSQL_DB_NAME, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD,
                      charset=MYSQL_CHARSET)


# 店铺信息(第三方商家池)
class ThirdPartyShops(pw.Model):
    shop_id = pw.CharField(verbose_name="店铺ID", max_length=100, default='')
    platform = pw.IntegerField(verbose_name="店铺平台, 1=>淘宝，2=>天猫", default=0)
    name = pw.CharField(verbose_name="店铺名字", max_length=100, default='')
    shop_url = pw.CharField(verbose_name="店铺主页链接", max_length=400, default='')
    banner_imgs = pw.TextField(verbose_name="店铺banner图", default='')
    crawl_status = pw.IntegerField(verbose_name="店铺是否有被第一遍抓取,默认没有被抓取", default=0)
    update_time = pw.DateTimeField(verbose_name="店铺数据更新时间", default='1970-01-01')

    class Meta:
        database = db
        # 设置复合主键
        primary_key = pw.CompositeKey('shop_id', 'platform')
