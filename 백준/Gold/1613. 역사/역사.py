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
                graph[a][b] = 0
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for _ in range(int(input())):
    i, j = map(int,input().split())
    i-=1
    j-=1

    if graph[i][j] == INF and graph[j][i] == INF:
        print(0)
    elif graph[i][j] == INF and not graph[j][i] == INF:
        print(1)
    else:
        print(-1)