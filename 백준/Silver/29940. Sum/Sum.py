N,S=map(int,input().split())
A,a,l,r=[int(input())for _ in[0]*N],0,0,N-1
while l<r:
 s=A[l]+A[r]
 if s==S:a+=1
 if s>=S:r-=1
 if s<=S:l+=1
print(a)