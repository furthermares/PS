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
path = [None] + [[[] for _ in range(2)] for _ in range(N)]

def dfs(node):
    visited[node] = True
    
    dp[node][1] += W[node]
    path[node][1].append(node)
    
    for child in G[node]:
        if not visited[child]:
            dfs(child)
            
            if dp[child][0] > dp[child][1]:
                dp[node][0] += dp[child][0]
                path[node][0] += path[child][0]
            else:
                dp[node][0] += dp[child][1]
                path[node][0] += path[child][1]
            dp[node][1] += dp[child][0]
            path[node][1] += path[child][0]

dfs(1)

idx = 0 if dp[1][0] > dp[1][1] else 1
print(dp[1][idx])
print(*sorted(path[1][idx]))