import sys
def input(): return sys.stdin.readline().rstrip()

from math import gcd

MOD = 10000003

N = [0]*101
dp = [[0]*100001 for _ in range(101)]

n_len = int(input())
for i in range(n_len):
    N[i] = int(input())
    dp[i][N[i]] = 1

for i in range(1,n_len+1):
    for j in range(1,100001):
        dp[i][j] += dp[i-1][j]
        dp[i][j] %= MOD

        t = gcd(N[i],j)
        dp[i][t] += dp[i-1][j]
        dp[i][t] %= MOD

print(dp[n_len-1][1])