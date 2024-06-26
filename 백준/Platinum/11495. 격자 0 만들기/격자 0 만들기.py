input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())
inl=lambda:[*map(int,input().split())]

from collections import deque

def add_edge(u,v,c=1):
    E[u].append(v)
    E[v].append(u)
    C[u][v] = c

def edmonds_karp(s,e):
    max_flow = 0

    while True:
        parent = [-1]*(N*M+2)
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

dx = (1,-1,0,0)
dy = (0,0,1,-1)

for _ in range(inp()):
    N,M = inm()

    E = [[] for _ in range(N*M+2)]
    C = [[0]*(N*M+2) for _ in range(N*M+2)]
    F = [[0]*(N*M+2) for _ in range(N*M+2)]
    s,e = N*M,N*M+1
    G = [inl() for _ in range(N)]

    for x in range(N):
        for y in range(M):
            if (x+y)%2:
                add_edge(s,x*M+y,G[x][y])

                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        add_edge(x*M+y, nx*M+ny, float("inf"))
            else:
                add_edge(x*M+y,e,G[x][y])

    print(sum(map(sum,G)) - edmonds_karp(s,e))