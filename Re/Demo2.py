import re
#|选择符
p=re.compile(r'fish[c|d]')
q=p.match('fishd')
print(q.group())
#^$开始符和结束符
p1=re.compile(r"^hel")
q1=p1.search('hello')
print(q1.group())
p2=re.compile(r'fishc$')
q2=p2.search("lovefishc")
print(q2.group())
#\的使用
q3=re.search(r'(fish)\1','fishfishfish')  #(fish)\1相当于fishfish
print(q3.group())


q4=re.search(r'(fish)\060','fish0')  #\后面加三位数 为八进制表示  060对应0的ASCII码
print(q4.group())

q5=re.search(r'(fish)\141','fisha')#141 对应的97  即a
print(q5.group())

#[]
q6=re.search(r'[.]','fish.com')
print(q6.group())