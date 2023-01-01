import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import combinations_with_replacement

n, m = map(int,input().split())
a = [i for i in range(1,n+1)]

for i in combinations_with_replacement(a, m):
    print(*i)
