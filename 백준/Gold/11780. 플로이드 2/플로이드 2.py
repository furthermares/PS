import sys
def input(): return sys.stdin.readline().rstrip()

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*n for _ in range(n)]
route = [[[]*n for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c
        route[a-1][b-1] = [a,b]

for k in range(n):
    for a in range(n):
        if a == k:
            graph[a-1][k-1] = 0
            route[a-1][k-1] = [0]
        for b in range(n):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                route[a][b] = route[a][k][:-1] + route[k][b]

for a in range(n):
    for b in range(n):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
    
for a in range(n):
    for b in range(n):
        if len(route[a][b]) == 1:
            print(0)
        else:
            print(len(route[a][b]), end=' ')
            print(*route[a][b])