'''
Author        : uiuing
Date          : 2021-04-01 23:20:37
LastEditTime  : 2021-05-17 22:30:09
LastEditors   : uiuing
Description   : 采集失踪数据
FilePath      : /DataCollection/Findbaby/spiders/Missing.py
©️ uiuing.com
'''
import scrapy
import re
from Findbaby.items import FindbabyItem
from Findbaby.spiders.ParticipleAndMatch import ParticipleAndMatch as PM

class MissingSpider(scrapy.Spider):
    name = 'Missing'
    allowed_domains = ['www.baobeihuijia.com']
    start_urls = ['https://www.baobeihuijia.com/list.aspx?tid=1&sex=&photo=1&page={}'.format(
        i) for i in range(1, 470)]

    def parse(self, response):

        href_url = response.xpath('//dt/a/@href').extract()

        for index in range(0,len(href_url)):

            href = 'https://www.baobeihuijia.com/' + str(href_url[index])

            yield scrapy.Request(href, callback=self.parser_detail)

    def parser_detail(self,response):

        item = FindbabyItem()
        
        # Individual information
        Individual_information = response.xpath("//*[@id=\"table_1_normaldivr\"]/ul/li/text()").extract()
        if int((Individual_information[3])[0:4]) > 1998:
            # ID
            n_id = response.xpath("//*[@id=\"table_1_normaldivr\"]/ul/li[2]/a/text()").extract()[0]
            
            # ID
            item['n_id'] = n_id
            # 人像
            item['image'] = "https://www.baobeihuijia.com/photo/Small/s_"+str(n_id)+".jpg"
            # 姓名
            item['name'] = Individual_information[1]
            # 性别
            item['sex'] = Individual_information[2]
            #出生日期
            item['birth'] = Individual_information[3]
            # 失踪时身高
            item['height'] = Individual_information[4]
            # 失踪时时间
            item['missing_time'] = Individual_information[5]
            # 失踪地点
            item['address'] = Individual_information[6]
            # 失踪地点ID
            item['address_id'] = PM.Run_Str(self, Individual_information[6])  
            # 特征描述
            item['person'] = Individual_information[7].replace('\r\n', '')
            # 其它资料
            item['after'] = Individual_information[8].replace('\r\n', '')

            yield item

        



        
