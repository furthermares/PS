import sys
input=sys.stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())
inl=lambda:list(map(int,input().split()))
sys.setrecursionlimit(10**6)

N = inp()
W = [None] + inl()
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = inm()
    G[a].append(b)
    G[b].append(a)

dp = [None] + [[0,0] for _ in range(N)]
visited = [None] + [False]*N

def dfs(node):
    visited[node] = True
    
    dp[node][1] += W[node]
    
    for child in G[node]:
        if not visited[child]:
            dfs(child)
            
            dp[node][0] += max(dp[child][0], dp[child][1])
            dp[node][1] += dp[child][0]

dfs(1)

print(max(dp[1]))