#!/usr/local/bin/python
# Connect to MariaDB Platform
import mysql.connector #mariadb

try:
    #連線DB
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="test"
    )
    #建立執行SQL指令用之cursor, 設定傳回dictionary型態的查詢結果 [{'欄位名':值, ...}, ...]
    cursor=conn.cursor(dictionary=True)
except mysql.connector.Error as e: # mariadb.Error as e:
    print(e)
    print("Error connecting to DB")
    exit(1)


def add(jName,jContent,dDay):
    sql="insert into todolist (jobName,jobContent,dueDate,status) VALUES (%s,%s,%s,%s)"
    param=(jName,jContent,dDay,0)
    cursor.execute(sql,param)
    conn.commit()
    return

def delete(id):
    sql="delete from 表格 where 條件"
    cur.execute(sql,(id,))
    conn.commit()
    return

def setFinish(id):
    sql="update todolist set status=1 where id=%s"
    param=(id,)
    cursor.execute(sql,param)
    conn.commit()
    return

def getList():
    sql="select id,jobName,jobContent,status,dueDate from todolist;"
    #param=('值',...)
    cursor.execute(sql)
    return cursor.fetchall()
