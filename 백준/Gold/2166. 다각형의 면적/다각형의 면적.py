import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
S = [tuple(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    ans += S[i][0] * S[i-1][1] - S[i][1] * S[i-1][0]

print(round(abs(ans/2),1))