import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque
MAX = 100001

N, K = map(int, input().split())

visited = [0] * MAX
path = [0] * MAX

def bfs():
    q = deque([N])
    visited[N] = 1
    while q:
        prev = q.popleft()
        for next in [prev-1,prev+1,prev*2]:
            if 0 <= next < MAX:
                if not visited[next]:
                    q.append(next)
                    visited[next] = visited[prev] + 1
                    path[next] = prev

bfs()
print(visited[K] - 1)

ans = []
v = K
while v != N:
    ans.append(v)
    v = path[v]
ans.append(N)
ans.reverse()
print(*ans)