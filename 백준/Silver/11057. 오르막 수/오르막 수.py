input=__import__('sys').stdin.readline
inp=lambda:int(input())

N = inp()

MOD = 10007

dp = [[0] * 10 for _ in range(N+1)]
dp[1] = [1] * 10

for i in range(2,N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1]) % MOD

print(sum(dp[N]) % MOD)