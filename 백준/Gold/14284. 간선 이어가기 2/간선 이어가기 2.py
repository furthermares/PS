import sys
def input(): return sys.stdin.readline().rstrip()
INF = int(1e9)
import heapq

n, m = map(int,input().split())
graph=[[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance=[INF]*(n+1)

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

start, end = map(int,input().split())
dijkstra(start)
print(distance[end])