__author__ = 'Sherlock'
import pymysql
con=pymysql.connect(host="localhost",user='root',passwd='root',port=3306)
cur=con.cursor()
cur.execute("create database if not exists pythonTest1")
con.select_db("pythonTest1")
cur.execute("create table test3(id int AUTO_INCREMENT,primary key(id),name varchar(10),age int)")
values=[]
for i in range(10):
    values.append(("yujie"+str(i),10+i))
cur.executemany("insert into test3 values(Null,%s,%s)",values)
con.commit()
cur.close()
con.close()