with open("f1.txt","r") as f1:
	with open("f2.txt","w") as f2:
		for l in f1:
			f2.write(l)
print(open("f2.txt").read())
