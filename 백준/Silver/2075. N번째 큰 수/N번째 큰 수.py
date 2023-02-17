import sys
def input(): return sys.stdin.readline().rstrip()

import heapq

N = int(input())

lst = list(map(int,input().split()))
heapq.heapify(lst)

for _ in range(N-1):
	for i in map(int,input().split()):
		heapq.heappush(lst, i)
		heapq.heappop(lst)

print(lst[0])