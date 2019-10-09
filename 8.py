from functools import reduce
li=[1,3,4,2,6,5]
new_li=[i*3 for i in li]
s1=reduce(lambda x,y:x+y,li)
s2=reduce(lambda x,y:x+y,new_li)
print(s1,s2)
