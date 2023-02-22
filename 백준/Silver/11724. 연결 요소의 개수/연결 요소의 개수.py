import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e6))

N, M = map(int,input().split())

graph=[[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort()

visited = [False] * (N+1)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)