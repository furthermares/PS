import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

for i in sorted(S):
    print(*i)