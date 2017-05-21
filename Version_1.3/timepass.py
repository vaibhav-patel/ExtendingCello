from math import *
import random
n=45
arr=[]
for i in range(1,10):
	arr.append(i)
flag=True
ans=arr[0]
while(flag):
	solution=[]
	ans=arr[0]
	for  i in range(2,10):
		x=random.randint(1,4)
		if(x==1):
			solution.append(' + ')
			ans=ans+i
		if(x==2):
			solution.append(' - ')
			ans=ans-i
		if(x==3):
			solution.append(' * ')
			ans=ans*i
		if(x==4):
			solution.append(' / ')
			ans=float(ans)/float(i)
		print ans
		if(int(ans)==n):
			break

str1=''
for i in range(1,9):
	str1=str1+str(i)+solution[i-1]
str1=str1+'9'
print str1
#		ans= ans 









