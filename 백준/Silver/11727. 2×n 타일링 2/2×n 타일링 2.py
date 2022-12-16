import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
d = [1]+[1]+[0]*999

for i in range(2,N+1):
    d[i] = (d[i-1] + d[i-2]*2)%10007

print(d[N])