N,M=map(int,input().split())
A,l,r,a=[0]+[int(input())for _ in[0]*N],1,1,1e9
for i in range(1,N+1):A[i]+=A[i-1]
while l<=r and r<=N:
 if A[r]-A[l-1]>=M:a=min(a,r-l+1);l+=1
 else:r+=1
print(a if a!=1e9else"NEPAVYKS")