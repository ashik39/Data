#ashik ali
m=int(input())
x=[]
b=[]
c=0
for i in range(m):
    s=raw_input()
    x.append(s)
for j in range(len(min(x))):
    for i in range(m):
        if i<m-1:
            if x[i][j]==x[i+1][j]:
               c+=1
            i-=1
    if c==m-1:
         b.append(x[i][j])
    else:
         break
    c=0                    
if b:
    print ''.join(b)
else:
    print "No matches"
