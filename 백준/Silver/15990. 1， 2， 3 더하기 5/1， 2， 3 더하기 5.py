import sys
def input(): return sys.stdin.readline().rstrip()

MAX = int(1e5)
MOD = 1000000009

d=[[0]*3 for _ in range(MAX+1)]
d[1] = [1,0,0]
d[2] = [0,1,0]
d[3] = [1,1,1]

for i in range(4,MAX+1):
    d[i][0] = (d[i-1][1] + d[i-1][2]) % MOD
    d[i][1] = (d[i-2][0] + d[i-2][2]) % MOD
    d[i][2] = (d[i-3][0] + d[i-3][1]) % MOD

T = int(input())

for _ in range(T):
    N = int(input())
    print(sum(d[N])%MOD)