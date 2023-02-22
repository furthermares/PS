import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx, dy, dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0],[0,0,0,0,1,-1]

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append([i,j,k])
    
def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    q.append([nx,ny,nz])

bfs()

ans = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))
print(ans - 1)