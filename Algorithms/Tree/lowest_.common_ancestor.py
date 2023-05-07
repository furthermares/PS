# https://boj.kr/11438
"""
# Input data range
2 ≤ No. of Nodes ≤ 100,000
1 ≤ No. of Node pairs ≤ 100,000

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

h = 21 # = 1 + math.ceil(math.log2(1000000))
parent = [[0] * h for _ in range(n + 1)] # parent node
d = [0] * (n + 1) # node depth
visited = [False] * (n + 1) # check if node is visited
graph = [[] for _ in range(n + 1)] # graph info

for _ in range(n - 1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# Get depth
def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for y in graph[x]:
        if visited[y]:
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

# set parents for all nodes
def set_parent():
    dfs(1, 0) # Root node is 1
    for i in range(1, h):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# Find LCA
def lca(a, b):
    # Make b to be the deeper one
    if d[a] > d[b]:
        a, b = b, a
    # Make their depth equal
    for i in range(h - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # Make their parents same
    if a == b:
        return a;
    for i in range(h - 1, -1, -1):
        # travese through ancestors
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

set_parent()

for i in range(int(input())):
    a, b = map(int,input().split())
    print(lca(a, b))
