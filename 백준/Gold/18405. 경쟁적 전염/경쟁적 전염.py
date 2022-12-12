import sys
def input(): return sys.stdin.readline().rstrip()

N, K = map(int,input().split())
grid=[]
viruses=[]
for i in range(N):
    grid.append(list(map(int,input().split())))
    for j in range(N):
        if grid[i][j] != 0:
            viruses.append([grid[i][j], 0, i, j])
S, X, Y = map(int,input().split())

from collections import deque
viruses.sort()
viruses=deque(viruses)

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

while viruses:
    virus, s, x, y = viruses.popleft()
    if s == S:
        break

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if grid[nx][ny] == 0:
                grid[nx][ny] = virus
                viruses.append([virus, s+1, nx, ny])

print(grid[X-1][Y-1])