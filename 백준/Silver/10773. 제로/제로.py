import sys
input = sys.stdin.readline

from collections import deque

dq = deque()
for _ in range(int(input())):
	n = int(input())
	if n == 0:
		dq.pop()
	else:
		dq.append(n)

print(sum(dq))