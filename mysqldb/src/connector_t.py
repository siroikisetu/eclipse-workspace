#coding=utf-8
import mysql.connector
from mysql.connector import errorcode

def printstu(cursor):
    #查询数据
    cursor.execute('select * from student where 1=1')
    values = cursor.fetchall()
    for row in values:
        print(row)
try: 
    conn = mysql.connector.connect(user='test', 
                                   password='test', 
                                   database='testdb',
                                   host='127.0.0.1',
                                   port=3306)
    cursor = conn.cursor()
    printstu(cursor)
    #插入数据
    print("插入一条数据")
    addsql="insert into student(stu_id,stu_name) values(%d,'%s')"
    name=input("请输入学生姓名：")
    data=(3,name)
    cursor.execute(addsql % data)
    printstu(cursor)
    
    #更新数据
    print("更新一条数据")
    updsql="update student set stu_name = '%s' where stu_id = %d"
    data=("zhuangyun",3)
    cursor.execute(updsql % data)
    printstu(cursor)
    
    #删除数据
    print("删除一条数据")
    updsql="delete from student where stu_id = %d"
    cursor.execute(updsql % 3)
    printstu(cursor)
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    conn.close()
