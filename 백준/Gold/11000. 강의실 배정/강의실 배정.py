import sys
def input(): return sys.stdin.readline().rstrip()

import heapq

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]
S.sort()

heap = []
heapq.heappush(heap, S[0][1])

for i in range(1,N):
    if S[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, S[i][1])
    
print(len(heap))