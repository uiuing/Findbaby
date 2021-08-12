'''
Author        : uiuing
Date          : 2021-03-22 14:46:39
LastEditTime  : 2021-05-17 22:29:48
LastEditors   : uiuing
Description   : 数据存储
FilePath      : /DataCollection/Findbaby/pipelines.py
©️ uiuing.com
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os

class SuccessCasePipeline:
    """生成json文件!"""
   
    def __init__(self):
        self.file = open('success_case.json', 'w')

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(item_json+'\n')
        return item

    def close_spider(self, spider):
        self.file.close()
        print ("{}:爬虫数据处理完毕!".format(spider.name))
    

class MissingPipeline:

    """生成json文件!"""

    def __init__(self):
        self.file = open('Missing.json', 'w')
        self.file.write("[")

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)+','
        self.file.write(item_json+'\n')
        return item

    def close_spider(self, spider):
        self.file.close()

        f = open('Missing.json', 'rb+')
        f.seek(-2,2)
        f.truncate() 
        f.close()

        f = open('Missing.json', 'a')
        f.write("]")
        f.close()
        print ("{}:爬虫数据处理完毕!".format(spider.name))