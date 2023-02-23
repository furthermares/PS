import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

N, M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N):
    graph[i].sort()

ans = False

visited = [False] * (N)
def dfs(v, depth):
    global ans
    if depth == 4:
        ans = True
        return
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth + 1)
            visited[i] = False
            
for i in range(N):
    if not visited[i]:
        dfs(i, 0)
        visited[i] = False
        if ans:
            break

if ans:
    print(1)
else:
    print(0)