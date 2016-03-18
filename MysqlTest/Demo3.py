import pymysql
con=pymysql.connect(host="localhost",user='root',passwd='root',port=3306)
cur=con.cursor()
cur.execute("create database if not exists python1")
con.select_db("python1")
cur.execute("create table test1(id int,name varchar(20))")
value=[1,'yujie']
cur.execute("insert into test1 values(%s,%s)",value)
values=[]
for i in range(20):
    values.append((i,'yujie'+str(i)))
cur.executemany("insert into test1 values(%s,%s)",values)
con.commit()
con.close()


'''
select *from test1 limit m,n  m从第几行开始  n 显示多少行
'''