import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

N, L, R = map(int,input().split())
A=[]
for r in range(N):
    A.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0

def get_unions(x,y):
    unions = []
    unions.append((x,y))
    
    q = deque()
    q.append((x,y))

    union_sum=A[x][y]
        
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1:
                if L <= abs(A[x][y]-A[nx][ny]) <= R:
                    q.append((nx,ny))
                    unions.append((nx,ny))
                    union_sum += A[nx][ny]
                    visited[nx][ny] = 1

    for i, j in unions:
        A[i][j] = union_sum // len(unions)
    
while True:
    turn = 0
    visited = [[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                get_unions(i,j)
                turn += 1
    if turn == N*N:
        break
    res+=1

print(res)