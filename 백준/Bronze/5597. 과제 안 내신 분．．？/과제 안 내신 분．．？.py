import sys
def input(): return sys.stdin.readline().rstrip()

N=[]
for i in range(28):
    N.append(int(input()))

N.sort()
for i in range(1,31):
    if i not in N: print(i)