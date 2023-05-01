import sys
def input(): return sys.stdin.readline().rstrip()
INF = sys.maxsize

n, m = map(int,input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    edges.append(tuple(map(int,input().split())))

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for cur_node, next_node, edge_cost in edges:
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + edge_cost:
                dist[next_node] = dist[cur_node] + edge_cost
                if i == n - 1:
                    return True
    return False

negative_weight_cycle = bellman_ford(1)

if negative_weight_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])