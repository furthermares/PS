import sys
def input(): return sys.stdin.readline().rstrip()
INF = int(1e9)

n, m = map(int,input().split())
graph=[[INF]*(n) for _ in range(n)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a==b:
                graph[a-1][b-1] = 0
            graph[a-1][b-1] = min(graph[a-1][b-1], graph[a-1][k-1] + graph[k-1][b-1])

res = 0
for i in range(n):
    count = 0
    for j in range(n):
        if graph[i-1][j-1] != INF or graph[j-1][i-1] != INF:
            count += 1
    if count == n:
        res += 1

print(res)