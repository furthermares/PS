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

cycle = False    # check for a cycle

for _ in range(e):
    a, b = map(int,input().split())
    # if it cycles, break
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

# Checking for connections
print('set each element is in: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('parent table: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

"""input
6 4
1 4
2 3
2 4
5 6
"""
"""output
set each element is in: 1 1 1 1 5 5 
parent table: 1 1 1 1 5 5
"""
"""complexity
time: O(V + M(1 + log_(2-M/V) V) ≈ O(V + M * log_2 V)
"""

# Checking for cycles
if cycle:
    print("Cycle formed.")
else:
    print("Cycle not formed.")

"""input
3 3
1 2
1 3
2 3
"""
