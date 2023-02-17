import sys
def input(): return sys.stdin.readline().rstrip()

from collections import deque

N, _ = map(int,input().split())
dq = [deque([0]) for _ in range(N)]
cnt = 0

for _ in range(N):
	idx, k = map(int,input().split())
	q = dq[idx]

	while q[-1] > k:
		q.pop()
		cnt += 1

	if q[-1] == k:
		continue

	q.append(k)
	cnt += 1

print(cnt)
