N=int(input())
A=[*map(int,input().split())]
for _ in range(N-1):A=[abs(A[i]-A[i+1]) for i in range(len(A)-1)]
print(*A)