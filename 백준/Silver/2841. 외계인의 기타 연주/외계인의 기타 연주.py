import sys
def input(): return sys.stdin.readline().rstrip()

from collections import deque

N, _ = map(int,input().split())
dq = [deque() for _ in range(N)]
cnt = 0

for _ in range(N):
	idx, k = map(int,input().split())
	q = dq[idx]
	
	if len(q) == 0:
		q.append(k)
		cnt += 1
	else:
		if q[-1] < k:
			q.append(k)
			cnt += 1
		else:
			while q[-1] > k:
				if q[-1] == k:
					break
				else:
					q.pop()
					cnt += 1
					
					if len(q) == 0:
						break
			if len(q) != 0:
				if q[-1] != k:
					q.append(k)
					cnt += 1
			else:
				q.append(k)
				cnt += 1

print(cnt)