import sys
def input(): return sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input())
graph=[[INF]*(n) for _ in range(n)]
while(True):
    a, b = map(int,input().split())
    if a==-1 and b==-1:
        break
    graph[a-1][b-1] = graph[b-1][a-1] = 1
    
for k in range(n):
    for a in range(n):
        for b in range(n):
            if a==b:
                graph[a][b] = 0
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

score=[]
for k in range(n):
    tmp = -1
    for i in range(n):
        if graph[k][i] == 0 or graph[k][i] == INF:
            continue
        tmp = max(graph[k][i], tmp)
    score.append(tmp)

min_score = min(score)
print(min_score, score.count(min_score))
print(*[i+1 for i, x in enumerate(score) if x == min_score], sep=" ")