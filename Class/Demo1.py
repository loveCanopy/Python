class Person:
	def __init__(self,name,sex,nationlity,age,job):
		self.name=name
		self.sex=sex
		self.nationlity=nationlity 
		self.age=age 
		self.job=job
	def talk(self,msg=0):
		if msg!=0:
			print("hello %s,you are from %s,%s years old,your job is %s" %(self.name,self.nationlity,self.age,self.job))
person=Person("yujie","man","CN",'25',"student")
person.talk(1)


class Student(Person):
	def __init__(self,name,sex,nationlity,age,job):
		# super().__init__(name,sex,nationlity,age,job)
		Person.__init__(self,name,sex,nationlity,age,job)
s=Student("yujie1","man","CN",'25',"student")
s.talk(1)



