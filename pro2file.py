from itertools import combinations
a,s=map(int,input().split())
h=len(str(a))
l=list(combinations(str(a),h-s))
l=sorted(l)
print("".join(l[0]))
