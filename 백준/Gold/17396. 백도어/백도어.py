import sys
def input(): return sys.stdin.readline().rstrip()
INF = int(1e10)+1
import heapq

n, m = map(int,input().split())
graph=[[]*(n) for _ in range(n)]

blockade=list(map(int,input().split()))
blockade[-1] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    if blockade[a] == 0 and blockade[b] == 0:
        graph[a].append((b,c))
        graph[b].append((a,c))
distance=[INF]*(n)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[0] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

start, end = 0, n-1
dijkstra(start)

ans = distance[end]
if ans == INF:
    print(-1)
else:
    print(distance[end])