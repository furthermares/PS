import sys
def input(): return sys.stdin.readline().rstrip()

MAX = 10 + 1

d=[[] for _ in range(MAX)]

d[1].append('1')
d[2].append('1+1')
d[2].append('2')
d[3].append('1+1+1')
d[3].append('1+2')
d[3].append('2+1')
d[3].append('3')

for i in range(4, MAX):
    for j in d[i-1]:
        d[i].append(j+"+1")
    for j in d[i-2]:
        d[i].append(j+"+2")
    for j in d[i-3]:
        d[i].append(j+"+3")

N, K = map(int, input().split())

d[N].sort()

if len(d[N]) < K:
    print(-1)
else:
    print(d[N][K-1])