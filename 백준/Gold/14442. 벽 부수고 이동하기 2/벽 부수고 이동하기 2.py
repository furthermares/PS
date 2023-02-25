import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * M for _ in range(N)] for _ in range(K+1)]
visited[0][0][0] = 1

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    q = deque([(0,0,0)])
    while q:
        z,x,y = q.popleft()
        
        if x == N-1 and y == M-1:
            return visited[z][x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and z < K and not visited[z+1][nx][ny]:
                    q.append((z+1, nx, ny))
                    visited[z+1][nx][ny] = visited[z][x][y] + 1
                elif graph[nx][ny] == 0 and not visited[z][nx][ny]:
                    q.append((z, nx, ny))
                    visited[z][nx][ny] = visited[z][x][y] + 1
    return -1

print(bfs())