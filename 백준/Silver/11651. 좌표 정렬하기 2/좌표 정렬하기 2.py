import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

for i in sorted(S, key = lambda x: (x[1], x[0])):
    print(*i)