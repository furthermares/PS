N=int(input())
K,M,m=map(int,input().split())
a=0
for _ in range(N):
 H,_,*L=map(int,input().split())
 for i in L:a+=(i*M<H)|(H*K<i*m)
print(a)