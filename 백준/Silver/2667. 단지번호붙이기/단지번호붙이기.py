import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e6))

N = int(input())
visited = [[True if i == "0" else False for i in input()] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#visited = [[False] * N for _ in range(N)]
def dfs(x,y):
    global depth
    visited[x][y] = True
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X == N or Y < 0 or Y == N:
            continue
        if not visited[X][Y]:
            depth += 1
            dfs(X, Y)

cnt = 0
tmp = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            depth = 1
            dfs(i, j)
            tmp.append(depth)
            cnt += 1

print(cnt)

tmp.sort()
print(*tmp, sep='\n')