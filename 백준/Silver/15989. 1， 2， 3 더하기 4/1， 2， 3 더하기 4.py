import sys
def input(): return sys.stdin.readline().rstrip()

MAX = 10000

d=[1] * (MAX+1)

for i in range(2,MAX+1):
    d[i] += d[i-2]
for i in range(3,MAX+1):
    d[i] += d[i-3]

T = int(input())
for _ in range(T):
    print(d[int(input())])