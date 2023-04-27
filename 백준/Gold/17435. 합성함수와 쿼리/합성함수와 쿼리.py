import sys
def input(): return sys.stdin.readline().rstrip()

log = 18 # = floor(lg(max(n)=500000))

M = int(input())
F = [0] + list(map(int,input().split()))

sparse = [[0] * (M+1) for _ in range(log+1)]
sparse[0] = F

for i in range(1, log+1):
    for j in range(1, M+1):
        sparse[i][j] = sparse[i-1][sparse[i-1][j]]

for _ in range(int(input())):
    N, X = map(int,input().split())
    
    for i in range(log, -1, -1):
        if N & (1 << i):
            X = sparse[i][X]

    print(X)