import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
S = set([input() for _ in range(N)])

cnt = 0
for _ in range(M):
	T = input()
	if T in S:
		cnt += 1

print(cnt)