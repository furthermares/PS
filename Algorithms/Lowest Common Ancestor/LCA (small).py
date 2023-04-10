"""
# Input data range
2 ≤ No. of Nodes ≤ 50,000
1 ≤ No. of Node pairs ≤ 10,000

# Info
https://boj.kr/11437

# Input
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15

# Output
2
4
2
1
3
1
"""

import sys
sys.setrecursionlimit(10**5)

n = int(input())

parent = [0] * (n + 1) # parent node
d = [0] * (n + 1) # node depth
visited = [False] * (n + 1) # check if node is visited
graph = [[] for _ in range(n + 1)] # graph info

for _ in range(n - 1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# Get depths
def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for y in graph[x]:
        if visited[y]:
            continue
        parent[y] = x
        dfs(y, depth + 1)

# Find LCA
def lca(a, b):
    # First make their depth equal
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # Traverse through their ancestors until the nodes become the same
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0) # Root node is 1

for i in range(int(input())):
    a, b = map(int,input().split())
    print(lca(a, b))
