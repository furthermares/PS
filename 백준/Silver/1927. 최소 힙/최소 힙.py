import sys
def input(): return sys.stdin.readline().rstrip()

import heapq
heap=[]

N = int(input())
for i in range(N):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,x)