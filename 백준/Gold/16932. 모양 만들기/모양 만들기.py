#https://www.acmicpc.net/problem/16932
def input(): return __import__('sys').stdin.readline().rstrip()
from collections import deque

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        shapes[x][y] = group
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt

def cnt_sum(x,y):
    data = set()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if shapes[nx][ny]:
                data.add(shapes[nx][ny])
    cnt = 1
    for c in data:
        cnt += info[c]
    return cnt
    
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
shapes = [[0] * M for _ in range(N)]

group = 1
info = {}

for i in range(N):
    for j in range(M):
        if graph[i][j] and not visited[i][j]:
            cnt = bfs(i,j)
            info[group] = cnt
            group += 1

ans = []
for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            ans.append(cnt_sum(i,j))
            
print(max(ans))