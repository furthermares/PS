import sys
def input(): return sys.stdin.readline().rstrip()

import heapq

for _ in range(int(input())):
	M = int(input())
	lst = []

	for _ in range(M // 10 + 1):
		lst.extend(list(map(int,input().split())))

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

	print(len(ans))
	for i in range(0, len(ans), 10):
		print(*ans[i:i+10])