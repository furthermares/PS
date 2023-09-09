input=__import__('sys').stdin.readline
inp=lambda:int(input())

MAX = 52

def atoi(ch):
    if ch.isupper():
        return int(ord(ch) - 65)
    else:
        return int(ord(ch) - 97 + 26)

def edmonds_karp(S, T):
    parent = [-1]*len(G)
    max_flow = 0

    def bfs(S, T, parent):
        visited = [False] * len(G)
        q = []
    
        q.append(S)
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

G = [[0]*MAX for _ in range(MAX)]

for _ in range(inp()):
    A, B, F = input().split()
    A = atoi(A); B = atoi(B); F = int(F)

    G[A][B] += F; G[B][A] += F

print(edmonds_karp(atoi("A"), atoi("Z")))