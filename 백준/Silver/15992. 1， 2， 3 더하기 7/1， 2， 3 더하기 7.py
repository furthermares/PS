import sys
def input(): return sys.stdin.readline().rstrip()

MAX = 1001
MOD = 1000000009

d=[[0]*MAX for _ in range(MAX)]

d[1][1] = 1
d[2][1] = 1
d[2][2] = 1
d[3][1] = 1
d[3][2] = 2
d[3][3] = 1

for i in range(4,MAX):
    for j in range(1,i+1):
        d[i][j] = (d[i-1][j-1] + d[i-2][j-1] + d[i-3][j-1]) % MOD

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    print(d[N][M])