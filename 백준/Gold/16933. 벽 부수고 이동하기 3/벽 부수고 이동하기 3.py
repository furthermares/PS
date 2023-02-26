from sys import stdin
def input(): return stdin.readline().rstrip()
from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * M for _ in range(N)] for _ in range(K+1)]
for i in range(K+1):
    visited[i][0][0] = 1

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    q = deque([(0,0,0,True)])
    q2 = deque()
    q3 = deque()
    while q:
        while q:
            z,x,y,isDay = q.popleft()
            
            if x == N-1 and y == M-1:
                return visited[z][x][y]

            for i in range(4):

                #chk
                """print(isDay)
                for j in range(K+1):
                    for k in range(N):
                        print(*visited[j][k])
                    print()"""
                
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 1 and z < K and not visited[z+1][nx][ny]:
                        if isDay:
                            q2.append((z+1, nx, ny, False))
                            visited[z+1][nx][ny] = visited[z][x][y] + 1
                        else:
                            q3.append((z+1, nx, ny, False))
                            visited[z+1][nx][ny] = visited[z][x][y] + 2
                    elif graph[nx][ny] == 0 and not visited[z][nx][ny]:
                        q2.append((z, nx, ny, False if isDay else True))
                        visited[z][nx][ny] = visited[z][x][y] + 1
                        
        #q -> q2 -> q3
        q, q2, q3 = q2, q3, deque()
        if not q:
            q, q2 = q2, deque()

        #chk
        """print(isDay)
        for j in range(1,K+1):
            for k in range(N):
                print(*visited[j][k])
            print()"""
                
    return -1

#chk
"""print()
for i in range(N):
    print(*graph[i])
print()"""

print(bfs())