li=list(map(int,input("Enter numbers:").split()))
def rec(li,n):
	if n==0:
		return li[0]
	return max(li[n-1],rec(li,n-1))
print(rec(li,len(li)))
