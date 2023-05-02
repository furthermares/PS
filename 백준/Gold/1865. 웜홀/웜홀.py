import sys
def input(): return sys.stdin.readline().rstrip()
INF = 10001

def bellman_ford(start):
    dist[start] = 0
    for i in range(N):
        for cur_node, next_node, edge_cost in edges:
            if dist[next_node] > dist[cur_node] + edge_cost:
                dist[next_node] = dist[cur_node] + edge_cost
                if i == N - 1:
                    return True
    return False

for _ in range(int(input())):
    
    N, M, W = map(int,input().split())
    edges = []
    dist = [INF] * (N+1)

    for _ in range(M):
        S,E,T = map(int,input().split())
        edges.append((S,E,T))
        edges.append((E,S,T))
    for _ in range(W):
        S,E,T = map(int,input().split())
        edges.append((S,E,-T))
    
    negative_weight_cycle = bellman_ford(1)

    if negative_weight_cycle: 
        print("YES")
    else:
        print("NO")