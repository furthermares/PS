import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = list(map(int, input().split()))

l, r = 0, 1
cnt = 0

while l <= r and r <= N:
    total = sum(A[l:r])
    if total == M:
        cnt += 1
        r += 1
    elif total > M:
        l += 1
    else:
        r += 1

print(cnt)