N,M=map(int,input().split())
b=0
for _ in range(5):n,m=map(int,input().split());    b=max(b,n+m*10)
print(max(0,b-N-M*10+1))