import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int,input().split()))

dp = [0] * N
dp1 = [1] * N
dp2 = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)

A.reverse()

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)

for i in range(N):
    dp[i] = dp1[i] + dp2[N-i-1]
print(max(dp)-1)