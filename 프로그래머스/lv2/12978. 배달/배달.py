from queue import PriorityQueue

def dijkstra(road, N):
    q = PriorityQueue()
    q.put([1, 0])
    
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    
    while not q.empty():
        current, current_cost = q.get()
        for src, dest, cost in road:
            next_cost = cost + current_cost
            if src == current and next_cost < dist[dest]:
                dist[dest] = next_cost
                q.put([dest, next_cost])
            elif dest == current and next_cost < dist[src]:
                dist[src] = next_cost
                q.put([src, next_cost])
    return dist

def solution(N, road, K):
    return len([i for i in dijkstra(road, N) if i <= K])