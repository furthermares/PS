""" Input data range
2 ≤ No. of Nodes ≤ 50,000
1 ≤ No. of Node pairs ≤ 10,000
"""
""" Input, Output, Size, etc.
https://boj.kr/11437
"""

import sys
sys.setrecursionlimit(10**5)

n = int(input())

parent = [0] * (n+1) # parent node
d = [0] * (n+1) # node depth
visited = [False] * (n+1) # check if node is visited
graph = [[] for _ in range(n+1)] # graph info

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# Get depth
def get_depth(x, depth):
    visited[x] = True
    d[x] = depth
    for y in graph[x]:
        if visited[y]:
            continue
        parent[y] = x
        get_depth(y, depth + 1)

# Find LCA
def lca(a, b):
    # First make their depth equal
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # until their nodes become the same
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

get_depth(1, 0) # Root node is 1

m = int(input())

for i in range(m):
    a, b = map(int,input().split())
    print(lca(a, b))
