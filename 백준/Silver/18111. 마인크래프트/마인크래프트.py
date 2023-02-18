import sys
def input(): return sys.stdin.readline().rstrip()

MAX = sys.maxsize

N, M, B = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = MAX

for h in range(257):
	ub, tb = 0, 0
	
	for i in range(N):
		for j in range(M):
			cb = arr[i][j]
			if cb > h:
				tb += cb - h
			else:
				ub += h - cb
	if ub > tb + B:
		continue
	
	cnt = tb * 2 + ub

	if cnt <= ans:
		ans = cnt
		height = h

print(ans, height)