import sys
input=sys.stdin.readline
inm=lambda:map(int,input().split())
sys.setrecursionlimit(10**6)

N,K = inm()

MOD = 10007

dp = [[0]*(N+1) for _ in range(N+1)]

def f(n,k):
    if not dp[n][k]:        
        if n == 1 or k in {0,n}:
            dp[n][k] = 1
        else:
            dp[n][k] = f(n-1,k) + f(n-1,k-1)

    dp[n][k] %= MOD
    return dp[n][k]

print(f(N,K))