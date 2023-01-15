import sys
def input(): return sys.stdin.readline().rstrip()

MAX = 1000001
MOD = 1000000009

d=[0,1,2,2,3,3,6] + [0]*(MAX-7)

for i in range(7,MAX):
    d[i] += (d[i-2] + d[i-4] + d[i-6]) % MOD

T = int(input())
for _ in range(T):
    print(d[int(input())])