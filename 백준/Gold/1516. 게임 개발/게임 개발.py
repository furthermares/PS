import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

v = int(input())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    time[i], *t, _ = map(int, input().split())
    for j in t:
        graph[j].append(i)
        indegree[i] += 1

dp = time[:]

q = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[now] + time[i])
        if indegree[i] == 0:
            q.append(i)

print(*dp[1:], sep='\n')