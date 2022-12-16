import sys
def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
array=[]
for _ in range(N):
    array.append(int(input()))

INIT = 10001
d = [INIT]*(K+1)
d[0] = 0

for i in range(N):
    for j in range(array[i],K+1):
        if d[j - array[i]] != INIT:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[K] == INIT:
    print(-1)
else:
    print(d[K])