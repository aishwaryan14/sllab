li = ["The2","darkest1","ho6ur","200a9"]
for i in range(0,len(li)):
	if i%2==0:
		print(li[i])

print("\n")

for i in range(0,len(li)):
	if i%3==0:
		li[i]=li[i].upper()
print(li)
print("\n")

for i in range(0,len(li)):
	li[i]=li[i][::-1]
print(li)
print("\n")


num_li=[]
for l in li:
	for i in l:
		if i.isdigit():
			num_li.append(i)
print(num_li)
