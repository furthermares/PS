N,M=map(int,input().split())
h=[0]*N
for i in range(N):
 A=[*map(int,input().split())]
 for j in range(M):
  if A[j]==0:A[j]=-sum(A)
  h[i]+=A[j]*(M-j)
print(h.index(max(h))+1)