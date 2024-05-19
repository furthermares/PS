input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())

from collections import deque

def add_edge(u,v,c=1):
    E[u].append(v)
    E[v].append(u)
    C[u][v] = c

def edmonds_karp(s,e):
    max_flow = 0

    while True:
        parent = [-1]*(MAX)
        q = deque([s])
        while q and parent[e] == -1:
            cur = q.popleft()
            for nxt in E[cur]:
                if C[cur][nxt] - F[cur][nxt] > 0 and parent[nxt] == -1:
                    parent[nxt] = cur
                    if nxt == e: break
                    q.append(nxt)  
        if parent[e] == -1: break

        path_flow = float("Inf")
        i = e
        while i != s:
            path_flow = min(path_flow, C[parent[i]][i] - F[parent[i]][i])
            i = parent[i]
        max_flow += path_flow

        i = e
        while i != s:
            F[parent[i]][i] += path_flow
            F[i][parent[i]] -= path_flow
            i = parent[i]

    return max_flow

N,M = inm()
MAX = N+M+2
E = [[] for _ in range(MAX)]
C = [[0]*(MAX) for _ in range(MAX)]
F = [[0]*(MAX) for _ in range(MAX)]
s,e = 0,MAX-1

for i in range(1,N+1):
    add_edge(s,i)
    _,*Si = inm()
    for S in Si:
        add_edge(i,N+S)

for i in range(1,M+1):
    add_edge(N+i,e)

print(edmonds_karp(s,e))