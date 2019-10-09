s=input("Enter a string")
flag=1
for i in range(0,int(len(s)/2)):
	if s[i]!=s[-(i+1)]:
		flag=0
		break
if flag==0:
	print("Not a palindrome")
else:
	print("palindrome")

