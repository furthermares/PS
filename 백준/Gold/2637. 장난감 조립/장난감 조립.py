import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

v = int(input())
e = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
price = [[0] * (v+1) for _ in range(v+1)]

for _ in range(e):
    x, y, k = map(int,input().split())
    graph[y].append((x, k))
    indegree[x] += 1

basics = []
q = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        basics.append(i)
        q.append(i)

while q:
    now = q.popleft()
    for part, cnt in graph[now]:
        if now in basics:
            price[part][now] += cnt
        else:
            for i in range(1, v+1):
                price[part][i] += price[now][i] * cnt
        indegree[part] -= 1
        if indegree[part] == 0:
            q.append(part)

for i in range(v+1):
    if price[v][i]:
        print(i, price[v][i])