N=int(input())
A=[*map(int,input().split())]
a=c=1
for i in range(1,N):
 if A[i-1]<A[i]:c+=1
 else:a=max(a,c);c=1
print(max(a,c))