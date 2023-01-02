import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import combinations

n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

for i in sorted(set(combinations(a,m))):
    print(*i)