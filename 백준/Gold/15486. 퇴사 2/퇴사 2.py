import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
T=[]
P=[]
for _ in range(N):
    x, y = map(int,input().split())
    T.append(x)
    P.append(y)
dp = [0]*(N+1)

max_value=0
for i in range(N-1,-1,-1):
    if T[i] + i <= N:
        dp[i] = max(P[i]+dp[T[i]+i],max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)