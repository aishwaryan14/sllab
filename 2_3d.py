li=[1,2,3,4,5]
with open("text.txt","w") as myfile:
	for c in li:
		myfile.write("%s"%c)
file_content = open("text.txt","r")
print(file_content.read())
