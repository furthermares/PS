input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

from collections import deque

def solve():
    def edmonds_karp():
        while True:
            q = deque([s])
            parent = [-1]*(N+1)
            while q:
                cur = q.popleft()
                for nxt in E[cur]:
                    if parent[nxt] == -1 and C[cur][nxt] > 0:
                        q.append(nxt)
                        parent[nxt] = cur
                        if nxt == e: break   

            if parent[e] == -1: break

            nxt = e
            maxflow = float("Inf")
            while nxt != s:
                maxflow = min(maxflow, C[parent[nxt]][nxt])
                nxt = parent[nxt]

            nxt = e
            while nxt != s:
                C[parent[nxt]][nxt] -= maxflow
                C[nxt][parent[nxt]] += maxflow
                nxt = parent[nxt]

    for _ in range(inp()):
        N,M = inm()

        E = [[] for _ in range(N+1)]
        Es = []
        C = [[0]*(N+1) for _ in range(N+1)]
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
            if C[s][e] == 0:
                parent = [-1]*(N+1)
    
                q = deque([s])
                while q:
                    cur = q.popleft()
                    for nxt in E[cur]:
                        if parent[nxt] == -1 and C[cur][nxt] > 0:
                            parent[nxt] = cur
                            q.append(nxt)
                            if nxt == e: break
    
                ans += parent[e] == -1

        print(ans)

if __name__ == "__main__": solve()