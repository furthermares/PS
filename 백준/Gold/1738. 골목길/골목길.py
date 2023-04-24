import sys
def input(): return sys.stdin.readline().rstrip()
INF = sys.maxsize

n, m = map(int,input().split())
edges = []
dist = [-INF] * (n+1)
path = [0] * (n+1)

for _ in range(m):
    edges.append(tuple(map(int,input().split())))

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for cur_node, next_node, edge_cost in edges:
            if dist[cur_node] != -INF and dist[next_node] < dist[cur_node] + edge_cost:
                dist[next_node] = dist[cur_node] + edge_cost
                path[next_node] = cur_node
                if i == n - 1:
                    dist[next_node] = INF

bellman_ford(1)

if dist[n] != INF:
    node = n
    res = [n]
    while node != 1:
        node = path[node]
        res.append(node)
    print(*res[::-1])
else:
    print(-1)