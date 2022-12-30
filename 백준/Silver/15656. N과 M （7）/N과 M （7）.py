import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import product

n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

for i in product(a, repeat=m):
    print(*i)
