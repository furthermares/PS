import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
graph = [[[0] * 2 for _ in range(M)] for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(M):
        for k in range(2):
            graph[i][j][k] = int(tmp[j])

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    q = deque([[0,0,0]])
    graph[0][0][0] += 1
    graph[0][0][1] += 1
    while q:
        x,y,z = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if z == 0:
                    if graph[nx][ny][0] == 0:
                        q.append([nx,ny,0])
                        graph[nx][ny][0] = graph[x][y][0] + 1
                    if graph[nx][ny][0] == 1:
                        q.append([nx,ny,1])
                        graph[nx][ny][1] = graph[x][y][0] + 1
                else:
                    if graph[nx][ny][1] == 0:
                        q.append([nx,ny,1])
                        graph[nx][ny][1] = graph[x][y][1] + 1

bfs()

N -= 1; M -= 1
if graph[N][M][0] == 0:
    if graph[N][M][1] == 0:
        print(-1)
    else:
        print(graph[N][M][1])
else:
    if graph[N][M][1] == 0:
        print(graph[N][M][0])
    elif graph[N][M][0] < graph[N][M][1]:
        print(graph[N][M][0])
    else:
        print(graph[N][M][1])

"""
print(graph)

tmp = []
for i in range(N+1):
    for j in range(M+1):
        tmp.append(graph[i][j][0])
    print(*tmp)
    tmp = []
print()
tmp = []
for i in range(N+1):
    for j in range(M+1):
        tmp.append(graph[i][j][1])
    print(*tmp)
    tmp = []
"""