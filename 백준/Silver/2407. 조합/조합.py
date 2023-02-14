import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int,input().split())

ans = 1
for i in range(N-M+1, N+1):
	ans *= i
for i in range(2,M+1):
	ans //= i

print(ans)