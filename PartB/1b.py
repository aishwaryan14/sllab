file_content = open("file1.txt","r")
d={}
for i in file_content.read().split():
	if i not in d:
		d[i]=1
	else:
		d[i]=d[i]+1
print(d)
		
