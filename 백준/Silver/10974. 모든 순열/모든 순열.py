import sys
def input(): return sys.stdin.readline().rstrip()
    
from itertools import permutations

for i in permutations(range(1,int(input())+1)):
    print(*i)