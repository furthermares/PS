input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())

MAX_N = 400 + 1

def edmonds_karp(S, T):
    parent = [-1] * len(G)
    max_flow = 0

    def bfs(S, T, parent):
        visited = [False] * len(G)
        q = [S]
        visited[S] = True
    
        while q:
            u = q.pop(0)
            for idx, val in enumerate(G[u]):
                if not visited[idx] and val > 0:
                    q.append(idx)
                    visited[idx] = True
                    parent[idx] = u
                    if idx == T:
                        return True
    
        return False
    
    while bfs(S, T, parent):
        path_flow = float("Inf")
        
        s = T
        while(s != S):
            path_flow = min(path_flow, G[parent[s]][s])
            s = parent[s]
        max_flow += path_flow

        v = T
        while(v != S):
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]

    return max_flow

G = [[0]*MAX_N*2 for _ in range(MAX_N*2)]
for i in range(2, MAX_N*2, 2):
    G[i][i+1] = 1
    G[i+1][i] = -1

N, P = inm()
for _ in range(P):
    A, B = inm()

    G[A*2+1][B*2] += 1
    G[B*2+1][A*2] += 1

print(edmonds_karp(1*2+1,2*2))