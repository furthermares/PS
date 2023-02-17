import sys
def input(): return sys.stdin.readline().rstrip()

import heapq

heapL, heapR = [], []

for _ in range(int(input())):
	n = int(input())
	
	if len(heapL) == len(heapR):
		heapq.heappush(heapL, -n)
	else:
		heapq.heappush(heapR, n)

	if heapR and heapR[0] < -heapL[0]:
		heapq.heappush(heapL, -heapq.heappop(heapR))
		heapq.heappush(heapR, -heapq.heappop(heapL))
	
	print(-heapL[0])
