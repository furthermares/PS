import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
d = [0]+[1]+[0]*89

for i in range(2,N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])