class Student(dict):
	def __init__(self):	
		self=dict()
	def add(self,key,value):
		self[key]=value
obj=Student()
obj.add(1,"Raju")
obj.add(2,"Ravi")
obj.add(3,"Reema")
obj.add(4,"Seema")
obj.add(5,"Lata")
obj.add(6,"Lauen")

for key in obj.keys():
	if key%2==0:
		print(obj[key])
