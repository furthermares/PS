import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import combinations

a = []
for _ in range(9):
    a.append(int(input()))
a.sort()
for i in combinations(a,7):
    if sum(i) == 100:
        for j in range(7):
            print(i[j])
        break