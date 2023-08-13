import sys
input=sys.stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

sys.setrecursionlimit(10**6)

N = inp()
T = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = inm()
    T[u].append(v)
    T[v].append(u)

dp = [None] + [[0,1] for _ in range(N)]
visited = [None] + [False] * N
visited[1] = True

def dfs(root):
    for leaf in T[root]:
        if not visited[leaf]:
            visited[leaf] = True  
            dfs(leaf)
            dp[root][0] += dp[leaf][1]
            dp[root][1] += min(dp[leaf])

dfs(1)

print(min(dp[1]))