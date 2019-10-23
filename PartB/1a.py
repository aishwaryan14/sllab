li=list(map(int,input("Enter the numbers:").split()))
new_li=[]
for i in li:
	if i not in new_li:
		new_li.append(i)
print(new_li)

even_li=[i for i in li if i%2==0]

print(even_li)

print(li[::-1])
