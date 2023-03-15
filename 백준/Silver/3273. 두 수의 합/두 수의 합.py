import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = sorted(list(map(int, input().split())))
X = int(input())

l, r = 0, N-1
cnt = 0

while l < r:
    total = A[l] + A[r]
    if total == X:
        cnt += 1
        l += 1
    elif total < X:
        l += 1
    else:
        r -= 1

print(cnt)