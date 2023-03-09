import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

l, r = 0, 1
cnt = 0
total = 1

while l < N//2 + 1:
    if total < N:
        r += 1
        total += r
    elif total == N:
        cnt += 1
        r += 1
        total -= l
        total += r
        l += 1
    else:
        total -= l
        l += 1

print(cnt + 1) if N != 1 else print(1)
