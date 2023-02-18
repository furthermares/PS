import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
S = [list(input().split()) for _ in range(N)]

ans = sorted(S, key = lambda x: int(x[0]))
for i in ans:
    print(*i)