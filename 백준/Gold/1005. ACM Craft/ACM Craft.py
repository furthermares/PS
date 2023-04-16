import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

for _ in range(int(input())):
    v, e = map(int,input().split())
    indegree = [0] * (v+1)
    graph = [[] for i in range(v+1)]
    time = [0] + list(map(int, input().split()))
    dp = time[:]
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
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

    print(dp[int(input())])