input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

import math

MAX=10001

p=[False]*2+[True]*(MAX-2)

for i in range(2,int(math.sqrt(MAX))):
    for j in range(2,MAX//i):
        p[i*j] = False

f=[0]*MAX
for i in range(1,MAX):
    j=1
    while i*j<MAX:
        f[i*j]+=1
        j+=1

for _ in range(inp()):
    L,H=inm()
    a=[i for i in range(L,H+1) if p[f[i]]]
    print(*a) if a else print(-1)