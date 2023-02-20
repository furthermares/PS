import sys
def input(): return sys.stdin.readline().rstrip()

import bisect

N = int(input())
A = [0] + list(map(int,input().split()))
A = [-i for i in A]
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