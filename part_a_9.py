class Student:
	def __init__(self,name,age,marks):
		self.name=name
		self.age=age
		self.marks=marks
	def display(self):
		print(self.name)
		print(self.age)
		print(self.marks)
ob1=Student("John",22,[22,25,28])
ob2=Student("Raju",22,[23,24,30])
ob1.display()
ob2.display()		
