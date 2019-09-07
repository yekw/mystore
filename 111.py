import pymysql
import time

conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)

gettime = "select * from reader"
cursor.execute(gettime)
a = cursor.fetchone()
b = int(a[3])
print(type(b))
print(b)

# if a[3]>0:
#     print(111)