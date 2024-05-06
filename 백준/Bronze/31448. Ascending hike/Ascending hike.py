N=int(input())
A=[*map(int,input().split())]
m=c=0
for i in range(1,N):
 t=A[i]-A[i-1]
 if t>0:c+=t;m=max(m,c)
 else:c=0
print(m)