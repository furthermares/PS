N=int(input())
A=[*map(int,input().split())]
for i in range(N):
 if A[i]*2==sum(A):exit(print(i+1))