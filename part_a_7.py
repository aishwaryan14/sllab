def Atomic_dict():
	sym=input("Enter the symbol")
	name=input("Enter the name")
	return sym,name
atomic={'H':'Hydrogen','He':'Helium','Li':'Lithium','Be':'Berelium','B':'Boron'}
s1,n1=Atomic_dict()
atomic[s1]=n1
s2,n2=Atomic_dict()
atomic[s2]=n2

print(atomic)

s=input("Enter element to serch:")
print(atomic[s])
