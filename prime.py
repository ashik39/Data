z=int(raw_input())
temp=z
flag=0
if(z<0):
	print("negative numbers cannot be prime")
elif(z==0):
	print("not a prime")
else:
	for x in xrange(1,z+1):
		if(z%x==0):
			flag=flag+1

          
	if(flag==2):
		print("yes")
	else:
		print("no")
