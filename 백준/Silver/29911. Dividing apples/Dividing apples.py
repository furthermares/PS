import sys
I=sys.stdin.readline
N=int(I())
K=[0]+[int(I())for _ in[0]*N]
s=sum(K)/2
mn=float('inf')
for i in range(1,N+1):
 K[i]+=K[i-1]
 if abs(K[i]-s)<=mn:mn=abs(K[i]-s)
 else:print(i-1);break
else:print(i)