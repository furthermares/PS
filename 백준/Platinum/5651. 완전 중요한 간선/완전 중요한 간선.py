input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

from collections import deque

def solve():
    def edmonds_karp():
        while True:
            parent = [-1]*(N+1)
            q = deque([s])
            while q:
                cur = q.popleft()
                for nxt in E[cur]:
                    if C[cur][nxt] - F[cur][nxt] > 0 and parent[nxt] == -1:
                        parent[nxt] = cur
                        if nxt == e: break
                        q.append(nxt)  
    
            if parent[e] == -1: break
    
            cur = e
            maxflow = float("Inf")
            while cur != s:
                maxflow = min(maxflow, C[parent[cur]][cur] - F[parent[cur]][cur])
                cur = parent[cur]
    
            cur = e
            while cur != s:
                F[parent[cur]][cur] += maxflow
                F[cur][parent[cur]] -= maxflow
                cur = parent[cur]
    
    for _ in range(inp()):
        N,M = inm()
    
        E = [[] for _ in range(N+1)]
        Es = []
        C = [[0]*(N+1) for _ in range(N+1)]
        F = [[0]*(N+1) for _ in range(N+1)]
        s,e = 1,N
    
        for _ in range(M):
            f,t,b = inm()
            E[f].append(t)
            E[t].append(f)
            Es.append((f,t))
            C[f][t] += b
    
        edmonds_karp()
    
        ans = 0
        for s, e in Es:
            if C[s][e] - F[s][e] == 0:
                parent = [-1]*(N+1)
                q = deque([s])
                while q:
                    cur = q.popleft()
                    for nxt in E[cur]:
                        if C[cur][nxt] - F[cur][nxt] > 0 and parent[nxt] == -1:
                            parent[nxt] = cur
                            if nxt == e: break
                            q.append(nxt)
        
                ans += parent[e] == -1
    
        print(ans)
    
if __name__ == "__main__": solve()