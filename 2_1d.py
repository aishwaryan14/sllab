n=int(input("Enter n"))
file_content = open("file1d.txt","r")
for i in file_content.readlines()[-5:]:
	print(i)
