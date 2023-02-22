import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque
MAX = 100001

N, K = map(int, input().split())

visited = [0] * MAX
def bfs():
    q = deque([N])
    visited[N] = 1
    while q:
        prev = q.popleft()
        for next in [prev-1,prev+1,prev*2]:
            if 0 <= next < MAX:
                if not visited[next]:
                    if visited[next] < visited[prev] + 1:
                        q.append(next)
                        visited[next] = visited[prev] + 1

bfs()
print(visited[K] - 1)