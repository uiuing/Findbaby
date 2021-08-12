'''
Author        : uiuing
Date          : 2021-05-12 09:11:50
LastEditTime  : 2021-05-17 22:33:49
LastEditors   : uiuing
Description   : missing table 数据存储
FilePath      : /DataAnalysis/Data_Stored_To_Cloud/Stored_Missing_mysql.py
©️ uiuing.com
'''

import json
import pymysql as pm
from pymysql.converters import escape_string

db = pm.connect(
    host='43.129.74.180',user='FindBaby',password='pisX7XmWMc3WjcwK',
    db='findbaby',port=5743,charset='utf8mb4'
)
cur = db.cursor()

#? create table 
    # sql_create_table = """
    # CREATE TABLE Missing (
    #     n_id int(10),
    #     image varchar(100),
    #     name varchar(100),
    #     sex varchar(10),
    #     birth varchar(50),
    #     height varchar(50),
    #     missing_time varchar(50),
    #     address varchar(50),
    #     address_id int(20),
    #     person varchar(1300),
    #     after varchar(1300)
    # )
    # """
#? create index
    # sql_create_index = """
    # create index missing_index on missing(address_id);
    # """"
#? Perform operation
    # cur.execute(sql_create_table)
    # db.commit()
    # cur.execute(sql_create_index)
    # db.commit()

sql = """
    insert into missing values (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    ON DUPLICATE KEY UPDATE 
    image = %s,
    name = %s,
    sex = %s,
    birth = %s,
    height = %s,
    missing_time = %s,
    address = %s,
    address_id = %s,
    person = %s,
    after = %s
"""


with open("DataCollection/Missing.json",'r',encoding='utf-8') as f: data=json.load(f)

i = 0
for lines in data:
    i += 1
    n_id = lines['n_id']
    image =  lines['image']
    name = escape_string(lines['name'])
    sex = lines['sex']
    birth = escape_string(lines['birth'])
    height = escape_string(lines['height'])
    missing_time = escape_string(lines['missing_time'])
    address = escape_string(lines['address'])
    address_id = lines['address_id']
    person = escape_string(lines['person'])
    after = escape_string(lines['after'])

    sql_list = (n_id,image,name,sex,birth,height,
                missing_time,address,address_id,person,after,
                image,name,sex,birth,height,
                missing_time,address,address_id,person,after)
    
    try:
        cur.execute(sql,sql_list)
        db.commit()
        print("ok id:",n_id," 次数:",i,end="\r", flush=True)
    except  pm.Warning as e:
        print ("\n\n",e)
        db.rollback()
        print("\n插入数据失败\n")
print("存储成功")
f.close()
cur.close()
db.close()