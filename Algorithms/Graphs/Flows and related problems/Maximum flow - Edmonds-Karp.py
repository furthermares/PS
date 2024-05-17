from collections import deque

def add_edge(u,v,c=1):
    E[u].append(v)
    E[v].append(u)
    C[u][v] = c

def edmonds_karp(s,e):
    max_flow = 0
    
    while True:
        parent = [-1]*(N+1)
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

N,M = inm()				# # of nodes, # of edges

E = [[] for _ in range(N+1)] 		# Edges
C = [[0]*(N+1) for _ in range(N+1)]	# Capacity
F = [[0]*(N+1) for _ in range(N+1)]	# Flow
s,e = 1,2				# source, sink

for _ in range(M):
    f,t,b = inm()			# from, to, value
    add_edge(f,t,b)

print(edmonds_karp(s,e))

"""
# Input
5 5 (# of Node, # of Edges)
1 3 1 (from, to, value)
3 2 1
1 5 1
5 4 1
4 2 1

# Output
2
"""
