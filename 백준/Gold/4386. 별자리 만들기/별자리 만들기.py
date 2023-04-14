import sys
def input(): return sys.stdin.readline().rstrip()
from math import sqrt

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v = int(input())
e = v * (v-1) // 2

parent = [i for i in range(v+1)]

edges = []
result = 0

vertices = [tuple(map(float,input().split())) for _ in range(v)]

for i in range(v):
    for j in range(i+1, v):
        edges.append(( (vertices[i][0]-vertices[j][0])**2 + (vertices[i][1]-vertices[j][1])**2, i+1, j+1))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += sqrt(cost)

print(result)