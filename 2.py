def kelvintocelcius(K):
	return K-273.15	
def celciustokelvin(C):
	return C+273.15
def fahrenheittocelcius(F):
	return (F-32)*5/9
def celciustofahrenheit(C):
	return (9/5)*C+32

print("Enter 1:Kelvin to Celcius\nEnter 2:Celcius to Kelvin\n Enter 3:Fahrenheit to Celcius\nEnter 4:Celcius to fahrenheit\nEnter 5:Display the conversions\nEnter -1:Exit")

li=[]

while(True):
	c=int(input("Enter your choice:"))
	if c==1:
		K=float(input("Enter the temp in Kelvin:"))
		C=kelvintocelcius(K)
		print("The temperature in Celcius:{}".format(C))
		li.append((K,C))
	elif c==2:
		C=float(input("Enter the temp in Celcius:"))
		K=celciustokelvin(C)
		print("The temperature in Kelvin:{}".format(K))
		li.append((C,K))
	elif c==3:
		F=float(input("Enter the temp in Fahrenheit:"))
		C=fahrenheittocelcius(F)
		print("The temperature in Celcius:{}".format(C))
		li.append((F,C))
	elif c==4:
		C=float(input("Enter the temp in Celcius:"))
		F=celciustofahrenheit(F)
		print("The temperature in Fahrenheit:{}".format(F))
		li.append((C,F))
	elif c==5:
		print("Viewing conversions...:")
		print(li)
	elif c==-1:
		break
	else:
		pass



	
