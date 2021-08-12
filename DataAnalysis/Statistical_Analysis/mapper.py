'''
Author        : uiuing
Date          : 2021-05-11 16:49:46
LastEditTime  : 2021-05-17 22:32:09
LastEditors   : uiuing
Description   : 分词
FilePath      : /DataAnalysis/Statistical_Analysis/mapper.py
©️ uiuing.com
'''
#! /usr/bin/env python3

import sys
import json

for line in sys.stdin:
    Key_Information = json.loads(line.strip())
    Lost_place_key = Key_Information['Lost_place'] 
    Return_location_key = Key_Information['Return_location']
    for i in range(0, len(Lost_place_key)):
        try:
            print("%s\t1" % (Lost_place_key+Return_location_key))
        except:
            pass