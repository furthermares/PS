import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    q = deque([(0,0,0)])
    while q:
        x,y,z = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and z == 0:
                    q.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][0] + 1
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
    return -1

print(bfs())