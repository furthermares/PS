# Number of balanced sequences
from math import factorial as fact
MOD = int(1e9)+7

def catalan(n):
    return fact(2*n) // (fact(n) * fact(n+1))

L = int(input())

if L & 1:
    print(0)
else:
    print(catalan(L//2) % MOD)

# Finding the k-th sequence
N,K = map(int,input().split())
N //= 2
K += 1

dp = [[0]*(N+2) for _ in range(N+2)]
dp[1][0] = 1

for i in range(1, N+2):
    for j in range(i, N+2):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

x = N
y = N+1
ans = ""
if K > dp[x][y]:
    ans = "-1"
else:
    while y > 1:
        if K <= dp[x][y]:
            ans += "("
            x -= 1
        else:
            ans += ")"
            K -= dp[x][y]
            y -= 1
            
print(ans)
