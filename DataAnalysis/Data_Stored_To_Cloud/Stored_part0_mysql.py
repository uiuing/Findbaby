'''
Author        : uiuing
Date          : 2021-05-12 11:44:05
LastEditTime  : 2021-05-17 22:34:19
LastEditors   : uiuing
Description   : pb table 数据存储
FilePath      : /DataAnalysis/Data_Stored_To_Cloud/Stored_part0_mysql.py
©️ uiuing.com
'''

import json
import pymysql as pm
from pymysql.converters import escape_string

db = pm.connect(
    host='43.129.74.180',user='FindBaby',password='pisX7XmWMc3WjcwK',
    db='findbaby',port=5743,charset='utf8'
)
cur = db.cursor()

#? create table 
    # sql_create_table = """
    # CREATE TABLE  pb(
    #     input int(10),
    #     pb double,
    #     outs int(10)
    # )
    # """
#? create index
    # sql_create_index = """
    # create index pb_index on pb(input);
    # """"
#? Perform operation
    # cur.execute(sql_create_table)
    # db.commit()
    # cur.execute(sql_create_index)
    # db.commit()

sql = """
    insert into pb values (%s,%s,%s);
"""

i = 0
for line in open("DataAnalysis/part-00000",'r',encoding='utf-8'):
    
    i += 1
    
    inputs,outs,pb_index = line.split("\t",3)

    sql_list = (inputs.split(),pb_index.split(),outs.split())
    
    try:
        cur.execute(sql,sql_list)
        db.commit()
        print("ok id:",inputs," 次数:",i,end="\r", flush=True)
    except  pm.Warning as e:
        print ("\n\n",e)
        db.rollback()
        print("\n插入数据失败\n")

print("存储成功")
cur.close()
db.close()