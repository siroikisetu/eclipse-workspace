#coding=utf-8
import os
import pymysql

#打开数据库连接
db = pymysql.connect(host="127.0.0.1",
                     port=3306,
                     user="test",
                     password="test",
                     db="testdb"
                     )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT * from student")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()

os.system("pause")