import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
S = []
T = []

for _ in range(N):
	S.append(input())
for _ in range(M):
	T.append(input())

cnt = 0
for i in T:
	if i in S:
		cnt += 1

print(cnt)