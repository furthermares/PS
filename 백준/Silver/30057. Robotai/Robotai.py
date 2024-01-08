M,L,S=map(int,input().split())
P,l,r,a=[0]+[int(input())for _ in[0]*M]+[L],[0]*(M+2),[0]*(M+2),0
for i in range(1,M+1):l[i]=l[i-1]+P[i]-P[i-1]+S
for i in range(M,0,-1):r[i]=r[i+1]+P[i+1]-P[i]+S
for i in range(1,M+1):a=max(a,min(l[i],r[i]))
print(a)