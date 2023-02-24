import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [0] * (N+1)

def dfs(s):
    for i in G[s]:
        if not visited[i]:
            visited[i] = s
            dfs(i)

dfs(1)

for i in range(2,N+1):
    print(visited[i])