import sys
def input(): return sys.stdin.readline().rstrip()

import bisect

N = int(input())
A = [0] + list(map(int,input().split()))
dp = [0] * (N+1)

Ai = [-sys.maxsize - 1]

for i in range(1,N+1):
    if A[i] > Ai[-1]:
        Ai.append(A[i])
        dp[i] = len(Ai) - 1
    else:
        dp[i] = bisect.bisect_left(Ai, A[i])
        Ai[dp[i]] = A[i]

print(len(Ai)-1)

max_idx = max(dp)
ans = []
for i in range(N,0,-1):
    if dp[i] == max_idx:
        ans.append(A[i])
        max_idx = dp[i] - 1

print(*reversed(ans))