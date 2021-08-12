'''
Author        : uiuing
Date          : 2021-05-11 16:50:54
LastEditTime  : 2021-05-17 22:32:29
LastEditors   : uiuing
Description   : 特征分类
FilePath      : /DataAnalysis/Statistical_Analysis/reducer.py
©️ uiuing.com
'''

#! /usr/bin/env python3

import sys

current_Address, current_count, Address_information = None, 1, None

for line in sys.stdin:
    try:
        line = line.rstrip()
        Address_information, count = line.split("\t", 1)
        count = int(count)
    except:
        continue
    if current_Address == Address_information:
        current_count += count
    else:
        if current_Address:
            print("%s\t%u" % (current_Address, current_count))
        current_count, current_Address = count,Address_information
        
if current_Address == Address_information:
    print("%s\t%u" % (current_Address, current_count))
