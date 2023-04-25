import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque
INF = sys.maxsize

def dfs(v):
    visited = [False] * N
    q = deque([v])
    while q:
        a = q.pop()
        if a == end:
            return True
        visited[a] = True
        for b, _ in edges[a]:
            if not visited[b]:
                q.append(b)
    return False
    
def bellman_ford(start):
    dist[start] = profit[start]
    for i in range(N+1):
        if i == N and dist[end] == -INF:
            print("gg")
            return
        for S in range(N):
            if dist[S] == -INF:
                continue
            for E, T in edges[S]:
                if dist[E] < dist[S] + T:
                    dist[E] = dist[S] + T
                    if i == N:
                        if dfs(E):
                            print("Gee")
                            return
    print(dist[end])
    return
  
N, start, end, M = map(int,input().split())
edges = [[] for _ in range(N)]
dist = [-INF] * N
for _ in range(M):
    S, E, T = map(int, input().split())
    edges[S].append([E, T])
profit = list(map(int,input().split()))

for i in range(N):
    for j in range(len(edges[i])):
        for k in range(N):
            if edges[i][j][0] == k:
                edges[i][j][1] = profit[k] - edges[i][j][1]
                
bellman_ford(start)