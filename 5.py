import sys
import os
from functools import reduce

dict={}

if(len(sys.argv)!=2):
	print("Invalid args")
	sys.exit()
if(not(os.path.exists(sys.argv[1]))):
	print("Invalid file path")
	sys.exit()
if(sys.argv[1].split('.')[-1]!='txt'):
	print("Invalid file format")

#store no of occurrences in each word in a dictionary
filecontent=open(sys.argv[1]).read().split()
for word in filecontent:
	if word in dict:
		dict[word]=dict[word]+1
	else:
		dict[word]=1
print(dict)

#display 10 words with no of occurrences in descending order
s1=[]
s1=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(s1[:10])

#display list of lenghts of each word
word=[]
for i,j in s1[:10]:
	word.append(len(i))
print(word)

#reduce function to find sum and avg
sum=reduce((lambda x,y:x+y),word)
print("Sum is:",sum)
avg=sum/len(word)
print("Avg is:",avg)

#list comprehension to find odd length sqaures
sq_odd=[i*i for i in word if i%2!=0]
print("The square of odd nos:",sq_odd)			
	
