import sys
def input(): return sys.stdin.readline().rstrip()
from collections import Counter

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, xs, ys, xe, ye):
        self.s = Point(xs, ys)
        self.e = Point(xe, ye)

def on_segment(p, q, r):
    if q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y):
        return True
    return False

def ccw(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

def lines_intersect(l1, l2):
    p1, q1 = l1.s, l1.e
    p2, q2 = l2.s, l2.e
    
    o1 = ccw(p1, q1, p2)
    o2 = ccw(p1, q1, q2)
    o3 = ccw(p2, q2, p1)
    o4 = ccw(p2, q2, q1)

    if ((o1 != o2) and (o3 != o4)): return True
    if ((o1 == 0) and on_segment(p1, p2, q1)): return True
    if ((o2 == 0) and on_segment(p1, q2, q1)): return True
    if ((o3 == 0) and on_segment(p2, p1, q2)): return True
    if ((o4 == 0) and on_segment(p2, q1, q2)): return True

    return False

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N = int(input())

Lines = []
for _ in range(N):
    Lines.append(Line(*map(int,input().split())))

parents = [i for i in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if find_parent(i) != find_parent(j):
            if lines_intersect(Lines[i], Lines[j]):
                union_parent(i, j)

for i in range(N):
    parents[i] = find_parent(parents[i])

print(len(set(parents)))
print(Counter(parents).most_common()[0][1])