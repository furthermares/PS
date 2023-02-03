import sys
def input(): return sys.stdin.readline().rstrip()

MOD = int(1e6)

T, A, S, B = map(int,input().split())

N = [0]*201
dp = [[0]*4001 for _ in range(201)]

dp[0][0] = 1

d=list(map(int,input().split()))
for i in d:
    N[i] += 1

for i in range(1,T+1):
    for j in range(1,N[i]+1):
        dp[i][j] += 1

    for j in range(A+1):
        dp[i][j] += dp[i-1][j]

        for k in range(1,N[i]+1):
            if j>k:
                dp[i][j] += dp[i-1][j-k]
                dp[i][j] %= MOD

res = 0
for i in range(S,B+1):
    res += dp[T][i]
    res %= MOD

print(res)