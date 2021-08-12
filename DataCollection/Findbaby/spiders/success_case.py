'''
Author        : uiuing
Date          : 2021-03-22 15:00:54
LastEditTime  : 2021-05-17 22:31:21
LastEditors   : uiuing
Description   : 获取成功案例
FilePath      : /DataCollection/Findbaby/spiders/success_case.py
©️ uiuing.com
'''

import scrapy
from Findbaby.items import FindbabyItem
from Findbaby.spiders.ParticipleAndMatch import ParticipleAndMatch as PM

class SuccessCaseSpider(scrapy.Spider):

    name = 'success_case'
    allowed_domains = ['www.baobeihuijia.com']
    # !URI
    start_urls = ['https://www.baobeihuijia.com/succeed.aspx?keywords=&page={}'.format(
        i) for i in range(1,107)]

    def parse(self, response):

        item = FindbabyItem()

        Lost_place = response.xpath('.//table/tr/td[5]/text()').extract()
        Return_location = response.xpath('.//table/tr/td[6]/text()').extract()

        Lost_p = list()
        Return_l = list()
        for i in range(0, len(Return_location)):
            ram_Lstr = PM.Run_Str(self,Lost_place[i])
            ram_Rstr = PM.Run_Str(self,Return_location[i])
            if ram_Lstr != "" and ram_Rstr != "":
                Lost_p.append(ram_Lstr)
                Return_l.append(ram_Rstr)
        
        item['Lost_place'] = Lost_p
        item['Return_location'] = Return_l

        yield item
