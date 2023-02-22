import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque
MAX = 100001

N, K = map(int, input().split())

visited = [0] * MAX
def bfs():
    global cnt
    q = deque([N])
    visited[N] = 1
    while q:
        prev = q.popleft()
        if prev == K:
            cnt += 1
        for next in [prev-1,prev+1,prev*2]:
            if 0 <= next < MAX:
                if not visited[next] or visited[next] >= visited[prev] + 1:
                    q.append(next)
                    visited[next] = visited[prev] + 1
                        
cnt = 0
bfs()
print(visited[K] - 1)
print(cnt)