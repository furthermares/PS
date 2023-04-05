import sys
input = lambda: sys.stdin.readline().rstrip()

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
M = int(input())

parent = [i for i in range(v+1)]

for i in range(v):
    parent_table = list(map(int,input().split()))
    for j in range(v):
        if parent_table[j]:
            union_parent(parent, i+1, j+1)

path = list(map(int,input().split()))
start = parent[path[0]]
for i in range(M):
    if find_parent(parent, path[i]) != start:
        print("NO")
        break
else:
    print("YES")