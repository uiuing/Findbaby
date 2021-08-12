'''
Author        : uiuing
Date          : 2021-03-22 14:46:39
LastEditTime  : 2021-05-17 22:31:00
LastEditors   : uiuing
Description   : 数据对象
FilePath      : /DataCollection/Findbaby/items.py
©️ uiuing.com
'''

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FindbabyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 丢失地址
    Lost_place = scrapy.Field()
    # 找回地点
    Return_location = scrapy.Field()
    
    # ID
    n_id = scrapy.Field()
    # 人像
    image = scrapy.Field()
    # 姓名
    name = scrapy.Field()
    # 性别
    sex = scrapy.Field()
    # 出生日期
    birth = scrapy.Field()
    # 失踪时身高
    height = scrapy.Field()
    # 失踪时间
    missing_time = scrapy.Field()
    # 失踪地点
    address = scrapy.Field()
    # 失踪地点ID
    address_id = scrapy.Field()
    # 特征描述
    person = scrapy.Field()
    # 其它资料
    after = scrapy.Field()
    # url 
    url = scrapy.Field()
    pass
