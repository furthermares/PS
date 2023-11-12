N,F=map(int,input().split())
A=[[*map(int,input().split())]for _ in range(N)]
a=[0]*N
for i in range(N):a[i]=(F-A[i][0])/A[i][1]
print(a.index(min(a))+1)