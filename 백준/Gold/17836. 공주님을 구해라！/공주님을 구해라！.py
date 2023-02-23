import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

N, M, T  = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited_gram = T+1

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    global visited_gram
    q = deque([(0,0)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 2:
                    tmp = visited[x][y]+1 + N-1-nx + M-1-ny
                    visited_gram = min(visited_gram, tmp)
                if not visited[nx][ny] and graph[nx][ny] != 1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

bfs()
visited_notgram = visited[N-1][M-1]

if 0 < visited_gram <= T and not 0 < visited_notgram <= T:
    print(visited_gram)
elif not 0 < visited_gram <= T and 0 < visited_notgram <= T:
    print(visited_notgram)
elif 0 < visited_gram <= T and 0 < visited_notgram <= T:
    print(visited_gram if visited_gram < visited_notgram else visited_notgram)
else:
    print("Fail")