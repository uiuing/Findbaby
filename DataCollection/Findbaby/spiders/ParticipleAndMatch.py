'''
Author        : uiuing
Date          : 2021-04-01 16:13:39
LastEditTime  : 2021-05-17 22:30:36
LastEditors   : uiuing
Description   : 地区行政代码获取
FilePath      : /DataCollection/Findbaby/spiders/ParticipleAndMatch.py
©️ uiuing.com
'''

import scrapy
import cpca
import numpy as np

class ParticipleAndMatch:

    def Run_Str(self,Str):
        # ! Participle
        Str = np.array(cpca.transform([Str]))[:,-1]
        if Str:
            return "".join(Str)
        return ""

    