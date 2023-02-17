import sys
def input(): return sys.stdin.readline().rstrip()

import heapq

lst = []

for _ in range(int(input())):
	lst.append(int(input()))

heapL, heapR = [], []
middle = lst[0]
ans = [middle]

for idx, val in enumerate(lst[1:], 1):
	if val > middle:
		heapq.heappush(heapR, val)
	else:
		heapq.heappush(heapL, -val)

	if idx % 2 == 0:
		if len(heapL) < len(heapR):
			heapq.heappush(heapL, -middle)
			middle = heapq.heappop(heapR)
		elif len(heapL) > len(heapR):
			heapq.heappush(heapR, middle)
			middle = -heapq.heappop(heapL)
		ans.append(middle)
	else:
		if len(heapL) < len(heapR):
			ans.append(middle)
		else:
			ans.append(-heapL[0])

print(*ans, sep="\n")