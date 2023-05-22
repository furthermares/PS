import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import permutations

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, s, e):
        self.s = s
        self.e = e

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

N = int(input())
R = [Point(*map(int,input().split())) for _ in range(N)]
S = [Point(*map(int,input().split())) for _ in range(N)]

for case in permutations(range(N), N):
    for i in range(N):
        l1 = Line(R[i], S[case[i]])
        for j in range(i+1, N):
            if lines_intersect(l1, Line(R[j], S[case[j]])):
                break
        else:
            continue
        break
    else:
        for i in case:
            print(i+1)
        break