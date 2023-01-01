import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import permutations

n, m = map(int,input().split())
a = list(map(int,input().split()))

for i in sorted(set(permutations(a,m))):
    print(*i)