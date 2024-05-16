input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())
inl=lambda:[*map(int,input().split())]

from collections import deque

def edmonds_karp(s,e):
    max_flow = 0

    while True:
        parent = [-1]*(N+D+2)
        q = deque([s])
        while q:
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

N,K,D = inm()

E = [[] for _ in range(N+D+2)]
C = [[0]*(N+D+2) for _ in range(N+D+2)]
F = [[0]*(N+D+2) for _ in range(N+D+2)]
s,e = 0,N+D+1

for i in range(1,N+1):
    E[s].append(i)
    E[i].append(s)
    C[s][i] = K
Di = inl()
for i in range(D):
    E[N+1+i].append(e)
    E[e].append(N+1+i)
    C[N+1+i][e] = Di[i]
for i in range(1,N+1):
    _,*Zi = inm()
    for Z in Zi:
        E[i].append(N+Z)
        E[N+Z].append(i)
        C[i][N+Z] = 1

print(edmonds_karp(s,e))