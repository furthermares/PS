import sys
input = lambda: sys.stdin.readline().rstrip()

# Find a set element "x" is in
def find_parent(parent, x):
    # If it's not a root node, call it recursively.
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# input a number of nodes and edges(number of union operations)
v, e = map(int,input().split())

# initalize parents as itself in parent table.
parent = [i for i in range(v+1)]

# edge list and result variable
edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int,input().split())
    # initialize costs as itself for sorting.
    edges.append((cost, a, b))

# sort
edges.sort()

# iterate through edges
for edge in edges:
    cost, a, b = edge
    # if cycle doesn't form, add it to the set.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

"""input
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""
"""output
159
"""
"""complexity
Time: O(ElogE)
"""
