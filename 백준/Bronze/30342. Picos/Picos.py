N,M,T,K=map(int,input().split())
a=0
while N>0:a+=[0,min(N,M)*K][K>0];N-=M;K-=T
print(a)