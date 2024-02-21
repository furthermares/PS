I=lambda:map(int,input().split())
N,K=I()
A=sorted(I())
l=x=0
while l<N-K+1:
 if A[l+K-1]-A[l]<A[x+K-1]-A[x]:x=l
 l+=1
print(*A[x:x+K])