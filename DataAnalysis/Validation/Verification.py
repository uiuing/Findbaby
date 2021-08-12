import pymysql as pm
from pymysql.converters import escape_string
import random

db = pm.connect(
    host='43.129.74.180',user='FindBaby',password='pisX7XmWMc3WjcwK',
    db='findbaby',port=5743,charset='utf8'
)
cur = db.cursor()


success_2 = 0
fails_2 = 0
success_4 = 0
fails_4 = 0
success_6 = 0
fails_6 = 0

all_file_size = 0

n_size = 6

probability = list()
correspond_value = list()

success_value = list()
size_all = int(input("\n\n\n请一次性输入的数据流大小: "))

for line in open("DataAnalysis/Validation/Validation_set",'r',encoding='utf-8'):

    all_file_size += 1    

    ins,ous = line.split("\t",1)
    ins = ins.strip()
    ous = ous.strip()
    
    while len(probability) < size_all:
        probability.clear()
        correspond_value.clear()
        sql = "select pb,outs from pb where input like \'"+str(ins[0:n_size])+"%\';"
        n_size = n_size - 1
        try:
            cur.execute(sql)
            selects = cur.fetchall()
            for row in selects:
                probability.append(row[0])
                correspond_value.append(row[1])
            db.commit()
            
        except  pm.Warning as e:
            print ("\n\n",e)
            db.rollback()
            print("\n失败\n")

    while len(success_value) != size_all:
        random_value = random.uniform(0.000,0.001)
        index = random.randint(0,len(probability)-1)
        if (random_value < float(probability[index])):
            success_value.append(correspond_value[index])
            correspond_value.pop(index)
            probability.pop(index)
    ram_flag_success_2 = success_2
    ram_flag_success_4 = success_4
    ram_flag_success_6 = success_6

    s1 = 0
    s2 = 0
    s3 = 0

    for value in success_value:
        if int(ous) == value and s1 == 0:
            success_6 += 1
            s1 = 1
        if int(ous[0:4]) == int(str(value)[0:4]) and s2 == 0:
            success_4 += 1
            s2 = 1
        if int(ous[0:2]) == int(str(value)[0:2]) and s3 == 0:
            success_2 += 1
            s3 = 1
        if s1 == 1 and s2 == 1 and s3 == 1:
            break
    if(ram_flag_success_2 == success_2):
        fails_2 += 1
    if(ram_flag_success_4 == success_4):
        fails_4 += 1
    if(ram_flag_success_6 == success_6):
        fails_6 += 1
    probability.clear()
    correspond_value.clear()
    success_value.clear()

print("------------------验证集计算结果------------------")
print("数据大小: ",all_file_size)
print("\n省级区域内准确率\n\t%.8f" % (success_2/(success_2+fails_2)))
print("市级区域内准确率\n\t%.8f" % (success_4/(success_4+fails_4)))
print("县级区域内准确率\n\t%.8f" % (success_6/(success_6+fails_6)))
print("------------------------------------------------\n\n")

cur.close()
db.close()
