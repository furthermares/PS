import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())

ans = 0
row = [0]*N

def chk(x):
	for i in range(x):
		if row[i] == row[x] or abs(row[i] - row[x]) == abs(x - i):
			return False
	return True

def dfs(x):
	global ans
	if x == N:
		ans += 1

	else:
		for i in range(N):
			row[x] = i
			if chk(x):
				dfs(x + 1)

dfs(0)
print(ans)