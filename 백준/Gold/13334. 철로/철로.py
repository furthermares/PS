input=__import__('sys').stdin.readline
inp=lambda:int(input())
inl=lambda:[*map(int,input().split())]

import heapq

HO=sorted([sorted(inl())for _ in range(inp())],key=lambda x:(x[1],x[0]))
D=inp()

heap=[]
m=0

for H,O in HO:
    heapq.heappush(heap,H)
    while heap and heap[0] < O-D:
        heapq.heappop(heap)
    m=max(m,len(heap))
print(m)