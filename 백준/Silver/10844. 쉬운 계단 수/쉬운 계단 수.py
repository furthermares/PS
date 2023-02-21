import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
MOD = int(1e9)

dp = [[1] * 10 for _ in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % MOD
    dp[i][9] = dp[i-1][8]

print(sum(dp[N-1]) % MOD)