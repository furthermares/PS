import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N-1):
    A[i+1][0] += min(A[i][1], A[i][2])
    A[i+1][1] += min(A[i][0], A[i][2])
    A[i+1][2] += min(A[i][0], A[i][1])

print(min(A[-1]))