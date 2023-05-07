#https://www.acmicpc.net/problem/11657

import sys
INF = sys.maxsize

# input numbers of nodes and edges
n, m = map(int,input().split())
# list of edges
edges = []
# initialize distance tables to INF
dist = [INF] * (n+1)

# input all edges infos
for _ in range(m):
    a, b, c = map(int,input().split())
    # a -> b costs c
    edges.append((a, b, c))

def bellman_ford(start):
    # initialize starting node to 0
    dist[start] = 0
    # loop for n - 1 rounds
    for i in range(n):
        # check all edges each loop
        for cur_node, next_node, edge_cost in edges:
            # if it's shorter to go past current node to next node
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + edge_cost:
                dist[next_node] = dist[cur_node] + edge_cost
                # if it updates on nth round, it's a negative weight cycle
                if i == n - 1:
                    return True
    return False

# Run Bellman-Ford
negative_weight_cycle = bellman_ford(1) # starting node is 1

if negative_weight_cycle:
    print(-1)
else:
    # print shortest distnace to other nodes (from starting node 1)
    for i in range(2, n+1):
        # if unreachable, print -1
        if dist[i] == INF:
            print(-1)
        # if reachable, print distance
        else:
            print(dist[i])
