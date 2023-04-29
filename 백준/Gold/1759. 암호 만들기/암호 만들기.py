import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import combinations

L, C = map(int, input().split())

A = input().split()
A.sort()

for pwd in combinations(A, L):
    cnt = 0
    for i in pwd:
        if i in ('a', 'e', 'i', 'o', 'u'):
            cnt += 1
            
    if 1 <= cnt <= L - 2:
        print(''.join(pwd))