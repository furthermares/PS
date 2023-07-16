input = __import__('sys').stdin.readline
inm = lambda: map(int,input().split())
inl = lambda: list(map(int,input().split()))

import heapq

N,M = inm()
A = inl()

heapq.heapify(A)

for _ in range(M):
    t = heapq.heappop(A) + heapq.heappop(A)
    heapq.heappush(A, t)
    heapq.heappush(A, t)

print(sum(A))