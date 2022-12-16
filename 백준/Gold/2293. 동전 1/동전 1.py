import sys
def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
array=[]
for _ in range(N):
    array.append(int(input()))

d = [1]+[0]*(K)

for i in range(N):
    for j in range(array[i],K+1):
        d[j] += d[j-array[i]]

print(d[K])