N=int(input())
A=[]
while len(A) < N:
 A.extend(list(map(int,input().split())))
s=sum(A)
print((s-min(a for a in A if a&1))>>1 if s&1 else s>>1)