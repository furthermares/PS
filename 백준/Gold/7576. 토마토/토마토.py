import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [1,-1,0,0], [0,0,1,-1]

q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i,j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx,ny])

bfs()

ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans - 1)