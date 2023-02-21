import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())

MOD = 15746
dp = [1,1]

for i in range(2,N+1):
    dp.append((dp[i-1] + dp[i-2]) % MOD)

print(dp[-1] % MOD)