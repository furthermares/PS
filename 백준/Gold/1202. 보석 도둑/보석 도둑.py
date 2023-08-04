input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())
inl=lambda:list(map(int,input().split()))

import heapq

N, K = inm()
MV = [inl() for _ in range(N)]
C = [inp() for _ in range(K)]

MV.sort(); C.sort()

ans = 0
heap = []

for c in C:
    while MV and MV[0][0] <= c:
        heapq.heappush(heap, -MV[0][1])
        heapq.heappop(MV)
    if heap:
        ans -= heapq.heappop(heap)

print(ans)