'''
Author        : uiuing
Date          : 2021-05-11 17:09:11
LastEditTime  : 2021-05-17 22:33:00
LastEditors   : uiuing
Description   : 逻辑回归
FilePath      : /DataAnalysis/Probabilistic_Analysis/mapper.py
©️ uiuing.com
'''

#! /usr/bin/env python3

import sys

current_Address, current_count, Address_information = None, 1, None

key_array,value_array = list(),list()

for line in sys.stdin:
    try:
        line = line.rstrip()
        Address_information, count = line.split("\t", 1)
        count = int(count)
        key_array.append(Address_information)
        value_array.append(count)
    except:
        continue
    if current_Address != None and current_Address[0:6] == Address_information[0:6]:
        current_count += count
    else:
        if current_Address:
            for index in range(0,len(key_array)-1):
                print("%s\t%u\t%u" % (key_array[index], value_array[index], current_count))
            ram_key = key_array[-1]
            ram_value = value_array[-1]
            key_array.clear()
            value_array.clear()
            key_array.append(ram_key)
            value_array.append(ram_value)
        current_count, current_Address = count,Address_information
        
if current_Address[0:6] == Address_information[0:6]:
    for index in range(0,len(key_array)):
        print("%s\t%u\t%u" % (key_array[index], value_array[index], current_count))
