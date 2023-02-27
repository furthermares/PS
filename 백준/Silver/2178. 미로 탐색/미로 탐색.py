import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return -1

print(bfs(0,0))