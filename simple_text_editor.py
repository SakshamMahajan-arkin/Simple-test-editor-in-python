q=int(input())
string=''
stack=[]
start=-1
for i in range(q):
	value=input().strip().split(' ')
	#print(value[0]+ ' ' +value[1])
	value[0]=int(value[0])
	if (value[0]==1):
		string=string+value[1]
		#print(string+'abc')
		stack.append(string)
	if (value[0]==2):
		value[1]=int(value[1])
		temp=value[1]
		l=len(string)
		temp=l-temp
		string=string[0:temp]
		start=start+1
		stack.append(string)
	if (value[0]==3):
		value[1]=int(value[1])
		temp=value[1]
		temp=temp-1
		print(string[temp])
	if (value[0]==4):
		l=len(stack)
		l=l-1
		string=stack[l-1]
		stack.pop(l)
		start=start-1
	#print(stack)
#Made by Saksham Mahajan
#IIT Bhilai
