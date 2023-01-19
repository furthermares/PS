import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
d=[0]*N

A = list(map(int,input().split()))

ans = 0

while sum(A) != 0:
    for i in range(N):
        if A[i] % 2 == 1:
            A[i] -= 1
            ans += 1
    if sum(A) == 0:
        break
    else:
        A = [int(x/2) for x in A]
        ans += 1

print(ans)