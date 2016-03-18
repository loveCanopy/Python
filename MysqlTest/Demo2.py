from imp import reload

__author__ = 'Sherlock'
#encoding=utf-8
import  pymysql
con=pymysql.Connect(host='127.0.0.1',user='root',passwd='root',db='contact')
cur=con.cursor()
sql="insert into contactlist values(13,'yujie13',24,'798889080')"
sql1="create table catalog5(id int,pid int,name varchar(10),nickname varchar(10))"
sql2="insert into catalog5(id,pid,name,nickname)values(1,1,'yujie','man')"
# cur.execute(sql)
cur.execute("select *from contactlist")
cur.execute(sql1)
cur.execute(sql2)
cur.execute("select *from catalog5")
print(cur.fetchall())
con.commit()
con.close()


