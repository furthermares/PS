import sys
def input(): return sys.stdin.readline().rstrip()

def circles_intersect(p1, p2):
    x1,y1,r1 = p1
    x2,y2,r2 = p2
    d = (x1-x2)**2 + (y1-y2)**2
    if d <= (r1+r2)**2:
        return True
    return False

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(input())):
    N = int(input())
    
    Points = []
    for _ in range(N):
        Points.append(tuple(map(int,input().split())))
    
    parent = [i for i in range(N)]
    
    for i in range(N-1):
        for j in range(i+1, N):
            if find_parent(i) != find_parent(j):
                if circles_intersect(Points[i], Points[j]):
                    union_parent(i, j)

    for i in range(N):
        parent[i] = find_parent(parent[i])
    
    print(len(set(parent)))