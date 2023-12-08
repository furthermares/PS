input=__import__('sys').stdin.readline
inp=lambda:int(input())

import math

N=inp()

V=[0]*(N+1)
for i in range(1,N//2+1):
    V[i*2-1] = N//2 + i
    V[i*2] = i

visited=[False]*(N+1)

ans = 1
for i in range(1,N+1):
    if visited[i]:
        continue

    loop=0
    
    t=i
    while not visited[t]:
        visited[t] = True
        t=V[t]
        loop+=1

    ans *= loop // math.gcd(ans, loop)

print(ans)