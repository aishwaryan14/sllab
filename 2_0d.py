strings="and could wood chuck chuck wood?"
with open("file0d.txt","a") as myfile:
	for c in strings:
		myfile.write("%s"%c)
file_cont=open("file0d.txt","r")
print(file_cont.read())
