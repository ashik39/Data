try:
	q=0
	n=str(raw_input())
	a=[]
	m=str()
	for i in range (0,len(n)):
		a.append(n[i])
	if len(n)%2==0:
		j=len(n)
	else:
		j=len(n)-1
	while(q!=j):
		t=a[q]
		a[q]=a[q+1]
		a[q+1]=t
		q=q+2
	for i in range (0,len(a)):
		m=m+a[i]
	print m
except:
	print "Invalid"
