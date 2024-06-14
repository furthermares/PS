from collections import*
N=int(input())
A=list(map(int,input().split()))
for i in range(N):
 while A[i]%2-1:A[i]//=2
print(Counter(A).most_common(1)[0][1])