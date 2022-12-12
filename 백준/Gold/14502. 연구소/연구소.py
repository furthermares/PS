import sys
def input(): return sys.stdin.readline().rstrip()

#initialize
N,M = map(int,input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

grid_copy=[[0]*M for _ in range(N)]

#virus func with DFS
def virus(i,j):
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<N and 0<=ny<M:
            if grid_copy[nx][ny]==0:
                grid_copy[nx][ny] = 2
                virus(nx,ny)

#get score func
def calc_score():
    return sum(grid_copy[i].count(0) for i in range(N))

#build a wall with DFS
count=0
score=0
def wall(count):
    if count == 3:
        global score

        for i in range(N):
            for j in range(M):
                grid_copy[i][j] = grid[i][j]

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    virus(i,j)
                    
        score=max(score,calc_score())
        return
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                grid[i][j] = 1
                count += 1
                wall(count)
                grid[i][j] = 0
                count -= 1

wall(0)
print(score)