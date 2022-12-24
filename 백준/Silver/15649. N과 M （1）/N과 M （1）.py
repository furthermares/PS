import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import permutations

n, m = map(int,input().split())
a = [i for i in range(1,n+1)]

for i in permutations(a,m):
    print(*i)