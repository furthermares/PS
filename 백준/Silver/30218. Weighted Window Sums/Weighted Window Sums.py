input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

N,K=inm()

A=[inp() for _ in range(N)]

v=[0]*(N+1)
for i in range(1,N+1):v[i]=v[i-1]+A[i-1]
u=[0]*(N+1)
for i in range(1,N+1):u[i]=u[i-1]+A[i-1]*i

w=[(u[i+K]-u[i] - (v[i+K]-v[i])*i, i) for i in range(N-K+1)]

w.sort()

for i in range(len(w)):
    print(w[i][1]+1,w[i][0])