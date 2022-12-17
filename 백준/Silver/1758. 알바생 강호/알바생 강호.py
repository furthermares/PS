import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import permutations

N = int(input())
data=[]
for _ in range(N):
    data.append(int(input()))

value=0
rank=1
for j in sorted(data, reverse=True):
    tip = j - rank + 1
    if tip <= 0:
        continue
    value += tip
    rank += 1
print(value)