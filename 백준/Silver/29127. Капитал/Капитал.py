A,N=map(int,input().split())
if A>N*9:print(-1);exit()
for _ in[0]*N:t=min(A,9);print(t,end="");A-=t