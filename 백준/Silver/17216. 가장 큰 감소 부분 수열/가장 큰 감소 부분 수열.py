import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int,input().split()))
A = A[::-1]
dp = A[:]

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))