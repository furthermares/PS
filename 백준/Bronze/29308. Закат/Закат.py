m=(-1,"_")
for _ in[0]*int(input()):
 N,B,C=input().split()
 if C=="Russia":m=max(m,(int(N),B))
print(m[1])