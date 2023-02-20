import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int,input().split()))

ans = 0
for j in range(-99,100):
    dp = [0] * (101)
    for i in range(N):
        if(A[i] - j < 1 or A[i] - j > 100):
            dp[A[i]] = 1
        else:
            dp[A[i]] = dp[A[i] - j] + 1

        ans = max(ans, dp[A[i]])

print(ans)