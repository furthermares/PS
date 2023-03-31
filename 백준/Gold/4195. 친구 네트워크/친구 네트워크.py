import sys
input = lambda: sys.stdin.readline().rstrip()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]

for _ in range(int(input())):
    parent = {}
    cnt = {}
    
    for _ in range(int(input())):
        a, b = input().split()

        for i in a, b:
            if i not in parent:
                parent[i] = i
                cnt[i] = 1

        union_parent(parent, a, b)
        print(cnt[find_parent(parent, a)])