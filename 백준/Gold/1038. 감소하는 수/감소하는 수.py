import sys
def input(): return sys.stdin.readline().rstrip()
    
from itertools import combinations

lst = []
for i in range(1,11):
    for case in combinations(range(0,10), i):
        case = list(case)
        case.sort(reverse=True)
        lst.append(int("".join(map(str, case))))

lst.sort()

try:
    print(lst[int(input())])
except:
    print(-1)