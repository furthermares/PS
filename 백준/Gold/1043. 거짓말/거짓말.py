import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

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

N, M = map(int,input().split())
_, *truth = map(int,input().split())

parent = [i for i in range(N+1)]

party = [[] for _ in range(M)]
for i in range(M):
    _, *party[i] = map(int,input().split())
    for j in range(1, len(party[i])):
        union_parent(parent, party[i][0], party[i][j])

truth = [find_parent(parent, i) for i in truth]

cnt = M
for i in range(M):
    for j in party[i]:
        if find_parent(parent, j) in truth:
            cnt -= 1
            break
            
print(cnt)