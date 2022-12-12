import sys
def input(): return sys.stdin.readline().rstrip()

from collections import deque

N, M, K, X = map(int, input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

visited=[-1]*(N+1)
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start] = 0
    while(queue):
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] +1
            
bfs(graph,X,visited)

flag=False
for i in range(1,N+1):
    if visited[i] == K:
        print(i)
        flag=True

if flag == False:
    print(-1)