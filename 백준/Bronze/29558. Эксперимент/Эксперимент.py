N,D=map(int,input().split())
a=[]
if N%2:print(D,end=" ")
for i in range(1,N//2+1):print(D-i,D+i,end=" ")