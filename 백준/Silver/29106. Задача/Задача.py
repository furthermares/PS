input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())
inl=lambda:[*map(int,input().split())]

N,K=inm()
A=inl()
A.sort()
l=0
a=l
while l<N-K+1:
    if A[l+K-1]-A[l]<A[a+K-1]-A[a]:
        a=l
    l+=1
print(*A[a:a+K])