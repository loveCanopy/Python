__author__ = 'Sherlock'
#encoding=utf-8
import sqlite3
cx=sqlite3.connect("test.sql")
cu=cx.cursor()
cu.execute("create table catalog3 (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname not NULL)")
for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
    cx.execute("insert into catalog3 values (?,?,?,?)", t)
cx.commit()
cu.execute("select * from catalog3")
print(cu.fetchall())