'''
Author        : uiuing
Date          : 2021-05-11 17:09:08
LastEditTime  : 2021-05-17 22:33:15
LastEditors   : uiuing
Description   : 概率统计
FilePath      : /DataAnalysis/Probabilistic_Analysis/reducer.py
©️ uiuing.com
'''

#! /usr/bin/env python3

import sys

Address_information, Calculation_basis, sum_values = None, 1, 1

for line in sys.stdin:
    try:
        line = line.rstrip()
        Address_information,Calculation_basis,sum_values = line.split("\t", 2)
    except:
        continue
    if Address_information:
        print("%s\t%s\t%.8f" % (Address_information[0:6],Address_information[6:12],float(Calculation_basis)/float(sum_values)/1000))
