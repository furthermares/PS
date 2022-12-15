import sys
def input(): return sys.stdin.readline().rstrip()

import heapq
heap=[]

N = int(input())
for i in range(N):
    x = int(input())
    x = (abs(x), True if x>=0 else False)
    #print(x)
    if x[0] == 0:
        if len(heap) == 0:
            print(0)
        else:
            s = heapq.heappop(heap)
            #print(s)
            if s[1]: print(s[0])
            else: print(-s[0])
    else:
        heapq.heappush(heap,x)