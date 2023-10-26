A=[[None] for _ in range(1000)]
for _ in range(int(input())):
 T,N=map(int,input().split())
 A[N].append(T)
 if len(A[N])==3:print(N,A[N][2]-A[N][1])