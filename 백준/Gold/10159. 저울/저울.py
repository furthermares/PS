import sys
def input(): return sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input())
m = int(input())
graph=[[INF]*(n) for _ in range(n)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a==b:
                graph[a][b] = 0
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    count = n
    for j in range(n):
        if graph[i][j] != INF or graph[j][i] != INF:
            count -= 1
    print(count)