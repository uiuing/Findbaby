'''
Author        : uiuing
Date          : 2021-05-17 22:34:33
LastEditTime  : 2021-05-17 22:48:36
LastEditors   : uiuing
Description   : mi table 数据存储
FilePath      : /DataAnalysis/Data_Stored_To_Cloud/Stored_mi_mysql.py
©️ uiuing.com
'''


import json
import pymysql as pm
from pymysql.converters import escape_string

db = pm.connect(
    host='43.129.74.180', user='FindBaby', password='pisX7XmWMc3WjcwK',
    db='findbaby', port=5743, charset='utf8mb4'
)
cur = db.cursor()

# ? create table
# sql_create_table = """
# CREATE TABLE `mi` (
#   `image` varchar(100) DEFAULT NULL,
#   `name` varchar(100) DEFAULT NULL,
#   `sex` varchar(10) DEFAULT NULL,
#   `birth` varchar(50) DEFAULT NULL,
#   `missing_time` varchar(50) DEFAULT NULL,
#   `address` varchar(170) DEFAULT NULL,
#   `address_id` int DEFAULT NULL,
#   `person` varchar(1300) DEFAULT NULL,
#   `after` varchar(1300) DEFAULT NULL,
#   `url` varchar(100) DEFAULT NULL,
#   UNIQUE KEY `url` (`url`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
# """
# ? create index
# sql_create_index = """
# create index mi_index on mi(address_id);
# """"
# ? Perform operation
# cur.execute(sql_create_table)
# db.commit()
# cur.execute(sql_create_index)
# db.commit()

sql = """
    insert into mi values (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    ON DUPLICATE KEY UPDATE 
    image = %s,
    name = %s,
    sex = %s,
    birth = %s,
    missing_time = %s,
    address = %s,
    address_id = %s,
    person = %s,
    after = %s
"""


with open("mi.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

i = 0
for lines in data:
    i += 1
    image = lines['image']
    name = escape_string(lines['name'])
    sex = lines['sex']
    birth = escape_string(lines['birth'])
    missing_time = escape_string(lines['missing_time'])
    address = escape_string(lines['address'])
    address_id = lines['address_id']
    if address_id == '':
        address_id="0"
    person = escape_string(lines['person'])
    after = escape_string(lines['after'])
    url = escape_string(lines['url'])

    sql_list = (image, name, sex, birth,
                missing_time, address, address_id, person, after,url,
                image, name, sex, birth,
                missing_time, address, address_id, person, after)

    try:
        cur.execute(sql, sql_list)
        db.commit()
        print("ok url", url, " 次数:", i, end="\r", flush=True)
    except pm.Warning as e:
        print("\n\n", e)
        db.rollback()
        print("\n插入数据失败\n")
print("存储成功")
f.close()
cur.close()
db.close()
