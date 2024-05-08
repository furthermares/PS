input=__import__('sys').stdin.readline
inp=lambda:int(input())
inl=lambda:[*map(int,input().split())]

N=inp()
X=inl()
sieve=[0]*1000001
s=set(X)
m=max(X)
for i in X:
    if i==m: continue
    for j in range(i*2,m+1,i):
        if j in s:
            sieve[i]+=1
            sieve[j]-=1
for i in X:print(sieve[i],end=" ")